# H-AI ResearchLAB CHARTER & OPERATIONAL PROTOCOL
*(Điều Lệ Hoạt Động & Quy Chuẩn Xuất Bản Quốc Tế Của Phòng Thí Nghiệm H-AI)*

---

## 1. TÔN CHỈ VÀ ĐỊNH VỊ HỌC THUẬT
**H-AI ResearchLAB (Business Administration & Marketing AI Research Laboratory)** là mô hình phòng thí nghiệm nghiên cứu khoa học tiên phong, kết hợp giữa năng lực tư duy chiến lược của **Nghiên cứu sinh Tiến sĩ (Lab Director)** và sức mạnh xử lý chuyên sâu của **Đội ngũ 6 AI Agents Học thuật**.

### Mục tiêu Chiến lược
1. **Nghiên cứu Luận án Tiến sĩ**: Đạt chuẩn xuất sắc, bảo vệ thành công tại Hội đồng Quốc gia/Quốc tế.
2. **Chiến lược Xuất bản Quốc tế**: Công bố tối thiểu **3 đến 4 bài báo Scopus Q1, Web of Science (WoS), xếp hạng ABS/AJG 3-4\*** trên các tạp chí hàng đầu:
   - *Journal of Retailing and Consumer Services* (Scopus Q1, IF: 11.0, CiteScore: 19.5).
   - *Journal of Business Research* (Scopus Q1, ABS 3*, IF: 10.5).
   - *Information & Management* (Scopus Q1, ABS 3*, IF: 8.2).
   - *Computers in Human Behavior* (Scopus Q1, ABS 3*, IF: 9.0).
   - *International Journal of Information Management* (Scopus Q1, ABS 3*, IF: 18.0).

---

## 2. NGUYÊN TẮC VÀ RÀNG BUỘC LIÊM CHÍNH (THE 5 IRON RULES)

### Điều 1: Ràng Buộc Liêm Chính Trích Dẫn Tuyệt Đối (Zero Fake Citations)
- Mọi tài liệu tham khảo được sử dụng trong bất kỳ bản thảo nào của Lab bắt buộc phải là công trình khoa học có thật 100%, đã công bố chính thức và có thể tra cứu qua Crossref / Scopus / WoS / OpenAlex.
- CẤM TUYỆT ĐỐI các trích dẫn ma (ghost/hallucinated citations). Trước khi nghiệm thu một chương hoặc bài báo, Agent 2 (SLR) bắt buộc phải chạy qua công cụ kiểm chứng `citation_verifier.py`.

### Điều 2: Kiểm Soát Đạo Văn & Độc Lập Học Thuật (Zero Verbatim Copying)
- Tuyệt đối không sao chép nguyên văn từ bất kỳ nguồn nào trừ các câu trích dẫn có trích dẫn số trang rõ ràng.
- Toàn bộ các định nghĩa và lập luận phải được tổng hợp qua kỹ thuật Ma trận Tổng hợp (Matrix Synthesis) và diễn đạt lại (Paraphrasing) bậc cao.
- Giữ tỷ lệ trùng lặp Turnitin / iThenticate dưới 15% tổng thể và dưới 1% cho mỗi nguồn đơn lẻ.

### Điều 3: Xóa Bỏ Hoàn Toàn Dấu Ấn Văn Phong AI (Zero-AI Clichés & Hedging)
- CẤM các từ ngữ sáo rỗng AI và văn phong dịch máy gượng gạo: *delve into, tapestry, testament to, beacon of, game-changer, revolutionary, bức tranh toàn cảnh, minh chứng hùng hồn, chiếc chìa khóa vạn năng, chiếc cầu nối vững chắc...*
- BẮT BUỘC sử dụng kỹ thuật khiêm tốn khoa học (Academic Hedging): *kết quả bước đầu gợi mở, cung cấp bằng chứng thực nghiệm ủng hộ, trong giới hạn phạm vi mẫu khảo sát*.
- Đảm bảo Tỷ lệ Trích dẫn Tự sự (Narrative Citation Ratio) đạt $\ge 30\%$.

### Điều 4: Chuẩn Mực Thuật Ngữ Song Ngữ (Bilingual Terminology Protocol)
- Áp dụng nguyên tắc xuất hiện lần đầu: `Thuật ngữ tiếng Việt (Thuật ngữ tiếng Anh - Ký hiệu viết tắt)`.
- Không lặp lại phần đối chiếu tiếng Anh ở các lần xuất hiện tiếp theo trong cùng một chương/bài báo.

### Điều 5: Kiểm Thử Phản Biện Độc Lập Trước Khi Xuất Bản (Internal Mock Review Gate)
- Không có bất kỳ bản thảo nào được gửi đi nộp tạp chí quốc tế mà chưa trải qua quy trình phản biện mô phỏng 5 ghế của Agent 6 (Mock Review Panel).
- Mọi ý kiến phản biện (Major Revision) đều phải được giải quyết thấu đáo và lập Thư giải trình (Rebuttal Letter) chi tiết.

---

## 3. DANH MỤC 4 BÀI BÁO CHIẾN LƯỢC TRONG HỆ THỐNG PIPELINE CỦA LAB

```
[H-AI LAB PIPELINE]
├── Paper 1: Systematic Literature Review & Bibliometric Mapping (VOSviewer + PRISMA 2020)
│   └── Mục tiêu: Journal of Retailing and Consumer Services (Scopus Q1)
├── Paper 2: Serial Mediation PLS-SEM Model of Personalized Recommendation Agents
│   └── Mục tiêu: Computers in Human Behavior / Electronic Commerce Research and Applications (Scopus Q1)
├── Paper 3: Moderating Boundary of Ego Depletion & Self-Control Capacity
│   └── Mục tiêu: Journal of Business Research (Scopus Q1, ABS 3*)
└── Paper 4: Asymmetric Combinational Configurations (fsQCA & NCA Methodology)
    └── Mục tiêu: Information & Management (Scopus Q1, ABS 3*)
```

---

## 4. QUY TRÌNH PHỐI HỢP LIÊN TÁC TỬ (INTER-AGENT WORKFLOW)
1. **Giai đoạn 1 (Đề cương & Y văn)**: Agent 1 (CRS) thiết kế mô hình -> Agent 2 (SLR) rà soát PRISMA 2020 và kiểm chứng trích dẫn.
2. **Giai đoạn 2 (Phương pháp & Thang đo)**: Agent 3 (MSA) chuẩn hóa thang đo song ngữ, kiểm soát CMB, thẩm định CVI.
3. **Giai đoạn 3 (Xử lý Số liệu)**: Agent 4 (EDS) chạy mã Python/SmartPLS kiểm định đo lường, cấu trúc và bootstrapping.
4. **Giai đoạn 4 (Soạn thảo Bản thảo)**: Agent 5 (LPA) viết bài báo IMRAD, audit văn phong và triệt tiêu mùi AI.
5. **Giai đoạn 5 (Phản biện & Hoàn thiện)**: Agent 6 (MJR) phản biện 5 ghế, stress-test lỗ hổng, duyệt điều kiện xuất bản cùng Lab Director.
