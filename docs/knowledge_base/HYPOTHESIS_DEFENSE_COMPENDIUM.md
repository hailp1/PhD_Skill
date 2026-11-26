# HỒ SƠ BIỆN CHỨNG BẢO VỆ 9 GIẢ THUYẾT NGHIÊN CỨU (HYPOTHESIS DEFENSE COMPENDIUM)
*(Thư viện Tri thức Luận án Tiến sĩ - NCS Lê Phúc Hải | Luận Cứ Học Thuật Đối Chất Hội Đồng)*

---

## 1. SƠ ĐỒ QUAN HỆ CỦA 9 GIẢ THUYẾT NGHIÊN CỨU

```mermaid
flowchart LR
    subgraph STIMULUS ["KÍCH THÍCH AI (STIMULI)"]
        PP["Cá nhân hóa (PP)"]
        ACC["Độ chính xác (ACC)"]
        NOV["Tính mới mẻ (NOV)"]
    end

    subgraph ORGANISM ["TIẾN TRÌNH TÂM LÝ (ORGANISMS)"]
        ESAT["Hài lòng trong quá trình (ESAT)"]
        UBI["Thôi thúc mua bốc đồng (UBI)"]
    end

    subgraph RESPONSE ["PHẢN ỨNG HÀNH VI (RESPONSE)"]
        OIB["Mua bốc đồng thực tế (OIB)"]
    end

    subgraph MODERATION ["BIẾN ĐIỀU TIẾT (BOUNDARY)"]
        SC["Khả năng tự kiểm soát (Self-Control)"]
    end

    %% Hypotheses Paths
    PP -->|H1 (+)| ESAT
    ACC -->|H2 (+)| ESAT
    NOV -->|H3 (+)| ESAT

    PP -->|H4 (+)| UBI
    ACC -->|H5 (+)| UBI
    NOV -->|H6 (+)| UBI

    ESAT -->|H7 (+)| UBI
    UBI -->|H8 (+)| OIB

    SC -.->|H9: Điều tiết âm (-)| OIB
```

---

## 2. BIỆN CHỨNG CHI TIẾT TỪNG GIẢ THUYẾT & KỊCH BẢN ĐỐI THOẠI HỌC THUẬT

### Nhóm 1: Tác động của Kích thích AI lên Sự hài lòng trong quá trình (H1, H2, H3)

#### Giả thuyết H1: Cá nhân hóa cảm nhận (PP) có tác động tích cực đến Sự hài lòng trong quá trình (ESAT).
* **Luận cứ lý thuyết**: Vận dụng Lý thuyết Phù hợp Nhận thức (Cognitive Fit Theory - Vessey, 1991). Khi gợi ý AI phản ánh chính xác thị hiếu và lịch sử duyệt web của cá nhân, người dùng tiết kiệm tối đa chi phí tìm kiếm (Search costs) và nhận thức được sự thấu cảm của hệ sinh thái số.
* **Bằng chứng thực nghiệm**: Shanahan et al. (2019, *JRCS*); Ampadu et al. (2022, *JRCS*).
* **Phản biện Hội đồng**: *"Liệu cá nhân hóa quá mức có gây ra cảm giác lo ngại xâm phạm quyền riêng tư (Privacy Concern) làm giảm hài lòng?"*
* **Câu trả lời đanh thép**: *"Trong phạm vi phiên duyệt web tức thời, khi hệ thống gợi ý đem lại giá trị hữu dụng vượt trội, lợi ích nhận thức (Perceived benefits) sẽ lấn át sự lo ngại (Privacy paradox - Norberg et al., 2007). Hơn nữa, luận án định vị ESAT là sự hài lòng trong tiến trình tương tác (In-process), phản ánh cảm giác thỏa mãn khi thao tác diễn ra mượt mà."*

---

#### Giả thuyết H2: Độ chính xác cảm nhận (ACC) có tác động tích cực đến Sự hài lòng trong quá trình (ESAT).
* **Luận cứ lý thuyết**: Độ chính xác của thuật toán tạo dựng niềm tin ban đầu (Initial trust) và khẳng định tính năng lực của hệ thống (Al-Natour et al., 2011). Người tiêu dùng cảm thấy phiên duyệt web hiệu quả vì không bị làm phiền bởi các kết quả sai lệch hoặc rác thông tin (Information noise).
* **Bằng chứng thực nghiệm**: Al-Natour, Benbasat, & Cenfetelli (2011, *JAIS*); Xiao & Benbasat (2018, *DSS*).
* **Phản biện Hội đồng**: *"Nếu chính xác là hiển nhiên của thuật toán thì có cần đo không?"*
* **Câu trả lời đanh thép**: *"Mặc dù thuật toán máy tính có độ chuẩn xác kỹ thuật, nhưng 'Độ chính xác cảm nhận' là đánh giá chủ quan của con người. Người mua không quan tâm đến mã nguồn của thuật toán mà chỉ đánh giá xem sản phẩm hiện lên có thực sự đáp ứng đúng tiêu chí họ mong muốn hay không."*

---

#### Giả thuyết H3: Tính mới mẻ cảm nhận (NOV) có tác động tích cực đến Sự hài lòng trong quá trình (ESAT).
* **Luận cứ lý thuyết**: Dựa trên Lý thuyết Tìm kiếm Thông tin Tối ưu (Information Foraging Theory - Pirolli & Card, 1999) và Tâm lý học Khám phá. Con người luôn có động cơ bẩm sinh tìm kiếm sự mới lạ (Novelty-seeking). Tính mới lạ phá vỡ sự đơn điệu của các đề xuất quen thuộc, kích thích hưng phấn và đem lại cảm xúc thỏa mãn vượt trội.
* **Bằng chứng thực nghiệm**: Ping, Li, & Zhu (2025, *ECR*); Zhang, Xiao, & Zhou (2021, *CHB*).
* **Phản biện Hội đồng**: *"Liệu sản phẩm quá mới lạ có khiến người mua cảm thấy bỡ ngỡ hoặc không tin tưởng?"*
* **Câu trả lời đanh thép**: *"Đó chính là lý do mô hình đặt Tính mới mẻ (NOV) song hành cùng Độ chính xác (ACC). Sự cộng hưởng giữa 'chuẩn xác' (đáng tin) và 'mới lạ' (bất ngờ) tạo nên điểm cân bằng tối ưu, ngăn chặn cả nguy cơ bong bóng lọc lẫn sự ngờ vực."*

---

### Nhóm 2: Tác động của Kích thích AI trực tiếp lên Sự thôi thúc mua bốc đồng (H4, H5, H6)

#### Giả thuyết H4: Cá nhân hóa cảm nhận (PP) có tác động tích cực đến Sự thôi thúc mua bốc đồng (UBI).
* **Luận cứ lý thuyết**: Khi sản phẩm hiện lên đúng nhu cầu tiềm ẩn, rào cản phòng vệ tâm lý bị hạ thấp. Người mua nhận diện món hàng như một cơ hội tiêu dùng dành riêng cho mình, kích hoạt sự thôi thúc sở hữu ngay tức thì mà không cần suy tính dài hạn.
* **Bằng chứng thực nghiệm**: Chen et al. (2019, *I&M*); Gallin & Portes (2024, *JRCS*).

---

#### Giả thuyết H5: Độ chính xác cảm nhận (ACC) có tác động tích cực đến Sự thôi thúc mua bốc đồng (UBI).
* **Luận cứ lý thuyết**: Gợi ý chuẩn xác loại bỏ sự đắn đo về chất lượng và tính phù hợp của sản phẩm. Khi cảm nhận sản phẩm 'đúng chuẩn' không thể bỏ qua, người dùng nảy sinh cảm giác cấp bách (Sense of urgency) muốn chốt đơn ngay.
* **Bằng chứng thực nghiệm**: Al-Natour et al. (2011); Xiao & Benbasat (2007).

---

#### Giả thuyết H6: Tính mới mẻ cảm nhận (NOV) có tác động tích cực đến Sự thôi thúc mua bốc đồng (UBI).
* **Luận cứ lý thuyết**: Tính mới lạ là ngòi nổ trực tiếp kích thích cảm xúc tò mò và lo sợ bỏ lỡ cơ hội khám phá (Fear of Missing Out - FOMO). Người mua thường không có ý định mua từ trước đối với các sản phẩm mới, nhưng sự xuất hiện bất ngờ của chúng đánh thức ham muốn bốc phát.
* **Bằng chứng thực nghiệm**: Ping et al. (2025); Verhagen & van Dolen (2011).

---

### Nhóm 3: Tiến trình Trung gian Chuỗi và Điều tiết Kìm hãm (H7, H8, H9)

#### Giả thuyết H7: Sự hài lòng trong quá trình (ESAT) có tác động tích cực đến Sự thôi thúc mua bốc đồng (UBI).
* **Luận cứ lý thuyết**: Theo Khung S-O-R, trạng thái tâm lý tích cực (Pleasure / Satisfaction) là nguồn năng lượng xúc tác chuyển hóa kích thích môi trường thành xung năng hành vi. Khi người mua cảm thấy vui vẻ, thoải mái trong phiên duyệt web, họ sẵn sàng nới lỏng nguyên tắc chi tiêu và dễ bị thôi thúc mua sắm hơn.
* **Bằng chứng thực nghiệm**: Goel et al. (2022, *JBR*); Beatty & Ferrell (1998, *JR*).

---

#### Giả thuyết H8: Sự thôi thúc mua bốc đồng (UBI) có tác động tích cực đến Hành vi mua bốc đồng trực tuyến (OIB).
* **Luận cứ lý thuyết**: Dựa trên Mô hình Mua bốc đồng của Beatty & Ferrell (1998) và Badgaiyan & Verma (2015). Sự thôi thúc (Urge) là tiền đề trực tiếp, bắt buộc phải xảy ra trước khi hành vi thực tế (Behavior) được thực hiện. Khi xung năng đủ mạnh, ý định sẽ chuyển hóa thành hành động bấm nút đặt hàng.
* **Bằng chứng thực nghiệm**: Badgaiyan & Verma (2015, *JRCS* - $\beta = 0.61^{***}$); Rook & Fisher (1995, *JCR*).

---

#### Giả thuyết H9: Khả năng tự kiểm soát (Self-Control) điều tiết tiêu cực mối quan hệ giữa Sự thôi thúc mua bốc đồng (UBI) và Hành vi mua bốc đồng trực tuyến (OIB).
* **Luận cứ lý thuyết**: Vận dụng Mô hình Sức mạnh Tự kiểm soát (Baumeister et al., 2007) và Lý thuyết Điều hòa Bản thân (Self-Regulation Theory). Người có năng lực tự kiểm soát cao sở hữu 'nguồn năng lượng ức chế' dồi dào; khi đối diện với sự thôi thúc (UBI), họ có khả năng trì hoãn thỏa mãn (Delay of gratification), cân nhắc lại kế hoạch tài chính và từ chối hành vi mua sắm phi kế hoạch (OIB). Ngược lại, người có mức tự kiểm soát thấp sẽ nhanh chóng đầu hàng trước xung năng.
* **Bằng chứng thực nghiệm**: Tangney, Baumeister, & Boone (2004, *Journal of Personality*); Baumeister (2002, *JCR*).
* **Ý nghĩa học thuật độc đáo**: Giả thuyết H9 là **đóng góp lý thuyết mang tính bản lề của luận án**, giúp giải thích tại sao cùng chịu sự tác động mạnh mẽ của thuật toán AI nhưng có người vẫn kiểm soát được hành vi chi tiêu của mình.
