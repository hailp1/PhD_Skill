# QUY CHUẨN CHỐNG BỊA ĐẶT TRÍCH DẪN & KIẾN THỨC HỌC THUẬT
*(Anti-Hallucination Citation & Factual Grounding Protocol for Doctoral Research)*

---

## 1. MỐI NGUY HẠI CỦA "TRÍCH DẪN MA" (HALLUCINATED CITATIONS) TRONG LUẬN ÁN

Một trong những khuyết tật nguy hiểm nhất của các mô hình ngôn ngữ lớn (LLMs/AI) là **hiện tượng tự bịa đặt tài liệu tham khảo (Hallucination)**:
- Tự ghép tên tác giả nổi tiếng với một năm xuất bản không có thật.
- Bịa ra tiêu đề bài báo nghe rất thuyết phục nhưng không tồn tại trên đời.
- Gán ghép sai phát hiện nghiên cứu (ví dụ: tác giả A không hề nghiên cứu biến M nhưng AI tự nhận định rằng tác giả A tìm thấy tác động của M).
- Tự tạo DOI giả mạo.

> **HẬU QUẢ**: Trong bảo vệ Luận án Tiến sĩ và phản biện tạp chí Scopus Q1/Q2, chỉ cần hội đồng phát hiện **DUY NHẤT 01 trích dẫn bịa đặt**, toàn bộ luận án sẽ bị nghi ngờ về tính liêm chính học thuật (Academic Integrity), có thể dẫn đến **đình chỉ bảo vệ hoặc bác bỏ bài báo vĩnh viễn**.

---

## 2. NGUYÊN TẮC THÉP "ZERO-TOLERANCE" TRONG DỰ ÁN

Mọi nội dung học thuật được tạo ra trong workspace này đều tuân thủ 3 nguyên tắc ràng buộc:

### Nguyên tắc 1: Xác thực Nguồn gốc Thực tế (Real-World Provenance)
Mọi tài liệu trích dẫn `(Author, Year)` hoặc danh mục tài liệu tham khảo (References) bắt buộc phải là công trình:
- Có thật 100% trên thế giới.
- Được lập chỉ mục chính thức trên các cơ sở dữ liệu học thuật quốc tế: **Scopus, Web of Science, Crossref, PubMed, hoặc Google Scholar**.
- Có mã định danh số **DOI (Digital Object Identifier)** hợp lệ và truy cập được (`https://doi.org/...`).

### Nguyên tắc 2: Cấm Tuyệt đối Đoán Mò hoặc Tự Bịa (No Guesswork)
Nếu AI không chắc chắn 100% về thông số bài báo (tên tạp chí, số tập, số trang, năm xuất bản, hoặc phát hiện cụ thể):
- **CẤM** tự điền thông số giả định.
- **BẮT BUỘC** phải sử dụng công cụ kiểm chứng trực tiếp (`citation_verifier.py`, Crossref API, OpenAlex API hoặc công cụ tìm kiếm web học thuật) để xác nhận thông tin trước khi cung cấp cho người dùng.
- Nếu không tìm thấy bằng chứng thực tế, AI phải thừa nhận sự thiếu hụt thông tin và yêu cầu người dùng cung cấp file gốc.

### Nguyên tắc 3: Trung thực về Phát hiện Thực nghiệm (Factual Fidelity)
Không bao giờ gán ghép sai phát hiện cho các học giả:
- Khi viết: *"Smith et al. (2021) khẳng định rằng..."*, nội dung đó phải phản ánh đúng kết quả thực tế của bài báo.
- Tuyệt đối không tự bịa đặt số liệu thống kê (ví dụ: bịa đặt hệ số $\beta = 0.42, p < 0.01$) của các tác giả khác.

---

## 3. CÔNG CỤ TỰ ĐỘNG XÁC THỰC TRÍCH DẪN (CITATION VERIFIER TOOL)

Dự án trang bị công cụ kiểm tra trích dẫn trực tiếp kết nối với cơ sở dữ liệu **Crossref Official Registry** (cơ quan cấp phát DOI học thuật toàn cầu):

### 3.1. Xác thực một mã DOI cụ thể:
```bash
python .agents/skills/phd-literature-review/scripts/citation_verifier.py --doi "10.1108/EBR-11-2018-0203"
```
- Nếu bài báo có thật: Trả về trạng thái `VERIFIED`, kèm tiêu đề gốc, tác giả, tên tạp chí và năm xuất bản chính xác.
- Nếu bài báo giả mạo: Cảnh báo đỏ `HALLUCINATION_ALERT` (*DOI does not exist in Crossref database*).

### 3.2. Truy vấn kiểm chứng một cụm trích dẫn / tiêu đề bài báo:
```bash
python .agents/skills/phd-literature-review/scripts/citation_verifier.py --query "Hair When to use and how to report the results of PLS-SEM"
```

### 3.3. Quét kiểm tra toàn bộ một file bản thảo (Đề cương / Chương luận án):
```bash
python .agents/skills/phd-literature-review/scripts/citation_verifier.py --file your_chapter.md
```
Script sẽ tự động bóc tách tất cả các DOI trong tài liệu, kiểm tra tính xác thực của từng bài báo và xuất báo cáo:
`AUDIT SUMMARY: [X] Verified Authentic | [Y] Fake/Hallucinated`.
