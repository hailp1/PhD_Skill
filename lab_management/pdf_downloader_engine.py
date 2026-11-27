"""
H-AI ResearchLAB | HIGH-THROUGHPUT FULL-TEXT PDF DOWNLOADER ENGINE
Tác giả: H-AI ResearchLAB (DR. HAI 02 - Literature Reviewer)
Chức năng:
1. Đọc kho dữ liệu bài báo từ `lab_projects/ACADEMIC_LITERATURE_MASTER_CORPUS.json`.
2. Truy vết các đường link Open Access PDF hợp pháp (Unpaywall, ScienceDirect OA, Springer OA, Wiley OA, PubMed Central, arXiv).
3. Tải hàng loạt file PDF toàn văn về thư mục `lab_projects/fulltext_papers/`.
4. Đặt tên file chuẩn mực học thuật: `[Năm]_[Tác giả chính]_[Tiêu đề rút gọn].pdf`.
5. Tạo báo cáo kiểm kê tải toàn văn `lab_projects/FULLTEXT_DOWNLOAD_REPORT.md`.
"""

import sys
import os
import json
import re
import urllib.parse
import urllib.request
from datetime import datetime

WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CORPUS_PATH = os.path.join(WORKSPACE_DIR, "lab_projects", "ACADEMIC_LITERATURE_MASTER_CORPUS.json")
PDF_DIR = os.path.join(WORKSPACE_DIR, "lab_projects", "fulltext_papers")

def sanitize_filename(name):
    # Xóa ký tự không hợp lệ cho tên file trên Windows
    name = re.sub(r'[\\/*?:"<>|]', "", name)
    name = re.sub(r'\s+', "_", name.strip())
    return name[:60]

def resolve_best_pdf_url(paper):
    """
    Tìm kiếm URL tải PDF tốt nhất:
    1. Ưu tiên open_access_pdf có sẵn trong bài.
    2. Nếu không có hoặc link dạng landing page, thử truy vấn Unpaywall API miễn phí.
    """
    oa_url = paper.get("open_access_pdf") or ""
    doi = paper.get("doi") or ""
    
    if oa_url and oa_url.endswith(".pdf"):
        return oa_url
        
    if "doi.org/" in doi:
        clean_doi = doi.split("doi.org/")[-1]
        unpaywall_url = f"https://api.unpaywall.org/v2/{clean_doi}?email=phd_candidate@h-ai-lab.edu.vn"
        try:
            req = urllib.request.Request(unpaywall_url, headers={"User-Agent": "H-AI-Lab/2.0"})
            with urllib.request.urlopen(req, timeout=5) as resp:
                if resp.status == 200:
                    data = json.loads(resp.read().decode('utf-8'))
                    best_oa = data.get("best_oa_location") or {}
                    pdf_link = best_oa.get("url_for_pdf") or best_oa.get("url")
                    if pdf_link:
                        return pdf_link
        except Exception:
            pass
            
    return oa_url

def download_pdf(url, output_path, timeout=20):
    """
    Tải file PDF với User-Agent mô phỏng trình duyệt và hỗ trợ bypass SSL cert thiếu của Windows.
    """
    import ssl
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # Nếu URL là arxiv dạng https://arxiv.org/pdf/xxxx.xxxx thì đảm bảo có .pdf
    if "arxiv.org/pdf/" in url and not url.endswith(".pdf"):
        url = url + ".pdf"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept": "application/pdf,application/octet-stream,*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://scholar.google.com/"
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=timeout) as response:
            content_type = response.headers.get("Content-Type", "")
            data = response.read()
            
            # Kiểm tra xem có đúng là file PDF không (bắt đầu bằng %PDF)
            if data.startswith(b"%PDF") or "pdf" in content_type.lower():
                with open(output_path, "wb") as f:
                    f.write(data)
                return True, len(data), "OK"
            else:
                return False, len(data), "HTML_LANDING_PAGE"
    except Exception as e:
        return False, 0, str(e)

def run_bulk_pdf_downloader(max_downloads=20):
    print("=" * 85)
    print("📥 H-AI ResearchLAB | HIGH-THROUGHPUT FULL-TEXT PDF DOWNLOADER ENGINE")
    print(f"Thư mục lưu trữ: lab_projects/fulltext_papers/")
    print("=" * 85)
    
    if not os.path.exists(PDF_DIR):
        os.makedirs(PDF_DIR, exist_ok=True)
        
    if not os.path.exists(CORPUS_PATH):
        print(f"❌ Không tìm thấy file kho dữ liệu tại: {CORPUS_PATH}")
        return
        
    with open(CORPUS_PATH, "r", encoding="utf-8") as f:
        corpus = json.load(f)
        
    papers = corpus.get("papers", [])
    total_papers = len(papers)
    print(f"\n[BƯỚC 1] Đọc được {total_papers} bài báo khoa học trong Master Corpus.")
    print(f"Đang tiến hành truy vết và tải toàn văn tối đa {max_downloads} bài...")
    
    results = []
    success_count = 0
    
    for i, p in enumerate(papers[:max_downloads]):
        year = str(p.get("year", "YYYY"))
        author = sanitize_filename(p.get("first_author", "Author").split()[-1])
        title = sanitize_filename(p.get("title", "Untitled"))
        filename = f"{year}_{author}_{title}.pdf"
        target_path = os.path.join(PDF_DIR, filename)
        
        print(f"\n[{i+1}/{min(total_papers, max_downloads)}] ({year}) {p.get('title')[:65]}...")
        pdf_url = resolve_best_pdf_url(p)
        
        if not pdf_url:
            print(f"  ⚠️ Bài báo thuộc diện Closed-Access (Paywall) - Không có link PDF mở hợp pháp.")
            results.append({
                "title": p.get("title"),
                "first_author": p.get("first_author"),
                "year": year,
                "journal": p.get("journal"),
                "doi": p.get("doi"),
                "status": "PAYWALL_CLOSED",
                "filename": None,
                "pdf_url": None
            })
            continue
            
        print(f"  🔗 Tìm thấy URL PDF: {pdf_url[:75]}...")
        success, size_bytes, msg = download_pdf(pdf_url, target_path)
        
        if success:
            success_count += 1
            size_mb = size_bytes / (1024 * 1024)
            print(f"  ✅ TẢI THÀNH CÔNG! Dung lượng: {size_mb:.2f} MB -> Lưu tại: {filename}")
            results.append({
                "title": p.get("title"),
                "first_author": p.get("first_author"),
                "year": year,
                "journal": p.get("journal"),
                "doi": p.get("doi"),
                "status": "DOWNLOADED_SUCCESS",
                "filename": filename,
                "size_mb": round(size_mb, 2),
                "pdf_url": pdf_url
            })
        else:
            print(f"  ⚠️ Không thể tải trực tiếp ({msg}). Cần truy cập qua tài khoản thư viện trường.")
            results.append({
                "title": p.get("title"),
                "first_author": p.get("first_author"),
                "year": year,
                "journal": p.get("journal"),
                "doi": p.get("doi"),
                "status": "LANDING_PAGE_OR_REDIRECT",
                "filename": None,
                "pdf_url": pdf_url
            })
            
    # Tạo báo cáo Markdown tổng kết
    report_path = os.path.join(WORKSPACE_DIR, "lab_projects", "FULLTEXT_DOWNLOAD_REPORT.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# BÁO CÁO KIỂM KÊ TOÀN VĂN BÀI BÁO (FULL-TEXT REPOSITORY REPORT)\n")
        f.write(f"## H-AI ResearchLAB | Thư mục: `lab_projects/fulltext_papers/`\n\n")
        f.write(f"- **Thời gian quét:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        f.write(f"- **Tổng số bài báo rà soát:** {min(total_papers, max_downloads)}\n")
        f.write(f"- **Số bài báo tải thành công PDF toàn văn:** {success_count} bài ({success_count/max(1, min(total_papers, max_downloads))*100:.1f}%)\n\n")
        f.write("---\n\n")
        f.write("### DANH MỤC CHI TIẾT BÀI BÁO VÀ TRẠNG THÁI TOÀN VĂN:\n\n")
        f.write("| TT | Năm | Tác giả & Tạp chí | Tiêu đề | Trạng thái Full Text | File PDF / DOI |\n")
        f.write("| :---: | :---: | :--- | :--- | :---: | :--- |\n")
        
        for idx, r in enumerate(results):
            if r["status"] == "DOWNLOADED_SUCCESS":
                status_badge = "🟢 **ĐÃ TẢI FULL PDF**"
                file_link = f"[`{r['filename']}`](file:///d:/SE_Project/khoahoc/lab_projects/fulltext_papers/{r['filename']}) ({r['size_mb']} MB)"
            elif r["status"] == "LANDING_PAGE_OR_REDIRECT":
                status_badge = "🟡 Link Cần Đăng Nhập"
                file_link = f"[Mở Link Trang Chủ]({r['pdf_url']})"
            else:
                status_badge = "🔴 Paywall (Thu phí)"
                file_link = f"[Mở DOI]({r['doi']})" if r.get('doi') else "N/A"
                
            f.write(f"| {idx+1} | {r['year']} | **{r['first_author']}**<br>*{r['journal'][:25]}* | {r['title'][:70]}... | {status_badge} | {file_link} |\n")
            
    print("\n" + "=" * 85)
    print(f"🎉 HOÀN THÀNH QUY TRÌNH TẢI BÀI BÁO TOÀN VĂN!")
    print(f"1. Tổng số bài tải thành công: {success_count}/{min(total_papers, max_downloads)} bài.")
    print(f"2. Thư mục chứa file PDF: lab_projects/fulltext_papers/")
    print(f"3. Báo cáo chi tiết: lab_projects/FULLTEXT_DOWNLOAD_REPORT.md")
    print("=" * 85)

def main():
    max_count = 15
    if len(sys.argv) > 1:
        try:
            max_count = int(sys.argv[1])
        except ValueError:
            pass
    run_bulk_pdf_downloader(max_count)

if __name__ == "__main__":
    main()
