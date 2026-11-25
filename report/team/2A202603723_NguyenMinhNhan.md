# Báo cáo cá nhân — Nguyễn Minh Nhân - 2A202603723

## 1. Thông tin thành viên

- Họ tên: Nguyễn Minh Nhân
- MSSV: 2A202603723
- Email: 26ai.nhannm@vinuni.edu.vn
- Vai trong nhóm: Người kiểm số (M2), kiêm triển khai code phân tích độ nhạy chi phí và đánh giá rủi ro kinh tế.

## 2. Phần việc phụ trách

- CP2 — Nhiệm vụ B1–B4: Phân tích độ nhạy chi phí của trợ lý AI hoàn phí LogiX-VN.
- Triển khai hàm `chay_B()` trong `src/lab13.py`, tái sử dụng contract `mo_hinh()` của M1.
- Hoàn thiện phần B trong `report/team/bang_chi_phi.md`.
- E2 — Phân tích rủi ro kinh tế trong `report/team/chi_so.md`.
- Kiểm tra công thức, độ chính xác và tính nhất quán của số liệu.
- Chuẩn bị kết quả bàn giao cho M4 tổng hợp hồ sơ Launch v0.

## 3. Đóng góp cụ thể

### CP2 — Phân tích độ nhạy chi phí

- **B1:** Triển khai đầy đủ 9 kịch bản thay đổi giá token, chi phí xem lại, chi phí làm lại, lương nhân viên và giới hạn số lần chạy.
- **B2:** Phân tích kịch bản kết hợp giá token và chi phí xem lại cùng tăng gấp đôi; xếp hạng ba yếu tố ảnh hưởng mạnh nhất.
- **B3:** So sánh giới hạn chạy lại 1, 2 và 3 lần, phân biệt chi phí mỗi việc thành công (CPS) với tổng chi phí hệ thống.
- **B4:** Phân tích kịch bản xem lại 100% trong phạm vi `noi_dia` và `hang_nang`, với hai mức làm lại 9 và 15,3 phút/ca; xác định ngưỡng thời gian xem lại hòa vốn.
- Kiểm chứng kết quả tính toán trong giới hạn sai số 2%.

### E2 — Phân tích rủi ro kinh tế

- Xác định và phân tích 4 rủi ro: làm lại tăng, xem lại 100%, khối lượng thấp và tối ưu sai chi phí khi giới hạn chạy lại.
- Xác định tác động kinh tế, công thức, nguồn số liệu A/B, dấu hiệu theo dõi, hành động và vai trò phụ trách.
- Phân biệt toàn mẫu 1.200 yêu cầu với phạm vi Pilot 982 yêu cầu.
- Ghi rõ các ngưỡng 7%/50%/15% là đề xuất, chưa được xác thực bằng Pilot.
- Chuẩn bị kết quả bàn giao cho M3 và M4.
- Hoàn thành 4 dòng đủ 5 cột, vượt yêu cầu tối thiểu 2 dòng của rubric E2.

Trong quá trình thực hiện, tôi giữ nguyên chữ ký và 9 key trả về của `mo_hinh()`, dữ liệu CSV, starter code và phần việc của các thành viên khác.

## 4. Bằng chứng

### File đóng góp

| File | Nội dung |
|---|---|
| `src/lab13.py` | Hoàn thiện hàm `chay_B()` |
| `report/team/bang_chi_phi.md` | Hoàn thiện B1–B4 |
| `report/team/chi_so.md` | Hoàn thiện section E2 |
| `report/team/2A202603723_NguyenMinhNhan.md` | Báo cáo cá nhân CP2 và E2 |

### Kết quả CP2

Toàn bộ số liệu chi phí dưới đây mang nhãn `simulated`.

| Kịch bản B1 | Chi phí mỗi việc thành công | Thay đổi |
|---|---:|---:|
| Cơ sở A2 | 4.472 đ | — |
| Token ×2 | 4.723 đ | +5,6% |
| Token ÷2 | 4.346 đ | −2,8% |
| Xem lại ×2 | 6.292 đ | +40,7% |
| Xem lại ÷2 | 3.562 đ | −20,3% |
| Làm lại ×2 | 6.787 đ | +51,8% |
| Làm lại ÷2 | 3.315 đ | −25,9% |
| Lương tăng 25% | 5.506 đ | +23,1% |
| Tối đa 2 lần chạy | 4.237 đ | −5,2% |
| Tối đa 1 lần chạy | 4.111 đ | −8,1% |

**B2:** Token và xem lại cùng tăng gấp đôi làm CPS tăng lên 6.543 đ, tương ứng +46,3% [simulated].

Ba yếu tố ảnh hưởng mạnh nhất: làm lại (51,8%), xem lại (40,7%) và lương nhân viên (23,1%).

**B3:** So sánh giới hạn chạy lại:

| Giới hạn | Không thành công | Chi phí hệ thống | CPS |
|---|---:|---:|---:|
| 1 lần | 319 | 7.449.781 đ | 4.111 đ |
| 2 lần | 234 | 6.901.220 đ | 4.237 đ |
| 3 lần | 222 | 7.037.585 đ | 4.472 đ |

Giới hạn 2 lần tối ưu tổng chi phí hệ thống, mặc dù giới hạn 1 lần có CPS thấp hơn. Các kết quả chi phí đều là `simulated`.

**B4:** Khi xem lại 100%:

- Làm lại 9 phút/ca: 11.743 đ/việc, bằng 0,98× baseline [simulated].
- Làm lại 15,3 phút/ca: 12.415 đ/việc, bằng 1,03× baseline [simulated].
- Ngưỡng thời gian xem lại hòa vốn tương ứng khoảng 5,1 và 4,8 phút [simulated].

### Kết quả E2

Nguồn: `report/team/chi_so.md`, đối chiếu với `bang_chi_phi.md` và `src/lab13.py`.

| Rủi ro | Tác động kinh tế |
|---|---|
| Làm lại tăng gấp đôi | CPS đạt 6.787 đ, tăng 51,8%; mốc làm lại trong phạm vi Pilot là 48/982 = 4,9% |
| Xem lại 100% | CPS đạt 11.743–12.415 đ, có nguy cơ vượt baseline 12.000 đ |
| Khối lượng giảm một nửa | 45.000 → 22.500 yêu cầu/tháng; CPS gồm chi phí cố định tăng 4.599 → 5.784 đ |
| Chọn 1 lần thay vì 2 lần chạy | Chi phí hệ thống tăng 548.560 đ và thêm 85 ca không thành công trên toàn mẫu |

Các kết quả chi phí trên đều mang nhãn `simulated`.

### Phương pháp và kết quả kiểm chứng

- Chạy `lab13.py` trong môi trường Python tạm có pandas; chương trình kết thúc thành công.
- Ba phép thử A1: ĐẠT.
- B1 hoàn thành đủ 9 kịch bản, sai số tối đa 0,01496%, thấp hơn ngưỡng 2%.
- Đối chiếu kết quả `chay_A()` và `chay_B()` với báo cáo A1–A4 và B1–B4.
- Sử dụng thư viện chuẩn `csv` để tính độc lập các kịch bản B3, B4, ngưỡng hòa vốn, chi phí làm lại và phân bổ chi phí cố định A4.
- Sử dụng số chưa làm tròn để kiểm chứng. Kết quả B4 là 12.414,79 đ, làm tròn thành 12.415 đ [simulated], chênh 1 đ so với hướng dẫn.
- Kiểm tra E2 có đủ 4 dòng, 5 cột, nguồn số liệu và nhãn `simulated`.
- `git diff --check`: ĐẠT.
- Kiểm tra phạm vi thay đổi, giữ nguyên contract, CSV, starter code và nhiệm vụ của các thành viên khác.

Các phép kiểm chứng tự động trên được thực hiện với sự hỗ trợ của Codex.

### Bàn giao và phối hợp

- M3: Chốt phạm vi, khối lượng theo rollout, ngưỡng an toàn và luật dừng.
- M4: Hoàn thiện tracking event để đo thời gian và tỷ lệ thực tế; đưa 4 rủi ro kinh tế vào mục 7 của E3 với trạng thái Giả lập.
- E2 đã hoàn thành độc lập từ kết quả A/B, không bị chặn bởi D hoặc E1.

## 5. Công cụ AI đã dùng

### ChatGPT

- Hỗ trợ phân tích yêu cầu, phân chia công việc và xác định dependency.
- Xây dựng kế hoạch triển khai CP2 và E2.
- Viết prompt cho Codex và hướng dẫn quy trình Git, Pull Request.
- Hỗ trợ tổng hợp báo cáo cá nhân.

### OpenAI Codex

- Đọc tài liệu Markdown, source code và rubric của Lab 13.
- Hỗ trợ triển khai `chay_B()` và hoàn thiện bảng chi phí B1–B4.
- Phát hiện yêu cầu bổ sung về hai mức thời gian làm lại và ngưỡng hòa vốn B4.
- Hỗ trợ phân tích 4 rủi ro kinh tế E2 từ số liệu A/B.
- Chạy chương trình, kiểm tra công thức, tính toán độc lập từ CSV và kiểm tra sai số.
- Kiểm tra nhãn `simulated`, phạm vi thay đổi và cập nhật báo cáo cá nhân.

### Kiểm soát kết quả AI

Tôi giới hạn phạm vi chỉnh sửa của AI theo nhiệm vụ được phân công, yêu cầu giữ nguyên contract của M1 và không thay đổi dữ liệu gốc.

Tôi sử dụng kết quả chạy chương trình, phép tính đối chiếu và báo cáo kiểm tra của Codex để đánh giá tính chính xác của kết quả. Các ngưỡng đề xuất được phân biệt rõ với số liệu quan sát và kết quả giả lập.

## 6. Tự đánh giá

Tôi đã hoàn thành toàn bộ phần việc chuyên môn được phân công cho M2, bao gồm CP2 (B1–B4) và E2, với kết quả đáp ứng tiêu chí sai số và yêu cầu rubric đã kiểm tra.

Qua bài lab, tôi hiểu rõ hơn sự khác biệt giữa chi phí sử dụng mô hình AI, chi phí mỗi việc thành công và tổng chi phí vận hành hệ thống.

Kết quả phân tích cho thấy tối ưu giá token không phải yếu tố quan trọng nhất. Giảm lỗi, thời gian xem lại và chi phí làm lại có thể mang lại hiệu quả kinh tế lớn hơn.

Tôi cũng nhận ra CPS thấp nhất không đồng nghĩa với tổng chi phí hệ thống thấp nhất. Việc giới hạn chạy lại cần xem xét cả số yêu cầu thất bại và chi phí chuyển sang nhân viên xử lý.

Thông qua E2, tôi hiểu rằng kết luận kinh tế cần ghi rõ phạm vi, mẫu số, chi phí cố định và giả định đầu vào. Các ngưỡng 7%/50%/15% mới là đề xuất, chưa được kiểm chứng bằng Pilot có đối chứng. Dữ liệu `_simulated` cần được thay bằng dữ liệu đo thực tế trước khi đưa ra quyết định triển khai.

Tôi đã cải thiện kỹ năng phối hợp nhóm, sử dụng contract chung, phân tích độ nhạy, đánh giá rủi ro và sử dụng AI trong quy trình phát triển phần mềm.

Điểm cần cải thiện là tăng khả năng kiểm chứng độc lập kết quả do AI tạo ra và nâng cao kỹ năng xác định ngưỡng dựa trên dữ liệu thực tế.

Phần việc chuyên môn M2 đã hoàn thành. Công việc còn lại là phối hợp bàn giao, giải thích công thức, rà soát E3 do M4 tổng hợp và kiểm tra Gate 2a cùng nhóm. Tôi không ghi nhận đã triển khai hoặc kiểm thử nhiệm vụ D, E1 và E3 của các thành viên khác.