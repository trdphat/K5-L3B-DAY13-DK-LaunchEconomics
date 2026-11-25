# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

> **Trạng thái:** bộ nhãn 1 do **Vũ Quang Thanh (M3)** gắn độc lập, không trao đổi. Bộ nhãn 2 do **Hồ An Lộc (M4)** gắn độc lập — cột nhãn người 2 và tỉ lệ đồng thuận **chờ M4 cung cấp** (RULES cấm ghép hoặc bịa bộ nhãn thứ hai). Cột “Nhãn thống nhất” là nháp theo bộ nhãn 1, chỉ chốt sau khi đối chiếu.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Vũ Quang Thanh (M3) · Người gắn nhãn 2: Hồ An Lộc (M4) (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | chờ M4 | — | Do người dùng (nháp) |
| 2 | Hệ thống | chờ M4 | — | Hệ thống (nháp) |
| 3 | Ngữ cảnh | chờ M4 | — | Ngữ cảnh (nháp) |
| 4 | Giới hạn hệ thống | chờ M4 | — | Giới hạn hệ thống (nháp) |
| 5 | Ngầm | chờ M4 | — | Ngầm (nháp) |
| 6 | Do người dùng | chờ M4 | — | Do người dùng (nháp) |
| 7 | Hệ thống | chờ M4 | — | Hệ thống (nháp) |
| 8 | Hệ thống | chờ M4 | — | Hệ thống (nháp) |
| 9 | Do người dùng | chờ M4 | — | Do người dùng (nháp) |
| 10 | Ngữ cảnh | chờ M4 | — | Ngữ cảnh (nháp) |
| 11 | Giới hạn hệ thống | chờ M4 | — | Giới hạn hệ thống (nháp) |
| 12 | Ngầm | chờ M4 | — | Ngầm (nháp) |
| 13 | Giới hạn hệ thống | chờ M4 | — | Giới hạn hệ thống (nháp) |
| 14 | Do người dùng | chờ M4 | — | Do người dùng (nháp) |
| 15 | Hệ thống | chờ M4 | — | Hệ thống (nháp) |
| 16 | Ngữ cảnh | chờ M4 | — | Ngữ cảnh (nháp) |
| 17 | Ngầm | chờ M4 | — | Ngầm (nháp) |
| 18 | Ngữ cảnh | chờ M4 | — | Ngữ cảnh (nháp) |
| 19 | Giới hạn hệ thống | chờ M4 | — | Giới hạn hệ thống (nháp) |
| 20 | Hệ thống | chờ M4 | — | Hệ thống (nháp) |

**Tỉ lệ đồng thuận:** chờ bộ nhãn độc lập của M4 — cần từ **16/20 = 80%** theo rubric C3. Nếu dưới 80%, cả nhóm viết lại định nghĩa 5 loại trước khi đi tiếp.

Phân bố bộ nhãn 1: Do người dùng 4 ca (1, 6, 9, 14) · Hệ thống 5 ca (2, 7, 8, 15, 20) · Ngữ cảnh 4 ca (3, 10, 16, 18) · Giới hạn hệ thống 4 ca (4, 11, 13, 19) · Ngầm 3 ca (5, 12, 17).

## Quy tắc phân biệt cho các ca không trùng

Quy tắc tạm áp dụng khi gắn nhãn; sẽ bổ sung một câu cho mỗi ca lệch sau khi so với bộ nhãn M4.

- **Ca 1, 6, 9, 14 là do người dùng, không phải hệ thống:** gốc lỗi là khách nhập sai hoặc chọn sai mục. Việc trợ lý không gợi ý cách sửa nằm ở cột khắc phục, không đổi nhãn.
- **Ca 2, 7, 8, 15, 20 là hệ thống, không phải ngầm:** sai đã lộ ra (ngân hàng trả lỗi, khách mở lại, nhân viên bắt được, bản chính sách không có điều 7.2, hoàn trùng bị phát hiện). Ngầm chỉ dùng khi không ai nhận ra cho tới lúc kiểm tra.
- **Ca 13 là giới hạn hệ thống:** sản phẩm bảo hiểm nằm ngoài phạm vi trợ lý; trả lời chung chung là lỗi khắc phục được, không đổi nguyên nhân gốc.
- **Ca 18 là ngữ cảnh:** số tiền đúng chính sách, chỉ giả định “khách hiểu cách tính” là không khớp hoàn cảnh.
- **Ca 12 là ngầm:** kết quả vẫn đúng nhưng chi phí gấp 3 lần suốt 3 tuần mà không ai thấy; “sai” ở đây là sai về chi phí, không chỉ về câu trả lời.
- **Ca 3, 10, 16 là ngữ cảnh:** trợ lý làm đúng thiết kế (hoàn về ví, từ chối do bất khả kháng, gửi ngay khi xong) nhưng giả định không khớp kỳ vọng của khách.

## Căn cứ gắn nhãn 20 ca (bộ nhãn 1)

| Ca | Nguyên nhân gốc | Nhãn |
| --: | --- | --- |
| 1 | Khách nhập thiếu hai chữ số số tài khoản | Do người dùng |
| 2 | Tool tra bảng giá nhận sai tham số hàng thường thay vì hàng nặng | Hệ thống |
| 3 | Thiết kế hoàn về ví LogiX, khách chờ tiền vào ngân hàng | Ngữ cảnh |
| 4 | Chặng giao của hãng nước ngoài không có dữ liệu | Giới hạn hệ thống |
| 5 | Hoàn theo giá trước giảm, không khách nào báo, không cảnh báo | Ngầm |
| 6 | Khách chọn sai mục hoàn phí giao trễ cho đơn hàng vỡ | Do người dùng |
| 7 | Sổ cái trả 503 nhưng trợ lý vẫn báo đã hoàn thành công | Hệ thống |
| 8 | Trích dẫn điều 7.2 không tồn tại trong chính sách hiện hành | Hệ thống |
| 9 | Khách nhập mã đơn sàn TMĐT thay vì mã vận đơn | Do người dùng |
| 10 | Từ chối hoàn do bất khả kháng đúng chính sách, app vẫn hứa giao 24 giờ | Ngữ cảnh |
| 11 | Đầu vào tin nhắn thoại 40 giây, trợ lý không xử lý âm thanh | Giới hạn hệ thống |
| 12 | Tool trả thiếu trường, kết quả đúng nhưng token gấp 3 lần, không ai thấy | Ngầm |
| 13 | Câu hỏi về bảo hiểm hàng hoá ngoài phạm vi, trợ lý không nói rõ giới hạn | Giới hạn hệ thống |
| 14 | Khách bấm nhầm xác nhận đã nhận tiền | Do người dùng |
| 15 | Tính hoàn 100% trong khi chính sách là 50% cho trễ 24–48 giờ | Hệ thống |
| 16 | Gửi thông báo qua Zalo lúc 2:14 sáng theo thiết kế gửi ngay | Ngữ cảnh |
| 17 | Dùng bảng giá cũ trong bộ nhớ đệm, lệch 1.000–2.000 đ mỗi đơn | Ngầm |
| 18 | Số tiền đúng nhưng tin nhắn không ghi cách tính, khách tưởng thiếu | Ngữ cảnh |
| 19 | Đơn 14 tháng trước, trợ lý chỉ truy cập dữ liệu 12 tháng | Giới hạn hệ thống |
| 20 | Thiếu khoá chống trùng nên hoàn hai lần cho cùng một đơn | Hệ thống |

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi “cả đội”.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed`; cảnh báo khi quá 2% số yêu cầu/ngày | Nhận diện mã sàn TMĐT và tra sang mã vận đơn; không tra được thì hướng dẫn kèm ảnh | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: có `agent_run_completed` status ok nhưng không có `refund_ledger_write` ok cùng `trace_id`; ngưỡng 0 ca | Chỉ báo “đã hoàn” khi sổ cái trả ok; lỗi 503 sau 3 lần thì báo “đang xử lý” và chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ `ticket_reopened` với lý do số tiền trên các ca tính đúng chính sách, theo tuần; ngưỡng 2% | Mẫu tin nhắn luôn ghi cách tính: 30.000 đ × 50% = 15.000 đ | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với reason `thieu_du_lieu`, theo loại yêu cầu; ngưỡng 5%/tuần với `quoc_te` | Giữ cách chuyển kèm tóm tắt; đưa `quoc_te` ra khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu 100 đơn/tuần so với bảng giá hiện hành; ngưỡng 1% đơn lệch | Xoá bộ nhớ đệm khi có bảng giá mới; ghi `price_table_version` vào `agent_run_completed` | Kế toán trưởng |

**Xong khi:** có hai bộ nhãn độc lập và tỉ lệ đồng thuận từ 80% (hoặc định nghĩa đã sửa), bảng 5 ca đủ năm loại. Hai mục còn chờ: cột nhãn người 2 và tỉ lệ đồng thuận — cần bộ nhãn độc lập của M4.
