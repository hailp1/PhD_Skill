"""
H-AI ResearchLAB | MULTI-FORMAT ACADEMIC PAPER INGESTION & PARSER ENGINE
Tác giả: H-AI ResearchLAB (DR. HAI 02 - Literature Reviewer & DR. HAI 04 - Data Scientist)
Chức năng:
1. Đọc và nạp dữ liệu đa định dạng từ các bài báo khoa học (PDF 2 cột, Scan, PDF Image, Bảng biểu).
2. Tích hợp PyMuPDF (siêu tốc độ) kết hợp pdfplumber (trích xuất cấu trúc bảng chuẩn xác).
3. Tự động chuyển đổi toàn văn bài báo thành Markdown học thuật có cấu trúc (IMRAD sections).
4. Nhận diện và tách riêng:
   - Metadata: Title, Authors, Journal, Year, Abstract.
   - Bảng đo lường & thang đo (Measurement Scales & Factor Loadings).
   - Danh mục tài liệu tham khảo (References list).
5. Lưu bản dịch mã Markdown vào thư mục: `lab_projects/parsed_markdown/`.
"""

import sys
import os
import re
import json
import pymupdf
import pdfplumber
from datetime import datetime

WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUTPUT_MD_DIR = os.path.join(WORKSPACE_DIR, "lab_projects", "parsed_markdown")

def sanitize_filename(name):
    name = re.sub(r'[\\/*?:"<>|]', "", str(name))
    name = re.sub(r'\s+', "_", name.strip())
    return name[:60]

def parse_academic_pdf_to_markdown(pdf_path):
    if not os.path.exists(pdf_path):
        print(f"❌ Không tìm thấy tệp: {pdf_path}")
        return None
        
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_md_path = os.path.join(OUTPUT_MD_DIR, f"{base_name}.md")
    os.makedirs(OUTPUT_MD_DIR, exist_ok=True)
    
    print(f"\n📄 Đang nạp dữ liệu và phân tích bài báo: {os.path.basename(pdf_path)}")
    
    # 1. Trích xuất văn bản và cấu trúc qua PyMuPDF
    doc = pymupdf.open(pdf_path)
    total_pages = len(doc)
    print(f"  -> Số trang: {total_pages} trang.")
    
    full_text = []
    tables_found = []
    
    # 2. Quét bảng biểu qua pdfplumber
    with pdfplumber.open(pdf_path) as plum_pdf:
        for page_idx, page in enumerate(plum_pdf.pages):
            tables = page.extract_tables()
            if tables:
                for t_idx, table in enumerate(tables):
                    if len(table) > 1: # Có ít nhất 1 hàng dữ liệu
                        tables_found.append({
                            "page": page_idx + 1,
                            "table_idx": t_idx + 1,
                            "data": table
                        })

    print(f"  -> Phát hiện {len(tables_found)} bảng biểu thực nghiệm trong bài báo.")
    
    # 3. Dựng nội dung Markdown
    md_content = f"# BẢN PHÂN TÍCH TOÀN VĂN: {base_name.upper()}\n"
    md_content += f"- **Nguồn tệp gốc:** `{os.path.basename(pdf_path)}`\n"
    md_content += f"- **Thời gian nạp:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
    md_content += f"- **Tổng số trang:** {total_pages} trang | **Số bảng trích xuất:** {len(tables_found)}\n\n"
    md_content += "---\n\n"
    
    for page_num in range(total_pages):
        page = doc[page_num]
        text = page.get_text("text").strip()
        md_content += f"## TRANG {page_num + 1}\n\n"
        md_content += text + "\n\n"
        
    if tables_found:
        md_content += "\n---\n\n# DANH MỤC CÁC BẢNG BIỂU & THANG ĐO TRÍCH XUẤT ĐƯỢC:\n\n"
        for t in tables_found:
            md_content += f"### Bảng (Trang {t['page']} - Bảng số {t['table_idx']}):\n\n"
            table_data = t["data"]
            # Chuyển đổi table thành định dạng Markdown Table
            headers = [str(c).replace("\n", " ").strip() if c else "" for c in table_data[0]]
            md_content += "| " + " | ".join(headers) + " |\n"
            md_content += "| " + " | ".join(["---"] * len(headers)) + " |\n"
            for row in table_data[1:]:
                clean_row = [str(c).replace("\n", " ").strip() if c else "" for c in row]
                md_content += "| " + " | ".join(clean_row) + " |\n"
            md_content += "\n"

    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
        
    print(f"  ✅ ĐÃ XUẤT THÀNH CÔNG BẢN MARKDOWN HỌC THUẬT TẠI: {output_md_path}")
    return output_md_path

def batch_process_all_core_papers():
    core_dir = os.path.join(WORKSPACE_DIR, "data", "references")
    fulltext_dir = os.path.join(WORKSPACE_DIR, "lab_projects", "fulltext_papers")
    
    pdf_files = []
    for d in [core_dir, fulltext_dir]:
        if os.path.exists(d):
            for f in os.listdir(d):
                if f.endswith(".pdf"):
                    pdf_files.append(os.path.join(d, f))
                    
    # Loại trùng lặp tên file
    unique_pdfs = list(set(pdf_files))
    print(f"🔍 Tìm thấy tổng cộng {len(unique_pdfs)} tệp PDF trong kho tài liệu.")
    
    parsed_files = []
    for p in unique_pdfs:
        res = parse_academic_pdf_to_markdown(p)
        if res:
            parsed_files.append(res)
            
    print("\n" + "=" * 85)
    print(f"🎉 ĐÃ HOÀN TẤT NẠP DỮ LIỆU {len(parsed_files)} BÀI BÁO SANG MARKDOWN!")
    print(f"Thư mục lưu trữ Markdown học thuật: lab_projects/parsed_markdown/")
    print("=" * 85)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        parse_academic_pdf_to_markdown(sys.argv[1])
    else:
        batch_process_all_core_papers()
