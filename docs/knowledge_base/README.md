# HỆ THỐNG THƯ VIỆN TRI THỨC NGHIÊN CỨU LUẬN ÁN TIẾN SĨ
*(Doctoral Dissertation Knowledge Base - Marketing & Business Administration)*

---

## 1. MỤC ĐÍCH & KIẾN TRÚC KHO TRI THỨC

Thư viện tri thức được thiết lập nhằm lưu trữ, cấu trúc hóa và tổng hợp toàn bộ các phát hiện khoa học, trường phái lý thuyết, thang đo thực nghiệm và ngân hàng ý tưởng công bố quốc tế phục vụ NCS Lê Phúc Hải. Kho tri thức này đảm bảo **100% tuân thủ bản quyền** (không lưu trữ tệp PDF thô vi phạm bản quyền) nhưng **bảo tồn trọn vẹn 100% giá trị học thuật** cần thiết để viết Chương 2, Chương 3 và các bài báo Scopus Q1.

```
docs/knowledge_base/
├── README.md                                      <- Bảng chỉ mục và hướng dẫn khai thác
├── THEORETICAL_FRAMEWORKS.md                      <- Phân tích sâu 5 lý thuyết nền tảng (S-O-R, Ego Depletion, Dual-Process, Cognitive Fit, Information Foraging)
├── EMPIRICAL_EVIDENCE_BANK.md                     <- Ma trận bằng chứng thực nghiệm của 15 công trình đầu ngành (2018 - 2025)
├── VARIABLE_OPERATIONALIZATION_DICTIONARY.md      <- Từ điển thao tác hóa 8 cấu niệm & bộ thang đo song ngữ Anh - Việt
├── HYPOTHESIS_DEFENSE_COMPENDIUM.md               <- Hồ sơ biện chứng bảo vệ 9 giả thuyết & kịch bản đối thoại hội đồng
└── RESEARCH_IDEA_INCUBATOR.md                     <- Vườn ươm ý tưởng công bố 4 bài báo Scopus Q1 độc lập
```

---

## 2. CHỈ MỤC CÁC MÔ-ĐUN HỌC THUẬT

| Mô-đun | Tệp Lưu Trữ | Nội Dung Trọng Tâm | Ứng Dụng Trong Luận Án |
| :---: | :--- | :--- | :--- |
| **Mô-đun 1** | [THEORETICAL_FRAMEWORKS.md](file:///d:/SE_Project/khoahoc/docs/knowledge_base/THEORETICAL_FRAMEWORKS.md) | 5 Lý thuyết nền tảng, định nghĩa gốc, cơ chế vận hành trong kỷ nguyên AI. | Soạn thảo Mục 2.1 (Cơ sở lý thuyết) của Chương 2. |
| **Mô-đun 2** | [EMPIRICAL_EVIDENCE_BANK.md](file:///d:/SE_Project/khoahoc/docs/knowledge_base/EMPIRICAL_EVIDENCE_BANK.md) | Ngân hàng 15 bài báo Scopus Q1/Q2, hệ số $\beta$, giá trị $R^2$, phát hiện bất đồng y văn. | Soạn thảo Mục 2.2 (Tổng quan y văn thực nghiệm) của Chương 2. |
| **Mô-đun 3** | [VARIABLE_OPERATIONALIZATION_DICTIONARY.md](file:///d:/SE_Project/khoahoc/docs/knowledge_base/VARIABLE_OPERATIONALIZATION_DICTIONARY.md) | Thao tác hóa 8 biến số (PP, ACC, NOV, ESAT, UBI, OIB, SC, IBT), thang đo 7 điểm Likert song ngữ, chỉ số $\alpha, CR, AVE$. | Thiết kế Bảng câu hỏi khảo sát & Mục 3.2 (Thang đo) của Chương 3. |
| **Mô-đun 4** | [HYPOTHESIS_DEFENSE_COMPENDIUM.md](file:///d:/SE_Project/khoahoc/docs/knowledge_base/HYPOTHESIS_DEFENSE_COMPENDIUM.md) | Luận cứ logic biện chứng cho 9 giả thuyết ($H_1 - H_9$), phản biện hội đồng & câu trả lời đanh thép. | Soạn thảo Mục 2.3 (Phát triển giả thuyết) & Chuẩn bị bảo vệ trước Hội đồng. |
| **Mô-đun 5** | [RESEARCH_IDEA_INCUBATOR.md](file:///d:/SE_Project/khoahoc/docs/knowledge_base/RESEARCH_IDEA_INCUBATOR.md) | Thiết kế 4 bài báo Scopus Q1 (SLR/Bibliometrics, Serial Mediation, Self-Control Moderation, fsQCA/NCA). | Triển khai công bố quốc tế chuẩn đầu ra tiến sĩ. |

---

## 3. CÔNG CỤ TRUY VẤN TRI THỨC TỨC THỜI (KNOWLEDGE CLI)

Bạn có thể tìm kiếm nhanh mọi khái niệm, thang đo, hoặc trích dẫn từ kho tri thức bằng công cụ:
```powershell
python scratch/query_knowledge_base.py "Self-Control"
python scratch/query_knowledge_base.py "Novelty"
python scratch/query_knowledge_base.py "H9"
```
