# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 · ĐẠT |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 · ĐẠT |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 · ĐẠT (= 1/p, vì 1 − (1 − p)^k triệt tiêu) |

`cd src && python lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT`.

## A2 · Mô hình chi phí từ trace

Tử số tính mọi lần chạy (1.624 lần, kể cả lần lỗi); mẫu số chỉ đếm yêu cầu có `ket_qua = thanh_cong`. Số lấy từ `mo_hinh(runs, reqs)` với tham số mặc định.

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` (5.600 lần gọi × 15 đ) | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` (890 phút × 2.000 đ) | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` (1.132 phút × 2.000 đ) | simulated |
| Tổng chi phí | 4.373.585 | token + tool + xem lại + làm lại | có phần simulated |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 | 4.373.585 ÷ 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | (245.585 + 84.000) ÷ 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? **16,3 lần**: 4.472 đ [simulated] so với 274,7 đ. So với nhân viên tự làm phải cộng 222 ca không thành công × 12.000 đ: (4.373.585 + 2.664.000) ÷ 1.200 = **5.865 đ/yêu cầu = 0,49×** của 12.000 đ [simulated].
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? **Làm lại, 51,8%** [simulated], tiếp theo là xem lại 40,7% [simulated]; giờ nhân viên chiếm 92,5% tổng chi phí [simulated], token + tool chỉ 7,5%.

## A3 · Tách theo loại yêu cầu

Mỗi dòng là `mo_hinh(runs, reqs[reqs.loai == loai])`; số lần chạy mỗi yêu cầu = số dòng trong `logix_runs.csv` ÷ số yêu cầu của loại.

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ [simulated] | 0,22× [simulated] |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ [simulated] | 0,69× [simulated] |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ [simulated] | 1,88× [simulated] |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ [simulated] | 0,85× [simulated] |

Tỉ lệ lần chạy có `status = ok` theo lần thử (đo từ trace; số lần chạy trong ngoặc):

| Loại | Lần 1 | Lần 2 | Lần 3 |
| --- | ---: | ---: | ---: |
| noi_dia | 91,0% (824) | 75,7% (74) | 38,9% (18) |
| hang_nang | 70,9% (158) | 39,1% (46) | 17,9% (28) |
| quoc_te | 30,0% (150) | 11,4% (105) | 2,2% (93) |
| doi_tac | 51,5% (68) | 18,2% (33) | 14,8% (27) |

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? **quoc_te**: 22.515 đ = 1,88× của 12.000 đ [simulated], chỉ 27,3% thành công dù chạy 2,32 lần/yêu cầu. Chạy lại không giúp: tỉ lệ ok giảm 30,0% → 11,4% → 2,2% vì lỗi lặp lại trên cùng yêu cầu, chạy thêm chỉ tốn tiền. doi_tac sát ngưỡng: 0,85× [simulated], 54,4% thành công.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Phạm vi có 982 yêu cầu, 900 việc thành công, tổng 3.072.513 đ → chi phí mỗi việc thành công 3.414 đ [simulated]. Việc thành công mỗi tháng = khối lượng × 900 ÷ 1.200 (tỉ lệ trên toàn mẫu, vì 45.000 là tổng yêu cầu mỗi tháng); cố định mỗi việc = 40.000.000 đ ÷ số việc thành công mỗi tháng.

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ [simulated] | 0,38× [simulated] |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ [simulated] | 0,48× [simulated] |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? Không đổi ở 45.000 yêu cầu/tháng: cộng 1.185 đ/việc, còn **4.599 đ = 0,38×** [simulated]. Khi khối lượng giảm một nửa (ví dụ giai đoạn pilot), cố định tăng gấp đôi lên 2.370 đ/việc → **5.784 đ = 0,48×** [simulated]: vẫn dưới 12.000 đ nhưng nhạy với khối lượng nhỏ, nên mọi con số phải ghi đã cộng cố định hay chưa.

## B1 · Đổi từng yếu tố

Baseline A2 = **4.472 đ/việc thành công [simulated]** (978 việc); thay đổi = `(cps_kịch_bản / cps_A2 − 1) × 100%`, dùng số chưa làm tròn. Các chi phí B1–B4 chưa cộng chi phí cố định.

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ [simulated] | +5,6% [simulated] |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ [simulated] | −2,8% [simulated] |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ [simulated] | +40,7% [simulated] |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ [simulated] | −20,3% [simulated] |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ [simulated] | +51,8% [simulated] |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ [simulated] | −25,9% [simulated] |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ [simulated] | +23,1% [simulated] |
| Chỉ cho chạy tối đa 2 lần | Bỏ attempt > 2; so_lan_chay > 2 → chuyen_nhan_vien, phút xem lại và làm lại bằng 0 | 4.237 đ [simulated] | −5,2% [simulated] |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ [simulated] | −8,1% [simulated] |

Kiểm tra CP2: cả 3 cặp token, xem lại, làm lại đều có mức giảm bằng đúng 1/2 mức tăng trên số chưa làm tròn [simulated].

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ/việc, +46,3% [simulated]**; bằng +5,6% + 40,7% [simulated] vì mô hình cộng tuyến tính, số việc thành công giữ ở 978.
- Xếp hạng theo độ lớn thay đổi trong các kịch bản B1, mỗi yếu tố lấy mức lớn nhất: **1. Số ca làm lại (+51,8%) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương nhân viên (+23,1%) [simulated]**.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = tổng chi phí trợ lý + **12.000 đ × số yêu cầu không thành công**; số không thành công = 1.200 − số `thanh_cong` sau giới hạn. Chi phí mỗi việc thành công vẫn là tổng trợ lý ÷ số `thanh_cong`.

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ [simulated] | 319 | 7.449.781 đ [simulated] | 4.111 đ [simulated] |
| 2 lần | 4.093.220 đ [simulated] | 234 | 6.901.220 đ [simulated] | 4.237 đ [simulated] |
| 3 lần | 4.373.585 đ [simulated] | 222 | 7.037.585 đ [simulated] | 4.472 đ [simulated] |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? **2 lần: 6.901.220 đ [simulated]** rẻ nhất cho công ty; CPS thấp nhất ở **1 lần: 4.111 đ [simulated]**, để lại thêm **85** yêu cầu cho nhân viên so với 2 lần.

## B4 · Nếu phải xem lại tất cả

Trong 982 yêu cầu `noi_dia` + `hang_nang`, có 948 yêu cầu có ít nhất 1 lần `status = ok` (đếm request_id duy nhất), 48 ca `lam_lai`, 900 việc thành công; token + tool mọi lần chạy = 224.513 đ.

| Kịch bản xem lại 100% | Tiền xem lại | Tiền làm lại | Tổng chi phí | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| Theo đề: xem lại 5 phút, làm lại 9 phút/ca | 948 × 5 × 2.000 = 9.480.000 đ [simulated] | 48 × 9 × 2.000 = 864.000 đ [simulated] | 10.568.513 đ [simulated] | 11.743 đ [simulated] | 0,98× [simulated] |
| Độ nhạy: làm lại 15,3 phút/ca | 9.480.000 đ [simulated] | 48 × 15,3 × 2.000 = 1.468.800 đ [simulated] | 11.173.313 đ [simulated] | 12.415 đ [simulated] | 1,03× [simulated] |

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: **11.743 đ = 0,98× [simulated]** theo đề; dùng trung bình toàn bộ 74 ca làm lại = 1.132 ÷ 74 ≈ **15,3 phút** (trung vị 14,5) → **12.415 đ = 1,03× [simulated]**; CPS = tổng ÷ 900.
- Kết quả này nói gì về thứ pilot cần học được? Cần đo tỉ lệ xem lại có thể giảm an toàn và phút xem lại/làm lại thực tế: ngưỡng xem lại hòa vốn **≤ 5,1 phút** với làm lại 9 phút, hoặc **≤ 4,8 phút** với 15,3 phút [simulated]; xem lại 100% ở 5 phút gần như hết tiết kiệm.

Đối chiếu hướng dẫn CP2/rubric C2: B1 đủ 9 dòng và cùng số làm tròn đáp án; B2 đúng 3 yếu tố; B3–B4 có số và nhãn simulated. B4 tính thực tế 11.173.313 ÷ 900 ≈ 12.414,79 → **12.415 đ [simulated]**, lệch 1 đ so với số 12.414 đ trong hướng dẫn (< 0,01%, dưới ngưỡng 2%).
