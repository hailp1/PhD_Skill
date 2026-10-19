# QUY TRÌNH TỔNG QUAN TÀI LIỆU HỆ THỐNG THEO CHUẨN PRISMA 2020
*(Preferred Reporting Items for Systematic Reviews and Meta-Analyses)*

---

## 1. SƠ ĐỒ DÒNG CHẢY PRISMA 2020 (PRISMA FLOW DIAGRAM)

```mermaid
graph TD
    subgraph Identification ["1. Giai đoạn Xác định (Identification)"]
        A1["Tìm kiếm từ các cơ sở dữ liệu học thuật<br/>(Scopus: n = ...<br/>Web of Science: n = ...<br/>ScienceDirect / Emerald / Wiley: n = ...)"]
        A2["Các nguồn bổ sung khác<br/>(Google Scholar, ResearchGate, snowballing: n = ...)"]
        A3["Tổng số bài thu thập ban đầu<br/>(n = ...)"]
        A4["Loại bỏ các bài trùng lặp (Duplicates removed)<br/>(n = ...)"]
        A1 --> A3
        A2 --> A3
        A3 --> A4
    end

    subgraph Screening ["2. Giai đoạn Sàng lọc (Screening)"]
        B1["Tổng số bài tiến hành sàng lọc Tiêu đề & Tóm tắt<br/>(Records screened: n = ...)"]
        B2["Các bài bị loại bỏ sau khi đọc Title/Abstract<br/>(Records excluded: n = ...)<br/>- Không đúng phạm vi marketing/kinh doanh<br/>- Không phải bài nghiên cứu có bình duyệt"]
        A4 --> B1
        B1 --> B2
        B1 --> C1
    end

    subgraph Eligibility ["3. Giai đoạn Đánh giá Đủ điều kiện (Eligibility)"]
        C1["Số bài đọc toàn văn (Full-text assessed for eligibility)<br/>(n = ...)"]
        C2["Số bài toàn văn bị loại bỏ (Full-text excluded with reasons)<br/>(n = ...):<br/>- Lý do 1: Thiếu mô hình/dữ liệu thực nghiệm (n = ...)<br/>- Lý do 2: Không đo lường biến cốt lõi (n = ...)<br/>- Lý do 3: Bối cảnh không phù hợp (n = ...)"]
        C1 --> C2
        C1 --> D1
    end

    subgraph Included ["4. Giai đoạn Đưa vào Luận án (Included)"]
        D1["Số bài báo cuối cùng được đưa vào Tổng quan & Phân tích ma trận<br/>(Final included studies: n = ...)"]
    end
```

---

## 2. BẢNG TIÊU CHÍ LỰA CHỌN VÀ LOẠI TRỪ (ELIGIBILITY CRITERIA)

| Tiêu chí (Criterion) | Tiêu chuẩn Lựa chọn (Inclusion Criteria) | Tiêu chuẩn Loại trừ (Exclusion Criteria) |
| :--- | :--- | :--- |
| **Loại tài liệu** | Bài báo nghiên cứu gốc (Original empirical articles), Tổng quan hệ thống (Systematic reviews) trên tạp chí có phản biện khoa học (Peer-reviewed journals). | Kỷ yếu hội thảo tóm tắt, sách, bình luận xã luận (Editorials), luận văn chưa công bố, báo cáo kỹ thuật. |
| **Xếp hạng tạp chí** | Tạp chí thuộc Scopus (Q1/Q2/Q3), Web of Science (SSCI/ESCI), hoặc danh mục ABS/AJG (2, 3, 4, 4*), ABDC (B, A, A*). | Tạp chí kém chất lượng (Predatory journals), tạp chí không có chỉ số trích dẫn. |
| **Khung thời gian** | 5 - 10 năm gần nhất (ví dụ: 2015 - 2026), cộng với các công trình kinh điển đặt nền móng. | Các bài quá cũ không còn phù hợp với bối cảnh kinh tế số/công nghệ mới (trừ các bài lý thuyết nền). |
| **Ngôn ngữ** | Tiếng Anh và Tiếng Việt. | Các ngôn ngữ khác không thể dịch hoặc thẩm định độ tin cậy. |
| **Nội dung chủ đề** | Nghiên cứu tập trung vào mối quan hệ giữa các biến số về hành vi người tiêu dùng, marketing, chuyển đổi số, năng lực doanh nghiệp. | Các bài thuần túy về thuật toán tin học, kỹ thuật phần cứng, không chứa các biến số hành vi/quản trị. |
