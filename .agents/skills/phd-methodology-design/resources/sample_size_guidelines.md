# HƯỚNG DẪN XÁC ĐỊNH CỠ MẪU CHO LUẬN ÁN TIẾN SĨ
*(Sample Size Calculation for Doctoral Research in Business & Marketing)*

---

## 1. CÁC PHƯƠNG PHÁP XÁC ĐỊNH CỠ MẪU CHUẨN MỰC

Trong luận án tiến sĩ kinh tế/quản trị kinh doanh, hội đồng chấm luận án thường soi xét rất kỹ căn cứ khoa học để xác định cỡ mẫu. Nghiên cứu sinh nên kết hợp ít nhất 2 căn cứ sau đây:

### 1.1. Phương pháp Phân tích Lực lượng Thống kê (Statistical Power Analysis via G*Power)
- **Công cụ**: Phần mềm chuyên dụng G*Power 3.1 (miễn phí của Đại học Heinrich-Heine-Universität Düsseldorf).
- **Thông số chuẩn cho hồi quy tuyến tính / SEM**:
  - Test family: $F$ tests $\rightarrow$ Linear multiple regression: Fixed model, $R^2$ deviation from zero.
  - Type of power analysis: A priori: Compute required sample size.
  - Effect size ($f^2$): $0.15$ (Mức tác động trung bình theo Cohen, 1988).
  - Mức ý nghĩa ($\alpha$ err prob): $0.05$.
  - Lực lượng kiểm định (Power: $1 - \beta$): $0.80$ (tối thiểu) đến $0.95$ (chuẩn mực luận án).
  - Number of predictors: Số lượng biến độc lập tác động vào một biến phụ thuộc.
- **Kết quả ước tính**: Thường dao động từ $150 - 250$ quan sát.

### 1.2. Quy tắc Kinh nghiệm của Hair et al. (2019, 2022) cho PLS-SEM
1. **Quy tắc "10 lần" (10-times rule)**: Cỡ mẫu tối thiểu bằng 10 lần số đường dẫn cấu trúc lớn nhất hướng vào một biến phụ thuộc trong mô hình. Ví dụ: Nếu biến phụ thuộc nhận tối đa 6 mũi tên $\rightarrow$ Mẫu tối thiểu = $6 \times 10 = 60$. (Lưu ý: Quy tắc này chỉ là ngưỡng tối thiểu tuyệt đối, không đủ cho luận án tiến sĩ).
2. **Quy tắc Khuyến nghị Thực tế (Practical Rule for PhD)**:
   - Nghiên cứu mô hình cấu trúc phức tạp (nhiều biến trung gian, điều tiết) đòi hỏi **$N \ge 300 - 500$** phiếu hợp lệ để đảm bảo ước lượng bootstrapping ổn định và phân tích đa nhóm (MGA).

### 1.3. Tỷ lệ Biến quan sát trên Người trả lời (Observation-to-Item Ratio)
- Theo Hair et al. (2010, 2014) và Kline (2016):
  - Tỷ lệ tối thiểu: **$5:1$** (5 người trả lời cho 1 biến quan sát/câu hỏi).
  - Tỷ lệ lý tưởng: **$10:1$** hoặc **$15:1$** (10 đến 15 người trả lời cho 1 câu hỏi).
- **Ví dụ tính toán thực tế**:
  - Mô hình có 8 biến tiềm ẩn, tổng cộng 36 câu hỏi khảo sát Likert.
  - Theo tỷ lệ 10:1 $\rightarrow$ Cỡ mẫu cần thiết tối thiểu = $36 \times 10 = 360$ quan sát hợp lệ.
  - Dự phòng tỷ lệ hao hụt / không đạt chất lượng (khoảng 20% do trả lời ẩu, trùng lặp, thiếu thông tin) $\rightarrow$ Cần phát đi:
    $$N_{phat\_ra} = \frac{360}{1 - 0.20} = 450 \text{ phiếu}.$$

---

## 2. BẢNG TỔNG HỢP KHUYẾN NGHỊ CỠ MẪU CHO LUẬN ÁN TIẾN SĨ

| Phương pháp phân tích dữ liệu | Ngưỡng mẫu tối thiểu | Ngưỡng mẫu khuyến nghị cho Luận án | Ghi chú quan trọng |
| :--- | :---: | :---: | :--- |
| **Hồi quy bội (Multiple Regression)** | $100$ | $200 - 300$ | Đủ để kiểm tra đa cộng tuyến và độ tin cậy |
| **CB-SEM (AMOS / LISREL / lavaan)** | $200$ | $350 - 500$ | CB-SEM nhạy cảm với kích thước mẫu lớn và phân phối chuẩn đa biến |
| **PLS-SEM (SmartPLS / cSEM)** | $150$ | $300 - 500$ | Phù hợp với mô hình phức tạp, nhiều biến trung gian/điều tiết |
| **Phân tích Đa nhóm (PLS-MGA)** | $100$ mỗi nhóm | $150 - 200$ mỗi nhóm | Ví dụ: So sánh Nhóm Gen Z vs Gen Y; So sánh Nam vs Nữ |
| **Nghiên cứu Thực nghiệm (Experimental 2x2)** | $30$ mỗi ô | $50 - 80$ mỗi ô (Cell) | Thiết kế 4 ô (2x2) $\rightarrow$ Tổng mẫu $200 - 320$ người |
