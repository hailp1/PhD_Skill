"""
H-AI ResearchLAB | ACADEMIC KNOWLEDGE DATABASE ENGINE (SQLite + FTS5)
Tác giả: H-AI ResearchLAB (DR. HAI 02 - Literature Reviewer & DR. HAI 04 - Data Scientist)
Chức năng:
1. Tạo và quản lý Database học thuật chuẩn hóa `lab_projects/ACADEMIC_KNOWLEDGE_BASE.db` (SQLite).
2. Thiết lập cấu trúc Schema chuẩn hóa:
   - `papers`: Lưu DOI, Title, Journal, Year, Citations, Abstract, FullText_Clean, PDF_Path, Source.
   - `authors`: Lưu danh sách tác giả và liên kết nhiều-nhiều.
   - `construct_scales`: Lưu các thang đo (Item code, Item wording tiếng Anh/Việt, Scale type, Source paper).
   - `papers_fts`: Bảng ảo FTS5 (Full-Text Search) cho phép tìm kiếm từ khóa siêu tốc trên toàn bộ Full-Text và Abstract.
3. Cung cấp hàm nạp tự động (Ingest Engine):
   - Nạp từ Master Corpus JSON (`lab_projects/ACADEMIC_LITERATURE_MASTER_CORPUS.json`).
   - Nạp từ tập VOSviewer CSV (`data/processed/dimensions_clean_included.csv`).
   - Nạp toàn văn Markdown đã bóc tách từ PDF (`lab_projects/parsed_markdown/`).
4. Cung cấp API truy vấn nhanh (Search & Retrieval).
"""

import sys
import os
import sqlite3
import json
import re
import pandas as pd
from datetime import datetime

WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DB_PATH = os.path.join(WORKSPACE_DIR, "lab_projects", "ACADEMIC_KNOWLEDGE_BASE.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_academic_database():
    """
    Khởi tạo cấu trúc Database học thuật chuẩn hóa quốc tế với FTS5.
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    # 1. Bảng bài báo chính (Papers)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS papers (
        paper_id INTEGER PRIMARY KEY AUTOINCREMENT,
        doi TEXT UNIQUE,
        title TEXT NOT NULL,
        journal TEXT,
        year INTEGER,
        citations INTEGER DEFAULT 0,
        abstract TEXT,
        fulltext_markdown TEXT,
        pdf_path TEXT,
        source_origin TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    
    # 2. Bảng tác giả (Authors)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS authors (
        author_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    );
    """)
    
    # 3. Bảng liên kết Bài báo - Tác giả (Many-to-Many)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS paper_authors (
        paper_id INTEGER,
        author_id INTEGER,
        author_order INTEGER DEFAULT 1,
        PRIMARY KEY (paper_id, author_id),
        FOREIGN KEY (paper_id) REFERENCES papers(paper_id) ON DELETE CASCADE,
        FOREIGN KEY (author_id) REFERENCES authors(author_id) ON DELETE CASCADE
    );
    """)
    
    # 4. Bảng thang đo & biến số trích xuất (Construct Scales & Measurement Items)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS construct_scales (
        scale_id INTEGER PRIMARY KEY AUTOINCREMENT,
        paper_id INTEGER,
        construct_code TEXT NOT NULL,
        construct_name TEXT NOT NULL,
        item_code TEXT NOT NULL,
        item_wording_en TEXT NOT NULL,
        item_wording_vi TEXT,
        scale_points INTEGER DEFAULT 7,
        factor_loading REAL,
        FOREIGN KEY (paper_id) REFERENCES papers(paper_id) ON DELETE CASCADE
    );
    """)
    
    # 5. Bảng tìm kiếm toàn văn FTS5 (Full-Text Search Virtual Table)
    cursor.execute("""
    CREATE VIRTUAL TABLE IF NOT EXISTS papers_fts USING fts5(
        title,
        abstract,
        fulltext_markdown,
        content=papers,
        content_rowid=paper_id
    );
    """)
    
    # 6. Các Triggers để tự động đồng bộ hóa FTS5
    cursor.execute("""
    CREATE TRIGGER IF NOT EXISTS papers_ai AFTER INSERT ON papers BEGIN
        INSERT INTO papers_fts(rowid, title, abstract, fulltext_markdown) 
        VALUES (new.paper_id, new.title, new.abstract, new.fulltext_markdown);
    END;
    """)
    cursor.execute("""
    CREATE TRIGGER IF NOT EXISTS papers_ad AFTER DELETE ON papers BEGIN
        INSERT INTO papers_fts(papers_fts, rowid, title, abstract, fulltext_markdown) 
        VALUES('delete', old.paper_id, old.title, old.abstract, old.fulltext_markdown);
    END;
    """)
    cursor.execute("""
    CREATE TRIGGER IF NOT EXISTS papers_au AFTER UPDATE ON papers BEGIN
        INSERT INTO papers_fts(papers_fts, rowid, title, abstract, fulltext_markdown) 
        VALUES('delete', old.paper_id, old.title, old.abstract, old.fulltext_markdown);
        INSERT INTO papers_fts(rowid, title, abstract, fulltext_markdown) 
        VALUES (new.paper_id, new.title, new.abstract, new.fulltext_markdown);
    END;
    """)
    
    conn.commit()
    conn.close()
    print(f"✅ Đã khởi tạo cấu trúc SQLite Database học thuật chuẩn hóa FTS5 tại: {DB_PATH}")

def ingest_master_corpus():
    """
    Nạp dữ liệu từ file ACADEMIC_LITERATURE_MASTER_CORPUS.json vào Database.
    """
    corpus_path = os.path.join(WORKSPACE_DIR, "lab_projects", "ACADEMIC_LITERATURE_MASTER_CORPUS.json")
    if not os.path.exists(corpus_path):
        print(f"⚠️ Chưa có file: {corpus_path}")
        return
        
    with open(corpus_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    papers = data.get("papers", [])
    conn = get_connection()
    cursor = conn.cursor()
    ingested = 0
    
    for p in papers:
        doi = p.get("doi") or f"openalex_{p.get('id', '')}"
        title = p.get("title", "")
        journal = p.get("journal", "")
        year = p.get("year")
        try:
            year = int(year) if year and str(year).isdigit() else None
        except Exception:
            year = None
        cites = p.get("citations", 0)
        abstract = p.get("abstract", "")
        
        cursor.execute("""
        INSERT INTO papers (doi, title, journal, year, citations, abstract, source_origin)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(doi) DO UPDATE SET
            citations = excluded.citations,
            abstract = COALESCE(excluded.abstract, papers.abstract);
        """, (doi, title, journal, year, cites, abstract, "OpenAlex"))
        
        # Lấy paper_id
        cursor.execute("SELECT paper_id FROM papers WHERE doi = ?", (doi,))
        row = cursor.fetchone()
        if row:
            paper_id = row[0]
            for order, author_name in enumerate(p.get("authors", [])):
                if author_name:
                    cursor.execute("INSERT OR IGNORE INTO authors (name) VALUES (?)", (author_name.strip(),))
                    cursor.execute("SELECT author_id FROM authors WHERE name = ?", (author_name.strip(),))
                    auth_row = cursor.fetchone()
                    if auth_row:
                        author_id = auth_row[0]
                        cursor.execute("""
                        INSERT OR IGNORE INTO paper_authors (paper_id, author_id, author_order)
                        VALUES (?, ?, ?)
                        """, (paper_id, author_id, order + 1))
        ingested += 1
        
    conn.commit()
    conn.close()
    print(f"📥 Đã nạp thành công {ingested} bài báo từ Master Corpus vào SQLite Database!")

def ingest_parsed_markdown_fulltext():
    """
    Đọc các file toàn văn Markdown đã bóc tách từ PDF và cập nhật vào trường fulltext_markdown trong DB.
    """
    md_dir = os.path.join(WORKSPACE_DIR, "lab_projects", "parsed_markdown")
    if not os.path.exists(md_dir):
        return
        
    conn = get_connection()
    cursor = conn.cursor()
    updated = 0
    
    for f in os.listdir(md_dir):
        if f.endswith(".md"):
            file_path = os.path.join(md_dir, f)
            with open(file_path, "r", encoding="utf-8") as mdf:
                content = mdf.read()
                
            base_key = os.path.splitext(f)[0] # ví dụ shanahan_2019
            # Tìm kiếm bài báo tương ứng trong DB dựa trên từ khóa trong tiêu đề
            keyword = base_key.split("_")[0] # ví dụ shanahan
            cursor.execute("SELECT paper_id, title FROM papers WHERE title LIKE ? OR fulltext_markdown IS NULL", (f"%{keyword}%",))
            matches = cursor.fetchall()
            
            for pid, title in matches:
                cursor.execute("""
                UPDATE papers SET fulltext_markdown = ?, pdf_path = ? WHERE paper_id = ?
                """, (content, f"data/references/{base_key}.pdf", pid))
                updated += 1
                print(f"  -> Đã nạp Full-Text Markdown vào DB cho bài: {title[:60]}...")
                break
                
    conn.commit()
    conn.close()
    print(f"📑 Đã đồng bộ Full-Text Markdown cho {updated} bài báo hạt nhân!")

def ingest_vosviewer_dataset(max_records=500):
    """
    Nạp dữ liệu 1,441 bài báo VOSviewer (PRISMA 2020) vào SQLite DB.
    """
    csv_path = os.path.join(WORKSPACE_DIR, "data", "processed", "dimensions_clean_included.csv")
    if not os.path.exists(csv_path):
        return
        
    df = pd.read_csv(csv_path).head(max_records)
    conn = get_connection()
    cursor = conn.cursor()
    count = 0
    
    for _, r in df.iterrows():
        doi = str(r.get('DOI', '')).strip()
        if not doi or doi == 'nan':
            continue
        title = str(r.get('Title', '')).strip()
        journal = str(r.get('Source title/Anthology title', '')).strip()
        year = r.get('PubYear')
        try:
            year = int(year) if not pd.isna(year) else None
        except Exception:
            year = None
        cites = r.get('Times cited', 0)
        try:
            cites = int(cites) if not pd.isna(cites) else 0
        except Exception:
            cites = 0
        abstract = str(r.get('Abstract', '')) if not pd.isna(r.get('Abstract')) else ""
        
        cursor.execute("""
        INSERT INTO papers (doi, title, journal, year, citations, abstract, source_origin)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(doi) DO UPDATE SET
            citations = MAX(papers.citations, excluded.citations),
            abstract = CASE WHEN papers.abstract IS NULL OR papers.abstract = '' THEN excluded.abstract ELSE papers.abstract END;
        """, (doi, title, journal, year, cites, abstract, "VOSviewer_PRISMA"))
        count += 1
        
    conn.commit()
    conn.close()
    print(f"📊 Đã nạp thành công {count} bài báo từ kho VOSviewer PRISMA 2020 vào SQLite Database!")

def query_database_fulltext(search_term, limit=5):
    """
    Truy vấn siêu tốc bằng FTS5 trên toàn bộ Title, Abstract và FullText.
    """
    conn = get_connection()
    cursor = conn.cursor()
    print(f"\n🔎 [TRUY VẤN FTS5 DATABASE] Từ khóa: '{search_term}'")
    
    cursor.execute("""
    SELECT p.paper_id, p.year, p.title, p.journal, p.citations, p.doi,
           snippet(papers_fts, 1, '<b>', '</b>', '...', 20) as matched_abstract
    FROM papers_fts
    JOIN papers p ON papers_fts.rowid = p.paper_id
    WHERE papers_fts MATCH ?
    ORDER BY rank
    LIMIT ?;
    """, (search_term, limit))
    
    rows = cursor.fetchall()
    print(f"  -> Tìm thấy {len(rows)} bài báo khớp hoàn hảo:")
    for r in rows:
        print(f"  📌 [{r[1]}] {r[2][:70]}...")
        print(f"      Tạp chí: {r[3]} | Cites: {r[4]} | DOI: {r[5]}")
        print(f"      Đoạn trích: {r[6]}\n")
    conn.close()
    return rows

def generate_database_stats_report():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM papers;")
    total_papers = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM papers WHERE fulltext_markdown IS NOT NULL;")
    total_fulltext = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM authors;")
    total_authors = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM papers WHERE abstract IS NOT NULL AND abstract != '';")
    total_abstracts = cursor.fetchone()[0]
    conn.close()
    
    print("=" * 85)
    print("🏛️ H-AI ResearchLAB | BÁO CÁO TỔNG QUAN DATABASE HỌC THUẬT (SQLITE FTS5)")
    print(f"- Tổng số bài báo khoa học đã nạp: {total_papers:,} bài")
    print(f"- Số bài có đầy đủ Abstract: {total_abstracts:,} bài")
    print(f"- Số bài đã nạp Toàn văn Full-Text Markdown: {total_fulltext} bài")
    print(f"- Tổng số tác giả khoa học được lập chỉ mục: {total_authors:,} tác giả")
    print(f"- Đường dẫn tệp CSDL: lab_projects/ACADEMIC_KNOWLEDGE_BASE.db")
    print("=" * 85)

def main():
    init_academic_database()
    ingest_master_corpus()
    ingest_vosviewer_dataset(max_records=500)
    ingest_parsed_markdown_fulltext()
    generate_database_stats_report()
    query_database_fulltext("impulse buying recommendation", limit=3)

if __name__ == "__main__":
    main()
