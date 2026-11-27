# H-AI ResearchLAB: PUBLICATION & DISSERTATION ADVISORY PROTOCOL
*(Quy Trình Tư Vấn Xuất Bản Bài Báo Quốc Tế & Báo Cáo Tiến Độ Luận Án Tiến Sĩ)*

---

## 1. VỊ TRÍ CỦA PHÂN HỆ TƯ VẤN TRONG LUỒNG LAB (ADVISORY STREAM)
Phân hệ **Tư Vấn Bài Báo & Báo Cáo (Paper & Dissertation Advisory Stream)** là trục điều phối trung tâm kết nối giữa **Nghiên cứu sinh (Lab Director)** và **Đội ngũ 6 AI Agents**. 

Phân hệ này giải quyết 4 bài toán sống còn:
1. **Tư vấn Định vị Tạp chí (Journal Targeting & Aims & Scope Matching)**.
2. **Tư vấn Cấu trúc Bản thảo Chuẩn IMRAD & Đóng góp Lý thuyết (Manuscript Architecture & Theoretical Contributions)**.
3. **Tư vấn Phản biện Mô phỏng & Kỹ thuật Viết Thư Tiếp thu Giải trình (Pre-Submission Mock Review & Rebuttal Strategy)**.
4. **Tư vấn Soạn Báo cáo Tiến độ & Slide Thuyết trình Luận án Tiến sĩ (Progress Report & Defense Slide Advisory)**.

---

## 2. BỐN TRỤ CỘT TƯ VẤN CHUYÊN SÂU

```
[H-AI PUBLICATION ADVISORY SUITE]
├── Trụ Cột 1: Tư Vấn Khớp Tạp Chí & Khẩu Vị Tổng Biên Tập (Journal Scope Matcher)
│   ├── Journal of Retailing and Consumer Services (JRCS) -> Phù hợp Bài 1 (SLR/Biblio)
│   ├── Computers in Human Behavior (CHB) / ECRA -> Phù hợp Bài 2 (Serial Mediation)
│   ├── Journal of Business Research (JBR) -> Phù hợp Bài 3 (Ego Depletion Moderation)
│   └── Information & Management (I&M) -> Phù hợp Bài 4 (fsQCA & NCA)
│
├── Trụ Cột 2: Tư Vấn Cấu Trúc Thành Văn & Chuẩn Mực Scopus Q1
│   ├── 6 Bước Tu từ Học thuật (Hook, Tension, Gap, Deduction, Discussion, Contribution)
│   ├── Zero AI Clichés & Kỹ thuật Academic Hedging
│   └── Narrative Citation Ratio >= 30%
│
├── Trụ Cột 3: Tư Vấn Phản Biện & Rebuttal Letter (Hội đồng 5 Ghế - Agent 06)
│   ├── Đánh giá Desk-Reject rủi ro
│   ├── Soạn Thư Trả lời Phản biện (Point-by-point Response to Reviewers)
│   └── Kỹ thuật "Không tranh cãi cùn, nhã nhặn bổ sung thực nghiệm"
│
└── Trụ Cột 4: Tư Vấn Báo Cáo & Slide Luận Án Tiến Sĩ (Doctoral Defense Suite)
    ├── Báo cáo Tiến độ Định kỳ (Bi-annual Progress Report)
    ├── Slide Bảo vệ Đề cương (Proposal Defense Presentation)
    └── Slide Bảo vệ Luận án Chính thức (Final Defense Slides)
```

---

## 3. DANH MỤC CÁC CÔNG CỤ TƯ VẤN TÍCH HỢP TRONG WORKSPACE
1. **Cổng Điều Hành Trực Quan**: 
   - [TRUNG_TAM_DIEU_HANH_LAB.html](file:///d:/SE_Project/khoahoc/TRUNG_TAM_DIEU_HANH_LAB.html) (Mục "Trung Tâm Tư Vấn Xuất Bản & Báo Cáo Luận Án").
   - [index.html (Tab 6)](file:///d:/SE_Project/khoahoc/index.html) và [Tab 4 (Slide & Báo cáo)](file:///d:/SE_Project/khoahoc/index.html).
2. **Cẩm Nang Thành Văn & Mẫu Câu Q1**:
   - [ACADEMIC_WRITING_RHETORIC_GUIDE.md](file:///d:/SE_Project/khoahoc/docs/knowledge_base/ACADEMIC_WRITING_RHETORIC_GUIDE.md).
3. **Bộ Công Cụ Kiểm Toán Văn Phong Học Thuật**:
   - [academic_tone_audit.py](file:///d:/SE_Project/khoahoc/.agents/skills/phd-dissertation-writing/scripts/academic_tone_audit.py).
4. **Bộ Công Cụ Thẩm Định Liêm Chính Trích Dẫn**:
   - [citation_verifier.py](file:///d:/SE_Project/khoahoc/.agents/skills/phd-literature-review/scripts/citation_verifier.py).
5. **Kịch Bản Điều Phối Dòng Lệnh**:
   - `python lab_management/PIPELINE_ORCHESTRATOR.py --advise`
