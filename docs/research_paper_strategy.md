# CHIẾN LƯỢC XUẤT BẢN 4 BÀI BÁO SCOPUS Q1 TỪ DỮ LIỆU LUẬN ÁN TIẾN SĨ
*(Doctoral Publication Roadmap & Paper Ideation Reservoir - NCS Lê Phúc Hải, TDTU)*

---

## 1. TỔNG QUAN KIẾN TRÚC KHO DỮ LIỆU ĐÃ NẠP VÀO HỆ THỐNG

Dự án hiện đang sở hữu **3 tầng dữ liệu có cấu trúc hoàn chỉnh** để bạn khai thác ý tưởng viết bài báo khoa học:

1. **Kho Y văn Thực chứng 1,441 Bài báo Scopus Q1/Q2 (2018–2026)**:
   - Lưu trữ tại: `data/processed/dimensions_clean_included.csv`.
   - Chứa đầy đủ: Tiêu đề, Tóm tắt khoa học (Abstracts), Tên tác giả, Tạp chí, Năm, Mã DOI, Số lượt trích dẫn, và Danh mục tài liệu tham khảo.
   - **Công cụ truy vấn nhanh**: `.agents/skills/phd-literature-review/scripts/query_literature_corpus.py` (Cho phép gõ lệnh tìm kiếm bất kỳ cấu niệm, lý thuyết hoặc từ khóa nào để trích xuất bằng chứng tức thì).
2. **Ma trận Đồng xuất hiện Mạng lưới Khoa học (Bibliometric Science Mapping)**:
   - Lưu trữ tại: `data/vosviewer/luan_an_real_network.json`, `keywords_map.txt`, `keywords_network.txt`.
   - Gồm: 28 cấu niệm, 4 cụm chủ đề, 250 liên kết đồng xuất hiện thực tế (Fruchterman-Reingold layout).
3. **Hồ sơ Trích xuất Toàn văn Thang đo và Lý thuyết Nền (Literature Extraction Dossier)**:
   - Lưu trữ tại: `docs/literature_matrix.md` (Mục 4) và `data/references/INDEX_OF_KEY_PAPERS.md`.
   - Chứa nguyên văn thang đo (Items tiếng Anh + Việt) và giới hạn nghiên cứu (Limitations) của 10 công trình bản lề: *Shanahan (2019), Al-Natour (2011), Zhang (2021), Xiao & Benbasat (2007, 2018), Beatty & Ferrell (1998), Rook & Fisher (1995), Verhagen (2011), Tangney (2004), Baumeister (2002), Badgaiyan (2015)*.

---

## 2. KẾ HOẠCH "PHÂN MẢNH HỌC THUẬT": 4 BÀI BÁO SCOPUS Q1 TIỀM NĂNG

Từ một bộ khung luận án, bạn hoàn toàn có thể "chẻ" ra **4 bài báo quốc tế độc lập** với góc nhìn và đóng góp học thuật khác nhau:

```
                                  [HỆ DỮ LIỆU LUẬN ÁN TIẾN SĨ]
                                                │
         ┌──────────────────────┬───────────────┴───────────────┬──────────────────────┐
         ▼                      ▼                               ▼                      ▼
    [BÀI BÁO 1]            [BÀI BÁO 2]                     [BÀI BÁO 3]            [BÀI BÁO 4]
  Tổng Quan Y Văn &     Mô Hình Trung Gian             Tính Mới Lạ & Khám      Góc Khuất AI & Sự Suy
 Trắc Lượng Thư Mục     Chuỗi Có Điều Tiết             Phá Bất Ngờ (Novelty)   Giảm Tự Kiểm Soát (Ethics)
  (PRISMA 2020 SLR)      (Core Empirical)               (Experimental / SEM)     (Consumer Vulnerability)
         │                      │                               │                      │
         ▼                      ▼                               ▼                      ▼
  Tạp chí: JRCS /        Tạp chí: JBR /                  Tạp chí: I&M /          Tạp chí: JCM /
   IJCS (Scopus Q1)       CHB (Scopus Q1)                 ECR (Scopus Q1)         JCR (Scopus Q1)
```

---

### BÀI BÁO 1: BÀI TỔNG QUAN Y VĂN CÓ HỆ THỐNG & BẢN ĐỒ KHOA HỌC (SLR & SCIENCE MAPPING)
- **Tên bài đề xuất**:  
  *“Algorithmic Curation and Online Impulse Buying: A PRISMA 2020 Systematic Literature Review and Bibliometric Science Mapping of Contemporary Evidence (2018–2026)”*
- **Tạp chí mục tiêu**:  
  - *International Journal of Consumer Studies* (Wiley, Scopus Q1, IF 8.6, ABS 2*)
  - *Journal of Retailing and Consumer Services* (Elsevier, Scopus Q1, IF 11.0, ABS 2*)
- **Dữ liệu sử dụng**:  
  - 866 bài báo Scopus Q1 từ tệp `luan_an_real_network.json` và lưu đồ PRISMA 2020 (`2,500 ➔ 1,441 ➔ 866 bài`).
- **Điểm nhấn học thuật (Hook & Contribution)**:
  - Đây là bài tổng quan y văn đầu tiên kết hợp cả PRISMA 2020 và VOSviewer để vạch ra 4 cụm chủ đề đương đại và định lượng hóa 3 khoảng trống nghiên cứu then chốt trong kỷ nguyên AI thương mại.
- **Tiến độ**: Đã có 90% số liệu và đồ họa từ Web Hub. Chỉ cần chấp bút viết bài theo mẫu của IJCS.

---

### BÀI BÁO 2: BÀI BÁO THỰC NGHIỆM CỐT LÕI (CORE EMPIRICAL DISSERTATION PAPER)
- **Tên bài đề xuất**:  
  *“When AI Recommendations Meet Self-Control: A Moderated Serial Mediation Model of Algorithmic Curation and Online Impulse Buying”*
- **Tạp chí mục tiêu**:  
  - *Journal of Business Research* (Elsevier, Scopus Q1, IF 10.5, ABS 3*)
  - *Computers in Human Behavior* (Elsevier, Scopus Q1, IF 9.0, ABS 3*)
  - *Asia Pacific Journal of Marketing and Logistics* (Emerald, Scopus Q1, ABS 1*)
- **Khung lý thuyết**:  
  - Tích hợp S-O-R Framework (*Mehrabian & Russell 1974*) và Self-Regulation Theory (*Baumeister 2007*).
- **Mô hình kiểm định**:  
  - Đầy đủ 8 biến: $PP, ACC, NOV \to ESAT \to UBI \to OIB$, điều tiết bởi $SC$ và kiểm soát bởi $IBT$.
- **Phương pháp phân tích**:  
  - PLS-SEM (SmartPLS 4) với mẫu $N \ge 400$ tại thị trường thương mại điện tử Việt Nam (Shopee/TikTok Shop).
- **Điểm nhấn học thuật**:  
  - Tái định nghĩa biến Hài lòng trong quá trình (In-process ESAT) và chứng minh vai trò kìm hãm của Self-Control đối với tác động của thuật toán AI.

---

### BÀI BÁO 3: BÀI CHUYÊN SÂU VỀ TÍNH MỚI LẠ VÀ BẤT NGỜ (SERENDIPITY & NOVELTY IN LIVE-COMMERCE)
- **Tên bài đề xuất**:  
  *“Beyond Recommendation Accuracy: The Role of Novelty and Serendipity in Triggering In-Process Satisfaction and Impulsive Purchases in Discovery Shopping”*
- **Tạp chí mục tiêu**:  
  - *Information & Management* (Elsevier, Scopus Q1, IF 9.9, ABS 3*)
  - *Electronic Commerce Research and Applications* (Elsevier, Scopus Q1, IF 6.0)
- **Góc nhìn học thuật (Unique Angle)**:
  - Tập trung giải quyết bài toán: Các thuật toán AI chỉ chú trọng độ chính xác (Accuracy) sẽ làm người dùng bị nhàm chán (Filter Bubble). Chính **Tính mới mẻ (Novelty)** và **Khám phá bất ngờ (Serendipity)** trên các nền tảng video ngắn (TikTok Shop/Reels) mới là động lực bùng nổ cảm xúc thôi thúc mua bốc đồng.
- **Biến trọng tâm**:  
  - So sánh đối trọng giữa $ACC$ và $NOV$ tác động lên $ESAT$ và $UBI$.

---

### BÀI BÁO 4: BÀI VỀ GÓC KHUẤT AI & ĐẠO ĐỨC KINH DOANH (DARK SIDE OF AI & CONSUMER VULNERABILITY)
- **Tên bài đề xuất**:  
  *“The Algorithmic Seduction: How AI Personalization Depletes Consumer Self-Control and Drives Post-Purchase Regret”*
- **Tạp chí mục tiêu**:  
  - *Journal of Consumer Marketing* (Emerald, Scopus Q1, ABS 1*)
  - *Journal of Consumer Behaviour* (Wiley, Scopus Q1, ABS 2*)
- **Khung lý thuyết**:  
  - Ego Depletion Theory (*Baumeister 2002*) & Cognitive Dissonance Theory (*Festinger 1957*).
- **Đóng góp chính sách & Xã hội**:
  - Đưa ra hàm ý cảnh báo cho các nhà hoạch định chính sách bảo vệ người tiêu dùng trước các thuật toán AI "thao túng tâm lý", gây suy giảm ý chí tự kiểm soát tài chính của giới trẻ (Gen Z).

---

## 3. CÁCH SỬ DỤNG KHO DỮ LIỆU ĐỂ TÌM KIẾM Ý TƯỞNG NHANH

Mỗi khi bạn muốn suy nghĩ ý tưởng cho một phần lập luận, hãy mở Terminal trong thư mục dự án và chạy công cụ truy vấn thông minh:

```bash
# 1. Tìm các bài bàn về sự tự kiểm soát (Self-control)
python .agents/skills/phd-literature-review/scripts/query_literature_corpus.py "self-control"

# 2. Tìm các bài về sự hài lòng trong quá trình (In-process satisfaction)
python .agents/skills/phd-literature-review/scripts/query_literature_corpus.py "in-process"

# 3. Tìm các bài về tính mới lạ và bất ngờ (Novelty / Serendipity)
python .agents/skills/phd-literature-review/scripts/query_literature_corpus.py "serendipity"

# 4. Tìm các bài kết hợp mô hình S-O-R và mua bốc đồng
python .agents/skills/phd-literature-review/scripts/query_literature_corpus.py "s-o-r impulse"
```

Công cụ sẽ tự động rà soát qua 1,441 bài báo Scopus Q1, trích xuất đúng tên tác giả, năm, trích dẫn APA, mã DOI và câu văn phát hiện thực nghiệm để bạn đưa ngay vào bài viết!
