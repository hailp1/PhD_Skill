# PH.D. DISSERTATION RESEARCH REPOSITORY
*(Kho Lưu Trữ Nghiên Cứu Luận Án Tiến Sĩ: Chuyên Ngành Marketing & Quản Trị Kinh Doanh)*

**Đề tài**: Tác động của hệ thống đề xuất cá nhân hóa dựa trên AI đến hành vi mua bốc đồng của người tiêu dùng trực tuyến: Vai trò trung gian của sự hài lòng trực tuyến  
**NCS**: Lê Phúc Hải | **Cơ sở đào tạo**: Trường Đại học Tôn Đức Thắng (TDTU)  
**Tiêu chuẩn hướng tới**: Scopus Q1 (ABS/AJG 3-4*), PRISMA 2020 Statement, và Trắc lượng thư mục VOSviewer  

---

## 🏛️ CẤU TRÚC THƯ MỤC CHUẨN QUỐC TẾ (REPOSITORY ARCHITECTURE)

Kho lưu trữ được tổ chức theo tiêu chuẩn mở OSF (Open Science Framework) và cấu trúc quản lý luận án tiến sĩ quốc tế:

```text
khoahoc/
├── docs/                                # Hồ sơ học thuật và tài liệu đề cương (Documentation)
│   ├── proposal_detailed.md             # Đề cương chi tiết (Mô hình trung gian chuỗi có điều tiết)
│   ├── literature_matrix.md             # Ma trận tổng quan 8 bài Scopus Q1 xác thực mã DOI Crossref
│   ├── prisma_2020_protocol.md          # Giao thức tổng quan y văn hệ thống chuẩn PRISMA 2020
│   ├── guidelines_dissertation.md       # Cẩm nang hướng dẫn thực thi và chiến lược 02 bài báo quốc tế
│   ├── notes_advisor_consultation.md    # Biên bản tổng hợp ý kiến góp ý của GVHD
│   ├── notes_ferrentino_2018.md         # Ghi chú phân tích bài báo nền tảng Ferrentino (2018)
│   └── progress_tracker.xlsx            # Bảng theo dõi tiến độ tổng thể luận án & bài báo
│
├── data/                                # Quản lý dữ liệu thực nghiệm (Research Data)
│   ├── raw/                             # Dữ liệu xuất thô từ cơ sở dữ liệu quốc tế
│   │   └── dimensions_raw_export.csv    # 2,500 bài báo thô xuất từ Dimensions
│   ├── processed/                       # Dữ liệu sạch sau sàng lọc PRISMA 2020
│   │   ├── dimensions_clean_included.csv# 1,441 bài báo Scopus Q1/Q2 cốt lõi (100% có DOI)
│   │   └── prisma_2020_slide_report.md  # Thống kê chi tiết & kịch bản nói 2 phút cho Slide
│   ├── vosviewer/                       # Tệp tọa độ và ma trận liên kết nạp vào VOSviewer
│   │   ├── keywords_map.txt             # Tọa độ 2D, tần suất xuất hiện và phân cụm từ khóa
│   │   └── keywords_network.txt         # 309 cặp liên kết đồng xuất hiện thực chứng
│   └── references/                      # Kho lưu trữ tệp PDF bài báo gốc
│       └── ferrentino_2018.pdf          # Tệp toàn văn bài báo Ferrentino et al. (2018)
│
├── web/                                 # Giao diện trực quan hóa và Dashboard điều khiển (Web UI)
│   ├── index.html                       # 🌟 DASHBOARD TRUNG TÂM THỐNG NHẤT (SPA 4 Tabs)
│   ├── prisma_flowchart.html            # Sơ đồ dòng chảy PRISMA 2020 tương tác (có nút in PDF)
│   ├── conceptual_model.html            # Mô hình khái niệm tương tác SVG (Chế độ Màu & Đơn sắc APA 7th)
│   └── interactive_science_map.html     # Bản đồ mạng lưới tương tác 3 chế độ (Network/Overlay/Density)
│
├── .agents/skills/                      # Hệ sinh thái kỹ năng AI nội bộ (AI Advisory Suite)
│   ├── phd-research-proposal/           # Kỹ năng xây dựng đề cương & giả thuyết nghiên cứu
│   ├── phd-literature-review/           # Kỹ năng PRISMA 2020, VOSviewer & Thẩm định trích dẫn Crossref
│   ├── phd-methodology-design/          # Kỹ năng thiết kế phương pháp, cỡ mẫu & thang đo dịch ngược
│   ├── phd-data-analysis/               # Kỹ năng phân tích PLS-SEM, CB-SEM & Kiểm soát CMB
│   └── phd-dissertation-writing/        # Kỹ năng viết 5 chương, thảo luận kết quả & tone audit v2.0
│
├── start_vosviewer_desktop.bat          # Kích hoạt 1-chạm VOSviewer Desktop (Đã nhúng Java 21)
├── start_vosviewer_online.bat           # Kích hoạt 1-chạm VOSviewer Online (Port 8600)
├── .gitignore                           # Danh mục loại trừ tệp tạm và dữ liệu lớn
├── GEMINI.md                            # Bộ quy chuẩn cố vấn học thuật độc quyền
├── LICENSE                              # Bản quyền mã nguồn mở MIT
└── README.md                            # Hướng dẫn tổng quan kho lưu trữ
```

---

## 🚀 HƯỚNG DẪN KHỞI ĐỘNG VÀ TRẢI NGHIỆM HỆ THỐNG

### 1. Trải nghiệm Dashboard Nghiên Cứu Thống Nhất (Tất cả trong một)
Bạn chỉ cần mở tệp:  
👉 **[web/index.html](web/index.html)** trên trình duyệt.  
Hệ thống cho phép bạn chuyển đổi mượt mà giữa 4 Tab chính:
* **Tab 1: Lưu Đồ PRISMA 2020** (2,500 thô $\to$ 1,441 bài sạch, kèm nút xuất PDF cho Slide).
* **Tab 2: VOSviewer Online** (Khung hiển thị web chính thức của Leiden University nạp sẵn dữ liệu).
* **Tab 3: Mô Hình Khái Niệm** (Kiến trúc trung gian chuỗi có điều tiết chuẩn Scopus Q1).
* **Tab 4: Báo Cáo Slide** (Kịch bản thuyết trình 2 phút trước Hội đồng & Top 8 tạp chí Q1).

### 2. Khởi động VOSviewer Desktop (Đã tích hợp sẵn Java 21 không lỗi)
Nhấp đúp chuột vào tệp:  
👉 **[start_vosviewer_desktop.bat](start_vosviewer_desktop.bat)**  
Ứng dụng sẽ tự động khởi động và nạp sẵn toàn bộ bản đồ 1,441 bài báo với 3 chế độ xem (kể cả *Density Heatmap*).

### 3. Khởi động VOSviewer Online Local (Port 8600)
Nhấp đúp chuột vào tệp:  
👉 **[start_vosviewer_online.bat](start_vosviewer_online.bat)**  
Máy chủ nội bộ sẽ bật và mở trình duyệt tại `http://localhost:8600/?json=data/luan_an_real_network.json`.

---

## 📊 TỰ ĐỘNG HÓA QUY TRÌNH KHI CÓ DỮ LIỆU MỚI

Khi bạn tải thêm bất kỳ tệp dữ liệu thô nào từ Dimensions / Scopus bỏ vào thư mục `data/raw/`, chỉ cần chạy 01 lệnh terminal:

```bash
python .agents/skills/phd-literature-review/scripts/pipeline_prisma_vosviewer.py
```

Toàn bộ quá trình lọc 4 tầng PRISMA 2020, làm sạch dữ liệu, tính toán ma trận tương quan và cập nhật bản đồ VOSviewer sẽ được tự động hoàn tất trong vòng 10 giây!
