"""
H-AI ResearchLAB | VOSVIEWER NETWORK FULL-TEXT PDF HARVESTER
Tác giả: H-AI ResearchLAB (DR. HAI 02 - Literature Reviewer)
Chức năng:
1. Đọc kho 1,441 bài báo khoa học chuẩn PRISMA 2020 của đề cương tại:
   `data/processed/dimensions_clean_included.csv`.
2. Lọc ra các bài báo hạt nhân (Core/Landmark Papers) có lượt trích dẫn cao nhất và liên quan trực tiếp đến mạng lưới VOSviewer.
3. Truy vấn Unpaywall & Open Access API để lấy trực tiếp link tải PDF toàn văn.
4. Tải và lưu trữ vào thư mục: `lab_projects/fulltext_papers/vosviewer_core/`.
5. Tạo báo cáo kiểm kê chi tiết: `lab_projects/VOSVIEWER_FULLTEXT_REPORT.md`.
"""

import sys
import os
import json
import re
import ssl
import urllib.parse
import urllib.request
import pandas as pd
from datetime import datetime

WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CSV_PATH = os.path.join(WORKSPACE_DIR, "data", "processed", "dimensions_clean_included.csv")
TARGET_DIR = os.path.join(WORKSPACE_DIR, "lab_projects", "fulltext_papers", "vosviewer_core")

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def sanitize_filename(name):
    name = re.sub(r'[\\/*?:"<>|]', "", str(name))
    name = re.sub(r'\s+', "_", name.strip())
    return name[:60]

def resolve_open_access_pdf(doi, title):
    if not doi or pd.isna(doi):
        return None
    clean_doi = str(doi).strip().split("doi.org/")[-1]
    
    # 1. Thử Unpaywall API
    unpaywall_url = f"https://api.unpaywall.org/v2/{urllib.parse.quote(clean_doi)}?email=phd_candidate@h-ai-lab.edu.vn"
    try:
        req = urllib.request.Request(unpaywall_url, headers={"User-Agent": "H-AI-Lab/2.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=6) as resp:
            if resp.status == 200:
                data = json.loads(resp.read().decode('utf-8'))
                best_oa = data.get("best_oa_location") or {}
                pdf_url = best_oa.get("url_for_pdf") or best_oa.get("url")
                if pdf_url and ("pdf" in pdf_url.lower() or best_oa.get("host_type") in ["repository", "publisher"]):
                    return pdf_url
    except Exception:
        pass
        
    # 2. Thử OpenAlex API
    try:
        alex_url = f"https://api.openalex.org/works/https://doi.org/{urllib.parse.quote(clean_doi)}"
        req = urllib.request.Request(alex_url, headers={"User-Agent": "H-AI-Lab/2.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=6) as resp:
            if resp.status == 200:
                data = json.loads(resp.read().decode('utf-8'))
                oa_url = data.get("open_access", {}).get("oa_url")
                if oa_url:
                    return oa_url
                best_loc = data.get("best_oa_location") or {}
                if best_loc.get("pdf_url"):
                    return best_loc.get("pdf_url")
    except Exception:
        pass

    return None

def download_pdf(url, output_path, timeout=20):
    if not url:
        return False, 0, "NO_URL"
    if "arxiv.org/pdf/" in url and not url.endswith(".pdf"):
        url = url + ".pdf"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept": "application/pdf,application/octet-stream,*/*",
        "Referer": "https://scholar.google.com/"
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=timeout) as response:
            content_type = response.headers.get("Content-Type", "")
            data = response.read()
            if data.startswith(b"%PDF") or "pdf" in content_type.lower():
                with open(output_path, "wb") as f:
                    f.write(data)
                return True, len(data), "OK"
            else:
                return False, len(data), "HTML_REDIRECT"
    except Exception as e:
        return False, 0, str(e)

def run_vosviewer_pdf_harvest(max_papers=20):
    print("=" * 85)
    print("🔬 H-AI ResearchLAB | VOSVIEWER NETWORK FULL-TEXT PDF HARVESTER")
    print(f"Nguồn dữ liệu: {CSV_PATH}")
    print(f"Thư mục lưu bài báo: lab_projects/fulltext_papers/vosviewer_core/")
    print("=" * 85)
    
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR, exist_ok=True)
        
    df = pd.read_csv(CSV_PATH)
    # Lọc bỏ bài không có DOI và sắp xếp theo lượt trích dẫn cao nhất (landmark papers)
    df_clean = df.dropna(subset=['DOI']).copy()
    df_clean['Times cited'] = pd.to_numeric(df_clean['Times cited'], errors='coerce').fillna(0)
    df_sorted = df_clean.sort_values(by='Times cited', ascending=False)
    
    selected_papers = df_sorted.head(max_papers)
    print(f"\n[BƯỚC 1] Đã chọn Top {len(selected_papers)} bài báo hạt nhân trung tâm mạng lưới VOSviewer:")
    
    results = []
    success_count = 0
    
    for i in range(len(selected_papers)):
        row = selected_papers.iloc[i]
        title = str(row['Title']).strip()
        year = str(row['PubYear']) if not pd.isna(row['PubYear']) else "YYYY"
        authors_raw = str(row['Authors']) if not pd.isna(row['Authors']) else "Author"
        first_author = sanitize_filename(authors_raw.split(";")[0].split(",")[0])
        cites = int(row['Times cited'])
        journal = str(row['Source title/Anthology title']) if not pd.isna(row['Source title/Anthology title']) else "Journal"
        doi = str(row['DOI']).strip()
        
        filename = f"{year}_{first_author}_{sanitize_filename(title)}.pdf"
        target_path = os.path.join(TARGET_DIR, filename)
        
        print(f"\n[{i+1}/{len(selected_papers)}] ({year}) {title[:65]}...")
        print(f"      Tạp chí: {journal[:35]} | Trích dẫn: {cites:,} | DOI: {doi}")
        
        pdf_url = resolve_open_access_pdf(doi, title)
        
        if pdf_url:
            print(f"      🔗 Phát hiện Open Access URL: {pdf_url[:75]}...")
            success, size_bytes, msg = download_pdf(pdf_url, target_path)
            if success:
                success_count += 1
                size_mb = size_bytes / (1024 * 1024)
                print(f"      ✅ TẢI THÀNH CÔNG! ({size_mb:.2f} MB) -> {filename}")
                results.append({
                    "title": title,
                    "first_author": first_author,
                    "year": year,
                    "journal": journal,
                    "citations": cites,
                    "doi": doi,
                    "status": "DOWNLOADED_SUCCESS",
                    "filename": filename,
                    "size_mb": round(size_mb, 2),
                    "url": pdf_url
                })
            else:
                print(f"      ⚠️ Không thể tải trực tiếp ({msg}). Cần truy cập thư viện trường.")
                results.append({
                    "title": title,
                    "first_author": first_author,
                    "year": year,
                    "journal": journal,
                    "citations": cites,
                    "doi": doi,
                    "status": "PAYWALL_OR_GATEWAY",
                    "filename": None,
                    "size_mb": 0,
                    "url": pdf_url
                })
        else:
            print(f"      🔴 Bài báo sau tường phí (Paywall Closed) - Có thể mở bằng DOI.")
            results.append({
                "title": title,
                "first_author": first_author,
                "year": year,
                "journal": journal,
                "citations": cites,
                "doi": doi,
                "status": "PAYWALL_CLOSED",
                "filename": None,
                "size_mb": 0,
                "url": f"https://doi.org/{doi}"
            })
            
    # Xuất báo cáo Markdown
    report_path = os.path.join(WORKSPACE_DIR, "lab_projects", "VOSVIEWER_FULLTEXT_REPORT.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# BÁO CÁO KIỂM KÊ BÀI BÁO TOÀN VĂN MẠNG LƯỚI VOSVIEWER\n")
        f.write(f"## H-AI ResearchLAB | Thư mục: `lab_projects/fulltext_papers/vosviewer_core/`\n\n")
        f.write(f"- **Tập dữ liệu nguồn:** `data/processed/dimensions_clean_included.csv` (1,441 bài báo chuẩn PRISMA 2020)\n")
        f.write(f"- **Thời gian quét:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        f.write(f"- **Top bài báo hạt nhân đã quét:** {len(selected_papers)} bài\n")
        f.write(f"- **Số bài báo tải thành công PDF toàn văn về máy:** {success_count}/{len(selected_papers)} bài ({success_count/len(selected_papers)*100:.1f}%)\n\n")
        f.write("---\n\n")
        f.write("### DANH MỤC TOP BÀI BÁO HẠT NHÂN VOSVIEWER VÀ TÌNH TRẠNG TOÀN VĂN:\n\n")
        f.write("| TT | Năm | Tác giả & Tạp chí | Tiêu đề công trình | Trích dẫn | Tình trạng Full Text | File PDF / Link Truy Cập |\n")
        f.write("| :---: | :---: | :--- | :--- | :---: | :---: | :--- |\n")
        
        for idx, r in enumerate(results):
            if r["status"] == "DOWNLOADED_SUCCESS":
                status_badge = "🟢 **ĐÃ CÓ FILE PDF**"
                file_link = f"[`{r['filename']}`](file:///d:/SE_Project/khoahoc/lab_projects/fulltext_papers/vosviewer_core/{r['filename']}) ({r['size_mb']} MB)"
            elif r["status"] == "PAYWALL_OR_GATEWAY":
                status_badge = "🟡 Link Cổng Nhà Xuất Bản"
                file_link = f"[Mở Link Nhà XB]({r['url']})"
            else:
                status_badge = "🔴 Paywall (Thu phí)"
                file_link = f"[`https://doi.org/{r['doi']}`](https://doi.org/{r['doi']})"
                
            f.write(f"| {idx+1} | {r['year']} | **{r['first_author']} et al.**<br>*{r['journal'][:25]}* | {r['title'][:70]}... | {r['citations']:,} | {status_badge} | {file_link} |\n")
            
    print("\n" + "=" * 85)
    print(f"🎉 HOÀN THÀNH QUY TRÌNH THU THẬP BÀI BÁO TOÀN VĂN CHO VOSVIEWER!")
    print(f"1. Số bài PDF toàn văn đã tải về máy: {success_count} bài.")
    print(f"2. Thư mục chứa: lab_projects/fulltext_papers/vosviewer_core/")
    print(f"3. Báo cáo kiểm kê: lab_projects/VOSVIEWER_FULLTEXT_REPORT.md")
    print("=" * 85)

if __name__ == "__main__":
    n = 20
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
        except ValueError:
            pass
    run_vosviewer_pdf_harvest(n)
