# DIMENSIONS RAW EXPORT LOG & REPRODUCIBILITY NOTE
*(Nhật ký Xuất dữ liệu Thô từ Dimensions & Hướng dẫn Tái lập Nghiên cứu)*

---

## 1. Thông tin File Dữ liệu Gốc (Source Metadata)
- **Tên file gốc:** `Dimensions-Publication-2026-11-28_08-04-54.csv` *(gốc tại thư mục dự án)* và `Dimensions-Publication-2026-11-28_08-12-01.csv` *(bản xuất đầy đủ trường thư mục VOSviewer)*.
- **File chuẩn hóa lưu trữ trong Pipeline:** [dimensions_raw_export.csv](file:///d:/SE_Project/khoahoc/data/raw/dimensions_raw_export.csv) (sao chép nguyên vẹn từ `Dimensions-Publication-2026-11-28_08-12-01.csv`).
- **Cơ sở dữ liệu:** Dimensions (`https://app.dimensions.ai`), Digital Science & Research Solutions Inc.
- **Ngày xuất (Export Date):** `2026-11-28` (`08:12:01 UTC+7` / `Nov 28, 2026`).
- **Tổng số bản ghi thô (Raw Records):** `2,500` bản ghi (trần xuất 2,500 dòng/lần ở chế độ Bibliometric / VOSviewer Export).
- **Định dạng xuất (Export Format):** Full Bibliometric / VOSviewer CSV (`skiprows=1`, dòng 1 chứa metadata/disclaimer của Dimensions).
- **Các cột dữ liệu (15 trường):**
  `Publication ID`, `DOI`, `Title`, `Abstract`, `Source title/Anthology title`, `PubYear`, `Volume`, `Issue`, `Pagination`, `Authors`, `Authors Affiliations - Name of Research organization`, `Authors Affiliations - Country of Research organization`, `Dimensions URL`, `Times cited`, `Cited references`.

---

## 2. Chuỗi Tìm Kiếm Trung Lập Đã Sử Dụng (Agnostic Boolean Query)
Truy vấn được thiết kế theo cấu trúc **3 khối độc lập** (không chứa tên lý thuyết *S-O-R* hay biến trung gian *e-satisfaction* để tránh Confirmation Bias), tìm trên trường `full data`:

```text
("artificial intelligence" OR "AI" OR "recommendation system*" OR "recommender system*" OR "algorithmic recommendation*" OR "personalized recommendation*" OR "deep learning recommendation*" OR "collaborative filtering")
AND
("impulse buying" OR "impulsive buying" OR "impulse purchase*" OR "spontaneous purchase*" OR "unplanned purchase*" OR "urge to buy impulsively")
AND
("e-commerce" OR "online shopping" OR "digital retailing" OR "electronic commerce" OR "social commerce" OR "mobile commerce")
```

---

## 3. Hướng dẫn Tải lại từ Dimensions (Reproducibility Steps)
1. Truy cập `https://app.dimensions.ai` (mục **Publications**).
2. Dán nguyên văn chuỗi Boolean 3 khối ở Mục 2 vào ô tìm kiếm (`Full data` hoặc `Title and Abstract` nếu muốn thu hẹp từ nguồn).
3. Tại mục **Export** (góc trên bên phải), chọn **Export for bibliometric mapping** (hoặc **Export full record** định dạng CSV) để lấy đủ 15 cột gồm `DOI`, `Title`, `Abstract`, `Times cited`, `Cited references`.
4. Lưu file tải về vào `data/raw/dimensions_raw_export.csv` (giữ nguyên dòng 1 disclaimer của Dimensions để bảo đảm tính xác thực nguồn).

---

## 4. Lệnh Chạy Lại Toàn Bộ Phân Tích & Cập Nhật Bài Báo
Chạy lần lượt các lệnh sau tại thư mục gốc `d:\SE_Project\khoahoc`:

```powershell
# 1. Chạy lại phễu PRISMA 2020, VOSviewer Co-occurrence, Regex Appendix A và cập nhật dữ liệu sạch
python lab_management/run_full_slr_from_dimensions.py

# 2. Chạy kiểm toán chất lượng (QA Gate 100/100), kiểm duyệt văn phong (Tone 100/100) và đóng gói DOCS_INLINE.js
python lab_management/PIPELINE_ORCHESTRATOR.py --run-all
```

### Các tệp đầu ra tự động sinh từ `dimensions_raw_export.csv`:
- [paper1a_osf_screening_log.csv](file:///d:/SE_Project/khoahoc/lab_projects/paper1a_osf_screening_log.csv): Nhật ký sàng lọc đầy đủ `2,500` dòng (kèm mã quyết định `INCLUDE` / `EXCLUDE_*`).
- [dimensions_clean_included.csv](file:///d:/SE_Project/khoahoc/data/processed/dimensions_clean_included.csv): Tập bài báo tạp chí bình duyệt đạt chuẩn `2018–2026`.
- [paper1a_real_stats.json](file:///d:/SE_Project/khoahoc/lab_management/paper1a_real_stats.json): Toàn bộ thống kê PRISMA, Trajectory, Top 10 Journals, Top 10 Cited, VOSviewer Clusters và Regex counts.
- [figure3_vosviewer_real_network.png](file:///d:/SE_Project/khoahoc/lab_projects/figures/figure3_vosviewer_real_network.png): Biểu đồ mạng lưới đồng xuất hiện từ khóa VOSviewer dựng trực tiếp từ tập `INCLUDE`.
