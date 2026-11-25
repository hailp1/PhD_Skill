# BẢN GHI CHÚ HỌC THUẬT VÀ TRÍCH DẪN TÀI LIỆU (RESEARCH NOTE)
*(Tóm tắt chuyên sâu phục vụ Luận án Tiến sĩ & Công bố Quốc tế - Tiết kiệm Token tra cứu)*

---

## 1. THÔNG TIN THƯ MỤC CHUẨN XÁC (BIBLIOGRAPHIC METADATA)

- **Tên bài báo**: *Customer satisfaction: a mathematical framework for its analysis and its measurement*
- **Tác giả**: Roberto Ferrentino & Carmine Boniello
- **Đơn vị công tác**: Department of Economic and Statistics Sciences, University of Salerno, Fisciano, Salerno, Italy
- **Tạp chí**: *Computational Management Science* (Nhà xuất bản Springer Nature)
- **Năm xuất bản**: 2018 *(Nhận bài: 07/05/2017; Chấp nhận: 26/03/2018; Xuất bản online: 09/05/2018)*
- **Tập san / Số / Trang**: Vol. 15, No. 3, pp. 395–417
- **Chỉ số phân hạng**: Scopus Q2 / Springer Nature
- **Định danh số DOI**: `10.1007/s10287-018-0305-1`
- **Tập tin PDF toàn văn trong dự án**: [s10287-018-0305-1.pdf](file:///d:/SE_Project/khoahoc/s10287-018-0305-1.pdf)
- **Trích dẫn chuẩn APA 7th**:
  > Ferrentino, R., & Boniello, C. (2018). Customer satisfaction: A mathematical framework for its analysis and its measurement. *Computational Management Science*, 15(3), 395–417. https://doi.org/10.1007/s10287-018-0305-1

---

## 2. MỤC TIÊU VÀ ĐÓNG GÓP HỌC THUẬT CỐT LÕI (RESEARCH AIMS & NOVELTY)

1. **Bản chất bài viết**: Bài báo thuộc dạng **Tổng quan Phương pháp luận (Methodological & Theoretical Review)**, thiết lập cầu nối chặt chẽ giữa lý thuyết quản trị Marketing về Sự hài lòng khách hàng (*Customer Satisfaction - CS*) và các mô hình thống kê toán học hiện đại.
2. **Khoảng trống học thuật giải quyết**:
   - Trước đây, việc đo lường sự hài lòng khách hàng thường dựa vào các chỉ số đơn giản, rời rạc (tỷ lệ phàn nàn, tỷ lệ rời bỏ), vốn mang tính thô sơ và không phản ánh được cấu trúc tâm lý tiềm ẩn.
   - Tác giả cung cấp một **khung toán học hoàn chỉnh** để chuẩn hóa quy trình đo lường sự hài lòng qua mô hình phương trình cấu trúc biến tiềm ẩn (*Structural Equation Modeling with Latent Variables - SEM*).

---

## 3. TÓM TẮT CHI TIẾT THEO TỪNG PHẦN CỦA BÀI BÁO

### Phần 1 - 3: Cơ sở lý thuyết về Sự hài lòng khách hàng (Theoretical Underpinnings)
- **Định nghĩa**: Sự hài lòng của khách hàng là sự đánh giá về **mức độ chênh lệch (discrepancy/gap)** giữa hiệu năng cảm nhận sau khi sử dụng dịch vụ/sản phẩm ($P$) và kỳ vọng trước đó ($E$) (dựa trên trường phái kỳ vọng - xác nhận của Oliver, 1980, 1999).
  - Nếu $P < E$: Khách hàng bất mãn (Dissatisfied).
  - Nếu $P = E$: Khách hàng hài lòng (Satisfied).
  - Nếu $P > E$: Khách hàng thích thú/phấn khích (Customer Delight) (Guido et al., 2010).
- **Ý nghĩa quản trị**:
  - Khách hàng hài lòng giúp ổn định dòng tiền (cash flow), giảm sự nhạy cảm về giá và cạnh tranh khuyến mãi (Fornell et al., 2006).
  - Giữ chân khách hàng hiện tại có chi phí thấp hơn 5 lần so với việc thu hút khách hàng mới (Myers et al., 1999).

### Phần 4: Đánh giá 6 Mô hình Đo lường Truyền thống (Traditional Measurement Approaches)
Tác giả hệ thống hóa và đưa ra công thức toán học cho các mô hình kinh điển:
1. **Mô hình SERVQUAL** (Parasuraman et al., 1985, 1988):
   - Đo lường khoảng cách giữa Cảm nhận và Kỳ vọng ($p_{jih} - a_{jih}$) qua 5 chiều kích: Tính hữu hình (Tangibles), Độ tin cậy (Reliability), Khả năng đáp ứng (Responsiveness), Năng lực đảm bảo (Assurance), và Sự thấu cảm (Empathy).
   - Chỉ số tổng hợp $CSI = \frac{1}{N} \sum_{h=1}^N \left[ \sum_{j=1}^5 w_{jh} \left( \sum_{i=1}^{q_j} \frac{p_{jih} - a_{jih}}{q_j} \right) \right]$.
2. **Mô hình SERVPERF** (Cronin & Taylor, 1994):
   - Phê phán SERVQUAL về tính bất ổn định của điểm hiệu số; SERVPERF chỉ đo lường trực tiếp trên Cảm nhận thực tế ($P$).
3. **Mô hình Chất lượng Định mức - Normed Quality Model** (Teas, 1993):
   - Phân biệt giữa Kỳ vọng lý tưởng ($AI$) và Kỳ vọng có thể đạt được ($AE$).
4. **Two-Way Model** (Schvaneveldt et al., 1991): Đánh giá song song khía cạnh khách quan và chủ quan.
5. **Qualitometro** (Rossetto & Franceschini, 1998): Theo dõi trực tuyến sai lệch kỳ vọng theo thời gian.
6. **Mô hình Kano** (Noriaki Kano): Phân loại thuộc tính thành: Bắt buộc (Must-be), Một chiều (One-dimensional), và Thu hút (Attractive).

### Phần 5: Khung Phương trình Cấu trúc Tuyến tính (SEM Framework) - Trọng tâm giá trị
Tác giả khẳng định: **SEM là phương pháp chặt chẽ và chuẩn xác nhất hiện nay để đo lường các cấu trúc tâm lý tiềm ẩn không quan sát trực tiếp được (Latent Variables) như Sự hài lòng**.

#### A. So sánh hai trường phái SEM:
1. **Covariance-Based SEM (CB-SEM / LISREL / FASEM)** (Jöreskog, 1970; Bentler, 1986):
   - Dựa trên ma trận hiệp phương sai, ước lượng bằng Maximum Likelihood (ML).
   - Đòi hỏi phân phối chuẩn đa biến nghiêm ngặt và cỡ mẫu lớn.
2. **Component-Based SEM / Partial Least Squares (PLS-PM / PLS-SEM)** (Herman Wold, 1973; Lohmöller, 1989; Chin, 1998):
   - Dựa trên phương sai và thành phần chính.
   - **4 Ưu điểm vượt trội của PLS-SEM**:
     - Đặt ít giả định phân phối dữ liệu (không bắt buộc chuẩn tuyệt đối).
     - Hoạt động tốt trên kích thước mẫu thực tiễn trong nghiên cứu kinh doanh.
     - Tránh được hiện tượng lỗi không hội tụ (non-convergence) của thuật toán.
     - Tối ưu hóa năng lực dự báo cho các biến hành vi khách hàng.

#### B. Phân loại Mô hình Đo lường (Measurement Models / Outer Models):
- **Dạng Phản xạ (Reflective Scheme)**: Biến quan sát phản ánh biến tiềm ẩn ($x_h = \pi_{h0} + \pi_h \xi + \varepsilon_h$). (Đây là dạng phù hợp cho thang đo Sự hài lòng).
- **Dạng Định hình (Formative Scheme)**: Các biến quan sát hợp thành biến tiềm ẩn ($\xi = \sum \omega_h x_h + \delta$).
- **Dạng MIMIC**: Kết hợp cả phản xạ và định hình.

#### C. Các công thức kiểm định độ tin cậy cốt lõi:
- **Tính đơn hướng (Unidimensionality)**: Phân tích thành phần chính (PCA), chỉ số riêng (Eigenvalue) thứ nhất phải $> 1$ và chỉ số thứ hai phải $< 1$.
- **Hệ số Cronbach's Alpha ($\alpha$)**:
  $$\alpha = \frac{p}{p - 1} \left( 1 - \frac{\sum s_h^2}{s_T^2} \right)$$
- **Độ tin cậy tổng hợp Dillon-Goldstein's $\rho$ (Composite Reliability - CR)**:
  $$\rho = \frac{\left( \sum_{h=1}^p \pi_h \right)^2}{\left( \sum_{h=1}^p \pi_h \right)^2 + \sum_{h=1}^p (1 - \pi_h^2)}$$
  *Ý nghĩa*: Bài báo chỉ ra rằng chỉ số $\rho$ (CR) phản ánh độ tin cậy tốt hơn Cronbach's $\alpha$ vì không mặc định trọng số của các câu hỏi bằng nhau.

---

## 4. MA TRẬN ỨNG DỤNG VÀO LUẬN ÁN TIẾN SĨ CỦA NCS LÊ PHÚC HẢI

| Vị trí trong Luận án / Bài báo | Nội dung ứng dụng cụ thể | Giá trị học thuật mang lại |
| :--- | :--- | :--- |
| **Chương 2 (Tổng quan lý thuyết)** | Trích dẫn lý luận về sự hài lòng: Nêu rõ sự hài lòng trong thương mại điện tử là cấu trúc tâm lý tiềm ẩn cần được mô hình hóa theo dạng phản xạ (Reflective). | Củng cố tính chặt chẽ của biến trung gian *E-Satisfaction*. |
| **Chương 3 (Phương pháp nghiên cứu)** | Trích dẫn trang 14-16 của bài báo để **biện minh cho việc chọn PLS-SEM (SmartPLS 4)** thay vì CB-SEM (AMOS/LISREL). | Trả lời thuyết phục câu hỏi bảo vệ đề cương của Hội đồng và phản biện tạp chí WoS/Scopus. |
| **Chương 4 (Phân tích kết quả)** | Sử dụng công thức Dillon-Goldstein's $\rho$ để giải thích tại sao cần báo cáo song song Cronbach's $\alpha$ và Composite Reliability (CR $\ge 0.70$). | Chuẩn hóa phương pháp đánh giá mô hình đo lường theo tiêu chuẩn quốc tế. |
| **Bài báo WoS số 1 (PAP-01)** | Trích dẫn Ferrentino & Boniello (2018) ở phần *Theoretical Framework & Measurement Model Assessment*. | Tăng mật độ trích dẫn tạp chí Q1/Q2 có thực, loại trừ rủi ro trích dẫn giả mạo. |

---

## 5. MẪU CÂU TRÍCH DẪN SẴN DÙNG (READY-TO-USE CITATION PHRASES)

### Mẫu câu tiếng Việt (Dùng cho Luận án):
> *"Để đo lường sự hài lòng trực tuyến một cách chuẩn xác, nghiên cứu này tiếp cận sự hài lòng như một cấu trúc tiềm ẩn đa diện theo mô hình đo lường phản xạ (reflective measurement model), phù hợp với khung phân tích phương trình cấu trúc của Ferrentino và Boniello (2018). Đồng thời, phương pháp PLS-SEM được lựa chọn nhờ khả năng xử lý linh hoạt các biến hành vi tiêu dùng mà không đòi hỏi nghiêm ngặt về giả định phân phối chuẩn đa biến (Ferrentino & Boniello, 2018)."*

### Mẫu câu tiếng Anh (Dùng cho Bài báo WoS / Scopus):
> *"Consistent with the mathematical and structural formulation by Ferrentino and Boniello (2018), e-satisfaction is operationalized as a reflective latent construct to capture the psychological evaluation resulting from algorithmic recommendations. Furthermore, partial least squares structural equation modeling (PLS-SEM) was adopted over covariance-based alternatives due to its superior predictive capability and methodological robustness with non-normal behavioral survey data (Ferrentino & Boniello, 2018)."*
