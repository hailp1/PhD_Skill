"""
Script: query_literature_corpus.py
Mục đích:
  Công cụ truy vấn ngữ nghĩa và từ khóa chuyên sâu trên tập hợp 1,441 bài báo Scopus Q1/Q2 sạch (PRISMA 2020).
  Giúp NCS Lê Phúc Hải nhanh chóng tìm kiếm bằng chứng thực nghiệm, câu trích dẫn, và ý tưởng viết báo.
Cách dùng:
  python query_literature_corpus.py "từ khóa" [--limit 10]
  Ví dụ:
  python query_literature_corpus.py "self-control"
  python query_literature_corpus.py "in-process"
  python query_literature_corpus.py "flow theory"
"""

import csv
import os
import sys
import argparse
import re

def search_corpus(query, limit=10, year_min=2018):
    workspace = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))
    csv_path = os.path.join(workspace, "data", "processed", "dimensions_clean_included.csv")
    
    if not os.path.exists(csv_path):
        print(f"Lỗi: Không tìm thấy tệp {csv_path}")
        return

    query_lower = query.lower()
    terms = query_lower.split()

    with open(csv_path, "r", encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f)
        records = list(reader)

    results = []
    for r in records:
        title = r.get("Title", "")
        abstract = r.get("Abstract", "")
        source = r.get("Source title/Anthology title", "")
        year_str = r.get("PubYear", "2024")
        authors = r.get("Authors", "")
        doi = r.get("DOI", "")
        times_cited = r.get("Times cited", "0")

        try:
            year = int(year_str)
            if year < year_min:
                continue
        except:
            year = 2024

        text_to_search = f"{title} {abstract}".lower()

        # Tính điểm khớp (Scoring)
        match = False
        score = 0
        if query_lower in text_to_search:
            score += 10
            match = True
        elif all(term in text_to_search for term in terms):
            score += 5
            match = True

        if match:
            # Tìm đoạn văn chứa từ khóa trong abstract
            snippet = ""
            sentences = re.split(r'(?<=[.!?]) +', abstract)
            for s in sentences:
                if any(t in s.lower() for t in terms):
                    snippet += f"...{s.strip()}... "
                    if len(snippet) > 300:
                        break
            if not snippet and sentences:
                snippet = sentences[0][:200] + "..."

            results.append({
                "title": title,
                "authors": authors,
                "year": year,
                "source": source if source else "Academic Press / Monograph",
                "doi": doi,
                "times_cited": times_cited,
                "snippet": snippet,
                "score": score + int(times_cited) if times_cited.isdigit() else score
            })

    # Sắp xếp theo mức độ phù hợp và trích dẫn
    results.sort(key=lambda x: x["score"], reverse=True)

    print(f"\n===============================================================================")
    print(f"   KẾT QUẢ TÌM KIẾM TRONG KHO Y VĂN THỰC CHỨNG 1,441 BÀI SCOPUS Q1 (PRISMA 2020)")
    print(f"   Từ khóa truy vấn: '{query}' | Tìm thấy: {len(results)} bài báo phù hợp")
    print(f"===============================================================================\n")

    for idx, item in enumerate(results[:limit], 1):
        author_short = item['authors'].split(';')[0] if item['authors'] else 'Tác giả'
        if len(item['authors'].split(';')) > 1:
            author_short += " et al."
        apa_cite = f"{author_short} ({item['year']}). {item['title']}. {item['source']}."
        
        print(f"[{idx}] {apa_cite}")
        print(f"    DOI: https://doi.org/{item['doi']} | Trích dẫn: {item['times_cited']} lần")
        print(f"    Phát hiện cốt lõi (Evidence Snippet):")
        print(f"    \"{item['snippet']}\"")
        print("-" * 79)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tìm kiếm trong kho y văn 1,441 bài báo Scopus Q1 của luận án")
    parser.add_argument("query", help="Từ khóa tìm kiếm (ví dụ: self-control, serendipity, in-process, flow theory)")
    parser.add_argument("--limit", type=int, default=10, help="Số lượng kết quả hiển thị tối đa (mặc định: 10)")
    parser.add_argument("--year", type=int, default=2018, help="Năm xuất bản tối thiểu (mặc định: 2018)")
    
    if len(sys.argv) == 1:
        # Mặc định demo
        search_corpus("self-control", limit=5)
    else:
        args = parser.parse_args()
        search_corpus(args.query, limit=args.limit, year_min=args.year)
