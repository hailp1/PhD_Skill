# PhD Research Skill Suite: Marketing & Business Administration
*(Bộ Kỹ Năng Nghiên Cứu Luận Án Tiến Sĩ: Chuyên Ngành Marketing & Quản Trị Kinh Doanh)*

Hệ thống kỹ năng học thuật hỗ trợ toàn diện lộ trình nghiên cứu tiến sĩ từ lúc xây dựng Đề cương (Research Proposal), Tổng quan tài liệu (PRISMA SLR), Thiết kế thang đo & phương pháp (Methodology), Phân tích dữ liệu mô hình cấu trúc SEM (PLS-SEM / CB-SEM) đến Viết luận án 5 chương và công bố bài báo quốc tế (Scopus Q1/Q2, ABS/AJG 3-4*).

Đặc biệt, hệ thống tích hợp **Quy chuẩn Triệt tiêu Văn phong AI & Thực hành Khiêm tốn Học thuật (Anti-AI & Academic Hedging)** nhằm đảm bảo tính liêm chính và sự điềm đạm của một nhà nghiên cứu khoa học chân chính.

---

## 📁 Cấu Trúc Hệ Thống Kỹ Năng (`.agents/skills/`)

```text
.agents/skills/
├── phd-research-proposal/           # Giai đoạn 1: Xây dựng Đề cương nghiên cứu
│   ├── SKILL.md
│   ├── resources/proposal_template.md
│   └── references/theories_in_marketing.md
│
├── phd-literature-review/            # Giai đoạn 2: Tổng quan tài liệu có hệ thống (SLR)
│   ├── SKILL.md
│   ├── resources/prisma_flow_template.md
│   ├── resources/literature_matrix_template.md
│   └── references/scopus_wos_search_guide.md
│
├── phd-methodology-design/          # Giai đoạn 3: Phương pháp luận & Thang đo
│   ├── SKILL.md
│   ├── resources/scale_development_protocol.md
│   ├── resources/sample_size_guidelines.md
│   └── resources/survey_questionnaire_template.md
│
├── phd-data-analysis/               # Giai đoạn 4: Phân tích dữ liệu & Mô hình SEM
│   ├── SKILL.md
│   ├── scripts/research_data_toolkit.py
│   └── references/sem_analysis_guide.md
│
└── phd-dissertation-writing/        # Giai đoạn 5: Viết luận án & Bài báo Scopus
    ├── SKILL.md
    ├── scripts/academic_tone_audit.py
    ├── resources/dissertation_structure_template.md
    ├── resources/academic_phrasebank_marketing.md
    ├── references/anti_ai_academic_hedging_guide.md
    └── references/journal_publication_strategy.md
```

---

## 🚀 Chi Tiết 5 Kỹ Năng Chuyên Sâu

### 1. `phd-research-proposal`
- **Xác định 4 khoảng trống nghiên cứu (Research Gaps)**: Theoretical gap, Empirical gap, Contextual gap, Methodological gap.
- **Hệ thống lý thuyết nền (Grounding Theories)**: S-O-R, TAM/UTAUT, TPB, Cognitive Appraisal, Flow Theory, RBV, Dynamic Capabilities, Service-Dominant Logic, Social Exchange Theory, Signaling Theory.
- **Xây dựng mô hình khái niệm & hệ thống giả thuyết** ($H_1, H_2...$).

### 2. `phd-literature-review`
- **Quy trình tổng quan hệ thống PRISMA 2020**: 4 giai đoạn sàng lọc minh bạch (Identification $\rightarrow$ Screening $\rightarrow$ Eligibility $\rightarrow$ Included).
- **Ma trận tổng hợp tài liệu (Literature Synthesis Matrix)**: Chuẩn hóa trích xuất dữ liệu bài báo.
- **Chiến lược truy vấn Boolean**: Dành riêng cho Scopus và Web of Science Core Collection.

### 3. `phd-methodology-design`
- **Quy trình thích ứng thang đo (Scale Adaptation)**: Kế thừa thang đo chuẩn từ các tạp chí uy tín (*JM, JAMS, JCR, JBR, IJRM*), dịch ngược (Back-translation), phỏng vấn chuyên gia (Expert panel), và khảo sát thử nghiệm (Pilot study $N=50-100$).
- **Xác định cỡ mẫu tối thiểu**: Phân tích lực lượng thống kê G*Power ($1-\beta = 0.80 - 0.95$), quy tắc Hair et al. (2019) và tỷ lệ quan sát 5:1 đến 10:1.
- **Mẫu bảng câu hỏi khảo sát cấu trúc chuẩn Likert**.

### 4. `phd-data-analysis`
- **Công cụ tự động hóa Python**:
  ```bash
  # 1. Thống kê mô tả & Kiểm tra phân phối chuẩn Kline (2016)
  python .agents/skills/phd-data-analysis/scripts/research_data_toolkit.py --file data.csv --task descriptive

  # 2. Kiểm định sai lệch phương pháp chung (Harman's Single Factor test)
  python .agents/skills/phd-data-analysis/scripts/research_data_toolkit.py --file data.csv --task harman

  # 3. Tính độ tin cậy Cronbach's Alpha và tương quan biến - tổng
  python .agents/skills/phd-data-analysis/scripts/research_data_toolkit.py --file data.csv --task alpha --items PU1,PU2,PU3,PU4
  ```
- **Tiêu chuẩn đánh giá mô hình đo lường & cấu trúc SEM**: Hướng dẫn chi tiết PLS-SEM và CB-SEM (Outer loadings $\ge 0.708$, $\text{CR} \ge 0.70$, $\text{AVE} \ge 0.50$, $\text{HTMT} < 0.85/0.90$, Bootstrapping $5000-10000$ mẫu).

### 5. `phd-dissertation-writing`
- **Kết cấu chuẩn 5 chương của Luận án Tiến sĩ**.
- **Thảo luận kết quả học thuật (Academic Discussion)**: Đối thoại với các công trình trước đây thay vì chỉ đọc lại số liệu thống kê.
- **Ngân hàng mẫu câu học thuật song ngữ (Academic Phrasebank)**.
- **Chiến lược công bố Scopus Q1/Q2 từ Luận án**: Trích xuất thành 2–3 bài báo và kỹ thuật trả lời phản biện (Response to Reviewers).

---

## 🛡️ Bộ Quy Chuẩn Anti-AI & Khiêm Tốn Học Thuật (Academic Hedging)
- **Công cụ kiểm duyệt tự động**:
  ```bash
  python .agents/skills/phd-dissertation-writing/scripts/academic_tone_audit.py --file draft.md
  ```
- **Triệt tiêu các từ ngữ rập khuôn của AI**: *delve into, tapestry, testament to, beacon, game-changer, revolutionary, bức tranh toàn cảnh, chiếc chìa khóa vạn năng, minh chứng hùng hồn...*
- **Triệt tiêu các khẳng định "chém gió" tuyệt đối**: Chuyển đổi các câu thiếu căn cứ (*"chứng minh hoàn toàn 100%"*, *"giải quyết triệt để mọi vấn đề"*) sang ngôn từ thận trọng, điềm đạm (*"lends empirical support to"*, *"cung cấp bằng chứng bước đầu"*, *"trong phạm vi điều kiện biên của mẫu"*).
- **Loại bỏ các dấu hiệu nhận diện máy móc**: Giảm thiểu lạm dụng dấu gạch ngang dài (`—` em-dash), hạn chế liệt kê bullet point thay cho văn xuôi học thuật liên kết (cohesive paragraphs).

---

## 👤 Tác Giả & Bản Quyền
- Dự án: **PhD Research Skill Suite (Marketing & Business Administration)**
- Repository: [https://github.com/hailp1/PhD_Skill.git](https://github.com/hailp1/PhD_Skill.git)
