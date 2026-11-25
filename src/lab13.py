"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.

Tổ chức file (để 4 người làm song song, mỗi người chỉ sửa vùng của mình):
    Vùng chung (M1) : hằng số, ba hàm A1, mo_hinh() — CONTRACT dùng chung, không đổi chữ ký/tên key.
    chay_A()  (M1)  : Nhiệm vụ A2, A3, A4.
    chay_B()  (M2)  : Nhiệm vụ B1–B4 — gọi lại mo_hinh().
    chay_D()  (M3)  : Nhiệm vụ D1 — cỡ mẫu.
    chay_E()  (M4)  : Nhiệm vụ E1 — tính thử ba chỉ số.
"""
import math
import sys
from statistics import NormalDist

import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)

# Số liệu dùng chung cho A4 (docs/du_lieu_va_cong_thuc.md)
CHI_PHI_CO_DINH_THANG = 40_000_000   # đồng mỗi tháng (vận hành, giám sát, cập nhật chính sách)
SO_YC_THANG = 45_000                 # yêu cầu hoàn phí mỗi tháng ở quy mô đầy đủ (1.500/ngày)
PHAM_VI_PILOT = ['noi_dia', 'hang_nang']
THU_TU_LOAI = ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']


# ---------- Định dạng số kiểu Việt Nam (1.234.567 · 4,5) ----------
def so(x, nd=0):
    """Định dạng số: dấu chấm ngăn nghìn, dấu phẩy thập phân."""
    s = f'{x:,.{nd}f}'
    return s.replace(',', '_').replace('.', ',').replace('_', '.')


def pt(x, nd=1):
    """Định dạng tỉ lệ (0..1) thành phần trăm."""
    return so(x * 100, nd) + '%'


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# CP1 (M1): ba hàm dưới đây; kiem_tra_dap_an_biet_truoc() phải in ĐẠT.
def _kiem_tra_p(p):
    if not 0 < p <= 1:
        raise ValueError(f'p phải nằm trong (0, 1], nhận được {p}')


def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng.
    Có giới hạn: E = 1 + (1-p) + ... + (1-p)^(k-1) = (1 - (1-p)^k) / p.
    Không giới hạn (k → ∞): E = 1 / p."""
    _kiem_tra_p(p)
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy: 1 - (1-p)^k; k=None → 1."""
    _kiem_tra_p(p)
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy:
    E[số lần chạy] / P(thành công). Với k hữu hạn, (1-(1-p)^k) triệt tiêu nên luôn bằng 1/p."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace (CONTRACT dùng chung) ----------
# Chữ ký và 9 key trả về là contract cho M2 (B), M4 (E). Không đổi tên tham số / tên key.
KEY_MO_HINH = ('token', 'tool', 'chay_lai', 'xem_lai', 'lam_lai',
               'tong', 'thanh_cong', 'cps', 'hoa_don_moi_yc')


def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL, luong_phut=LUONG_PHUT,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm đúng 9 key (KEY_MO_HINH), đơn vị đồng trừ thanh_cong (số yêu cầu):
    - token, tool: cộng trên MỌI lần chạy của các yêu cầu trong reqs, kể cả lần lỗi.
    - chay_lai: phần token + tool của các lần chạy có attempt > 1 (đã nằm trong token, tool).
    - xem_lai, lam_lai: số phút (cột *_simulated) × luong_phut × hệ số. Số GIẢ LẬP → nhãn simulated.
    - tong = token + tool + xem_lai + lam_lai.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - cps = tong / thanh_cong (chi phí mỗi việc thành công).
    - hoa_don_moi_yc = (token + tool) / số yêu cầu (con số "hoá đơn" để so sánh).
    Tham số cho Nhiệm vụ B (giữ mặc định ở A2):
    - gia_vao, gia_ra: đồng / 1.000 token; gia_tool: đồng / lần gọi; luong_phut: đồng / phút.
    - he_so_xem_lai, he_so_lam_lai: nhân vào tiền xem lại / làm lại.
    - max_lan_chay: bỏ các lần chạy có attempt > giới hạn; yêu cầu có so_lan_chay > giới hạn
      coi là chuyen_nhan_vien, phút xem lại và làm lại của yêu cầu đó bằng 0.
    reqs phải được đọc với keep_default_na=False. Hàm không sửa runs/reqs đầu vào.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    # Chia 1.000 trước khi nhân giá token
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    token = float(tien_token.sum())
    tool = float(tien_tool.sum())
    chay_lai = float((tien_token + tien_tool)[runs['attempt'] > 1].sum())

    xem_lai = float(reqs['phut_xem_lai_simulated'].sum()) * luong_phut * he_so_xem_lai
    lam_lai = float(reqs['phut_lam_lai_simulated'].sum()) * luong_phut * he_so_lam_lai
    tong = token + tool + xem_lai + lam_lai

    # Mẫu số chỉ đếm việc thành công
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    cps = tong / thanh_cong if thanh_cong else float('inf')
    hoa_don_moi_yc = (token + tool) / len(reqs) if len(reqs) else float('nan')

    return dict(token=token, tool=tool, chay_lai=chay_lai, xem_lai=xem_lai, lam_lai=lam_lai,
                tong=tong, thanh_cong=thanh_cong, cps=cps, hoa_don_moi_yc=hoa_don_moi_yc)


# ---------- Nhiệm vụ A · Báo cáo A2, A3, A4 (M1) ----------
def ti_le_ok_theo_lan(runs, reqs):
    """Tỉ lệ lần chạy có status ok, theo loại yêu cầu × attempt (để trả lời 'chạy lại có giúp không')."""
    ghep = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    ghep = ghep.assign(ok=(ghep['status'] == 'ok').astype(float))
    bang = ghep.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean')
    so_lan = ghep.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='size')
    return bang.reindex(THU_TU_LOAI), so_lan.reindex(THU_TU_LOAI)


def chay_A(runs, reqs):
    """In bảng A2, A3, A4 và trả về kết quả để các phần sau dùng lại:
    {'A2': dict mo_hinh, 'A2_phu': dict chỉ số phụ, 'A3': DataFrame theo loại,
     'ok_theo_lan': DataFrame, 'A4': list[dict], 'A4_pham_vi': dict mo_hinh phạm vi pilot}."""
    # ---- A2 ----
    a2 = mo_hinh(runs, reqs)
    khong_thanh_cong = len(reqs) - a2['thanh_cong']
    # Chi phí cả hệ thống mỗi yêu cầu: cộng 12.000 đ cho mỗi ca nhân viên phải làm thay
    he_thong_moi_yc = (a2['tong'] + khong_thanh_cong * BASELINE) / len(reqs)
    a2_phu = dict(
        so_yeu_cau=len(reqs),
        so_lan_chay=len(runs[runs['request_id'].isin(reqs['request_id'])]),
        so_lan_goi_tool=int(runs['tool_calls'].sum()),
        phut_xem_lai=float(reqs['phut_xem_lai_simulated'].sum()),
        phut_lam_lai=float(reqs['phut_lam_lai_simulated'].sum()),
        cps_gap_hoa_don=a2['cps'] / a2['hoa_don_moi_yc'],
        ti_trong_lam_lai=a2['lam_lai'] / a2['tong'],
        ti_trong_xem_lai=a2['xem_lai'] / a2['tong'],
        ti_trong_nhan_vien=(a2['xem_lai'] + a2['lam_lai']) / a2['tong'],
        khong_thanh_cong=khong_thanh_cong,
        he_thong_moi_yc=he_thong_moi_yc,
        he_thong_so_voi_baseline=he_thong_moi_yc / BASELINE,
    )

    print('\n=== A2 · Mô hình chi phí từ trace (1.200 yêu cầu) ===')
    dong_a2 = [
        ('Token (mọi lần chạy)', so(a2['token']), 'đ', 'đo từ trace'),
        (f"Tool ({so(a2_phu['so_lan_goi_tool'])} lần gọi)", so(a2['tool']), 'đ', 'đo từ trace'),
        ('Trong đó, lần chạy thứ 2 và 3', so(a2['chay_lai']), 'đ', 'đo từ trace'),
        (f"Xem lại ({so(a2_phu['phut_xem_lai'])} phút)", so(a2['xem_lai']), 'đ', 'simulated'),
        (f"Làm lại ({so(a2_phu['phut_lam_lai'])} phút)", so(a2['lam_lai']), 'đ', 'simulated'),
        ('Tổng chi phí', so(a2['tong']), 'đ', 'có phần simulated'),
        ('Số việc thành công', so(a2['thanh_cong']), 'yc', ''),
        ('Chi phí mỗi việc thành công', so(a2['cps']), 'đ', 'simulated'),
        ('Hoá đơn token + tool / số yêu cầu', so(a2['hoa_don_moi_yc'], 1), 'đ', 'đo từ trace'),
    ]
    for ten, gia_tri, don_vi, nhan in dong_a2:
        print(f'{ten:36s} {gia_tri:>12s} {don_vi:2s}  {nhan}')
    print(f"Chi phí mỗi việc thành công gấp {so(a2_phu['cps_gap_hoa_don'], 1)} lần hoá đơn / yêu cầu [simulated]")
    print(f"Tỉ trọng: làm lại {pt(a2_phu['ti_trong_lam_lai'])}, xem lại {pt(a2_phu['ti_trong_xem_lai'])}, "
          f"giờ nhân viên {pt(a2_phu['ti_trong_nhan_vien'])} [simulated]")
    print(f"Cả hệ thống (cộng {khong_thanh_cong} ca không thành công × 12.000 đ): "
          f"{so(he_thong_moi_yc)} đ/yêu cầu = {so(a2_phu['he_thong_so_voi_baseline'], 2)}× baseline [simulated]")

    # ---- A3 ----
    dong = []
    for loai in THU_TU_LOAI:
        con = reqs[reqs['loai'] == loai]
        m = mo_hinh(runs, con)
        so_lan_chay = len(runs[runs['request_id'].isin(con['request_id'])])
        dong.append(dict(loai=loai, so_yeu_cau=len(con), thanh_cong=m['thanh_cong'],
                         ti_le_thanh_cong=m['thanh_cong'] / len(con),
                         lan_chay_moi_yc=so_lan_chay / len(con),
                         cps=m['cps'], so_voi_baseline=m['cps'] / BASELINE))
    a3 = pd.DataFrame(dong).set_index('loai')

    print('\n=== A3 · Tách theo loại yêu cầu ===')
    print(f"{'Loại':10s} {'Số yc':>6s} {'Thành công':>11s} {'Lần chạy/yc':>12s} {'CPS [sim]':>10s} {'So 12.000':>10s}")
    for loai, r in a3.iterrows():
        print(f"{loai:10s} {r.so_yeu_cau:>6.0f} {pt(r.ti_le_thanh_cong):>11s} {so(r.lan_chay_moi_yc, 2):>12s} "
              f"{so(r.cps):>10s} {so(r.so_voi_baseline, 2) + '×':>10s}")

    ok_lan, so_lan = ti_le_ok_theo_lan(runs, reqs)
    print('\nTỉ lệ lần chạy ok theo attempt (số lần chạy trong ngoặc):')
    for loai in THU_TU_LOAI:
        o = ', '.join(f'lần {int(a)}: {pt(ok_lan.loc[loai, a])} ({int(so_lan.loc[loai, a])})'
                      for a in ok_lan.columns if not pd.isna(ok_lan.loc[loai, a]))
        print(f'  {loai:10s} {o}')

    # ---- A4 · Chi phí cố định, phạm vi noi_dia + hang_nang ----
    pv = reqs[reqs['loai'].isin(PHAM_VI_PILOT)]
    a4_pv = mo_hinh(runs, pv)
    # Tỉ lệ việc thành công trong phạm vi so với TOÀN BỘ mẫu, vì 45.000 là tổng số yêu cầu mỗi tháng
    ti_le_tc_pham_vi = a4_pv['thanh_cong'] / len(reqs)
    a4 = []
    for ten, khoi_luong in [('45.000 yêu cầu/tháng', SO_YC_THANG), ('Một nửa khối lượng', SO_YC_THANG / 2)]:
        viec_tc_thang = khoi_luong * ti_le_tc_pham_vi
        co_dinh_moi_viec = CHI_PHI_CO_DINH_THANG / viec_tc_thang
        tong_moi_viec = a4_pv['cps'] + co_dinh_moi_viec
        a4.append(dict(khoi_luong=ten, so_yc_thang=khoi_luong, viec_tc_thang=viec_tc_thang,
                       co_dinh_moi_viec=co_dinh_moi_viec, cps_pham_vi=a4_pv['cps'],
                       cps_cong_co_dinh=tong_moi_viec, so_voi_baseline=tong_moi_viec / BASELINE))

    print(f"\n=== A4 · Chi phí cố định, phạm vi {' + '.join(PHAM_VI_PILOT)} ===")
    print(f"Phạm vi: {so(len(pv))} yêu cầu, {so(a4_pv['thanh_cong'])} việc thành công / {so(len(reqs))} yêu cầu của mẫu; "
          f"tổng {so(a4_pv['tong'])} đ → CPS {so(a4_pv['cps'])} đ [simulated]")
    for r in a4:
        print(f"{r['khoi_luong']:22s} việc TC/tháng {so(r['viec_tc_thang']):>7s} · cố định {so(r['co_dinh_moi_viec'])} đ/việc"
              f" · CPS + cố định {so(r['cps_cong_co_dinh'])} đ = {so(r['so_voi_baseline'], 2)}× [simulated]")

    return {'A2': a2, 'A2_phu': a2_phu, 'A3': a3, 'ok_theo_lan': ok_lan, 'A4': a4, 'A4_pham_vi': a4_pv}


# ---------- Nhiệm vụ B · Bảng độ nhạy (M2) ----------
def chay_B(runs, reqs):
    """CP2: in B1–B4 và trả kết quả; mọi chi phí có giờ nhân viên mang nhãn simulated.
    Tái sử dụng mo_hinh(), chỉ thay phút B4 trên bản sao, không sửa dữ liệu đầu vào.
    """
    goc = mo_hinh(runs, reqs)
    kich_ban = [
        ('Giá token gấp đôi', 'Giá token', dict(gia_vao=GIA_VAO * 2, gia_ra=GIA_RA * 2)),
        ('Giá token giảm một nửa', 'Giá token', dict(gia_vao=GIA_VAO / 2, gia_ra=GIA_RA / 2)),
        ('Tỉ lệ xem lại gấp đôi', 'Tỉ lệ xem lại', dict(he_so_xem_lai=2)),
        ('Tỉ lệ xem lại giảm một nửa', 'Tỉ lệ xem lại', dict(he_so_xem_lai=0.5)),
        ('Số ca làm lại gấp đôi', 'Số ca làm lại', dict(he_so_lam_lai=2)),
        ('Số ca làm lại giảm một nửa', 'Số ca làm lại', dict(he_so_lam_lai=0.5)),
        ('Lương nhân viên tăng 25%', 'Lương nhân viên', dict(luong_phut=LUONG_PHUT * 1.25)),
        ('Chỉ cho chạy tối đa 2 lần', 'Giới hạn chạy', dict(max_lan_chay=2)),
        ('Chỉ cho chạy 1 lần', 'Giới hạn chạy', dict(max_lan_chay=1)),
    ]
    b1 = []
    anh_huong = {}
    print('\n=== B1 · Đổi từng yếu tố ===')
    print(f"Gốc A2: {so(goc['cps'])} đ/việc thành công [simulated]; chưa cộng chi phí cố định.")
    for ten, yeu_to, tham_so in kich_ban:
        m = mo_hinh(runs, reqs, **tham_so)
        thay_doi = m['cps'] / goc['cps'] - 1
        b1.append(dict(kich_ban=ten, yeu_to=yeu_to, tham_so=tham_so,
                       mo_hinh=m, thay_doi=thay_doi))
        # Mỗi yếu tố lấy biến động tuyệt đối lớn nhất trong các kịch bản B1 của nó.
        if yeu_to not in anh_huong or abs(thay_doi) > abs(anh_huong[yeu_to]):
            anh_huong[yeu_to] = thay_doi
        dau = '+' if thay_doi >= 0 else ''
        print(f"{ten:30s} {so(m['cps']):>8s} đ  {dau}{pt(thay_doi)} [simulated]")

    cap = mo_hinh(runs, reqs, gia_vao=GIA_VAO * 2, gia_ra=GIA_RA * 2, he_so_xem_lai=2)
    thay_doi_cap = cap['cps'] / goc['cps'] - 1
    xep_hang = sorted(anh_huong.items(), key=lambda muc: abs(muc[1]), reverse=True)[:3]
    print('\n=== B2 · Đổi một cặp và xếp hạng ===')
    print(f"Token và xem lại cùng gấp đôi: {so(cap['cps'])} đ, +{pt(thay_doi_cap)} [simulated].")
    print(f"Tác động cặp = {pt(b1[0]['thay_doi'])} + {pt(b1[2]['thay_doi'])} "
          f"= {pt(thay_doi_cap)} vì mô hình cộng tuyến tính [simulated].")
    print(' · '.join(f'{i}. {ten}: {pt(muc)}' for i, (ten, muc) in enumerate(xep_hang, 1))
          + ' [simulated; theo mức thay đổi của các kịch bản B1].')

    b3 = []
    print('\n=== B3 · Giới hạn chạy lại ===')
    print('Giới hạn | Tổng trợ lý [simulated] | Không thành công | Cả hệ thống [simulated] | CPS [simulated]')
    for k in (1, 2, 3):
        m = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_thanh_cong = len(reqs) - m['thanh_cong']
        he_thong = m['tong'] + BASELINE * khong_thanh_cong
        b3.append(dict(gioi_han=k, mo_hinh=m, khong_thanh_cong=khong_thanh_cong,
                       he_thong=he_thong))
        print(f"{k} lần | {so(m['tong'])} đ | {so(khong_thanh_cong)} | "
              f"{so(he_thong)} đ | {so(m['cps'])} đ")
    re_nhat = min(b3, key=lambda dong: dong['he_thong'])
    cps_thap_nhat = min(b3, key=lambda dong: dong['mo_hinh']['cps'])
    chenh_ca = cps_thap_nhat['khong_thanh_cong'] - re_nhat['khong_thanh_cong']
    print(f"Cả hệ thống rẻ nhất: {re_nhat['gioi_han']} lần, {so(re_nhat['he_thong'])} đ; "
          f"CPS thấp nhất: {cps_thap_nhat['gioi_han']} lần, "
          f"{so(cps_thap_nhat['mo_hinh']['cps'])} đ [simulated].")
    print(f"Giới hạn CPS thấp nhất để lại thêm {so(chenh_ca)} yêu cầu cho nhân viên.")

    # B4: xem lại mọi yêu cầu có ít nhất một run ok, không đếm lặp request_id.
    pv = reqs[reqs['loai'].isin(PHAM_VI_PILOT)].copy()
    co_ok = pv['request_id'].isin(runs.loc[runs['status'] == 'ok', 'request_id'])
    lam_lai = pv['ket_qua'] == 'lam_lai'
    phut_lam_lai = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated']
    # Hướng dẫn B4 dùng trung bình toàn bộ ca lam_lai, làm tròn 1 chữ số: 15,3 phút.
    trung_binh_lam_lai = round(float(phut_lam_lai.mean()), 1)
    b4 = []
    print(f"\n=== B4 · Xem lại 100%, {' + '.join(PHAM_VI_PILOT)} ===")
    print(f"{so(len(pv))} yêu cầu; {so(co_ok.sum())} có run ok × 5 phút xem lại; "
          f"{so(lam_lai.sum())} ca làm lại.")
    print(f"Phút làm lại toàn mẫu: trung bình {so(trung_binh_lam_lai, 1)}, "
          f"trung vị {so(phut_lam_lai.median(), 1)} [simulated].")
    for ten, phut in [('Theo đề', 9), ('Theo trung bình dữ liệu (làm tròn 1 chữ số)', trung_binh_lam_lai)]:
        pv['phut_xem_lai_simulated'] = co_ok.astype(float) * 5
        pv['phut_lam_lai_simulated'] = lam_lai.astype(float) * phut
        m = mo_hinh(runs, pv)
        hoa_von_phut = ((BASELINE * m['thanh_cong'] - m['token'] - m['tool'] - m['lam_lai'])
                        / (int(co_ok.sum()) * LUONG_PHUT))
        b4.append(dict(kich_ban=ten, phut_lam_lai=phut, mo_hinh=m,
                       so_voi_baseline=m['cps'] / BASELINE, hoa_von_phut=hoa_von_phut))
        print(f"{ten}: làm lại {so(phut, 1)} phút/ca; token + tool {so(m['token'] + m['tool'])} đ; "
              f"xem lại {so(m['xem_lai'])} đ; làm lại {so(m['lam_lai'])} đ [simulated].")
        print(f"Tổng {so(m['tong'])} đ / {so(m['thanh_cong'])} việc = {so(m['cps'])} đ "
              f"= {so(m['cps'] / BASELINE, 2)}× {so(BASELINE)} đ; "
              f"xem lại hòa vốn ≤ {so(hoa_von_phut, 1)} phút [simulated].")

    return {'goc_A2': goc, 'B1': b1,
            'B2': dict(mo_hinh=cap, thay_doi=thay_doi_cap, xep_hang=xep_hang),
            'B3': b3, 'B4': b4}


# ---------- Nhiệm vụ D · Cỡ mẫu và kế hoạch pilot (M3) ----------
# TODO CP4 · Nhiệm vụ D (M3): D1 năm câu cỡ mẫu; D3 tỉ lệ mở lại hiện tại trước khi đặt luật an toàn.
ICC_MAC_DINH = 0.02
BASELINE_PILOT = 0.70
MDE_PILOT = 0.05
MDE_CHAP_NHAN = 0.06


def _so_vn(x, nd=0):
    """Định dạng số kiểu Việt Nam (1.251 · 6,96) cho phần in của nhiệm vụ D."""
    s = f'{x:,.{nd}f}'
    return s.replace(',', '_').replace('.', ',').replace('_', '.')


def co_mau_hai_ti_le(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu MỖI NHÓM khi so hai tỉ lệ (công thức chuẩn, z lấy chính xác).
    Tương đương statsmodels.stats.power.NormalIndPower với effect_size = proportion_effectsize(p2, p1)."""
    if not (0 < p1 < 1 and 0 < p2 < 1):
        raise ValueError('p1, p2 phải nằm trong (0, 1)')
    if p1 == p2:
        raise ValueError('p1 và p2 phải khác nhau')
    z_alpha = NormalDist().inv_cdf(1 - alpha / 2)
    z_beta = NormalDist().inv_cdf(power)
    p_bar = (p1 + p2) / 2
    tu = (z_alpha * math.sqrt(2 * p_bar * (1 - p_bar))
          + z_beta * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2)))
    return math.ceil(tu ** 2 / (p2 - p1) ** 2)


def he_so_thiet_ke(m, icc=ICC_MAC_DINH):
    """Hệ số thiết kế khi chia theo cụm: DE = 1 + (m - 1) × ICC."""
    return 1 + (m - 1) * icc


def co_mau_hieu_dung(c, m, icc=ICC_MAC_DINH):
    """Cỡ mẫu hiệu dụng khi chia theo cụm: c × m / DE, luôn nhỏ hơn c / ICC."""
    return c * m / he_so_thiet_ke(m, icc)


def so_yeu_cau_moi_cum(n_hieu_dung, c, icc=ICC_MAC_DINH):
    """Số yêu cầu tối thiểu mỗi cụm để cỡ mẫu hiệu dụng đạt n_hieu_dung.
    Giải c × m / (1 + (m - 1) × ICC) ≥ n  →  m ≥ n(1 - ICC) / (c - n × ICC).
    Câu e: 859 × 0,98 / (20 - 859 × 0,02) = 298,5 → 299."""
    if n_hieu_dung * icc >= c:
        raise ValueError('Số cụm quá ít so với cỡ mẫu hiệu dụng cần có')
    return math.ceil(n_hieu_dung * (1 - icc) / (c - n_hieu_dung * icc))


def chay_D():
    """D1 · In năm câu cỡ mẫu và trả về dict để đối chiếu."""
    n_5_diem = co_mau_hai_ti_le(BASELINE_PILOT, BASELINE_PILOT + MDE_PILOT)
    n_6_diem = co_mau_hai_ti_le(BASELINE_PILOT, BASELINE_PILOT + MDE_CHAP_NHAN)
    de_75 = he_so_thiet_ke(75)
    n_theo_75 = math.ceil(n_5_diem * de_75)
    nguoi_moi_nhom = math.ceil(n_theo_75 / 75)
    toi_da_20_nguoi = 20 / ICC_MAC_DINH
    toi_da_6_depot = 6 / ICC_MAC_DINH
    m_6_diem = so_yeu_cau_moi_cum(n_6_diem, 20)
    de_6_diem = he_so_thiet_ke(m_6_diem)

    print('\n=== D1 · Cỡ mẫu (baseline 0,70; +5 điểm; alpha 0,05; power 0,8; ICC 0,02) ===')
    print(f'a) Chia theo yêu cầu: {_so_vn(n_5_diem)} yêu cầu mỗi nhóm')
    print(f'b) Theo nhân viên, m = 75: DE = {_so_vn(de_75, 2)}; {_so_vn(n_theo_75)} yêu cầu mỗi nhóm '
          f'= {nguoi_moi_nhom} người mỗi nhóm → cần {2 * nguoi_moi_nhom} người > 40: không đủ người')
    print(f'c) 20 nhân viên mỗi nhóm: tối đa {_so_vn(toi_da_20_nguoi)} < {_so_vn(n_5_diem)}: không đạt mức chênh 5 điểm')
    print(f'd) 6 depot mỗi nhóm: tối đa {_so_vn(toi_da_6_depot)}: loại')
    print(f'e) Mức chênh 6 điểm ({_so_vn(n_6_diem)} mỗi nhóm), 20 nhân viên mỗi nhóm: '
          f'm ≥ {m_6_diem} yêu cầu mỗi người (DE = {_so_vn(de_6_diem, 2)}; '
          f'{_so_vn(20 * m_6_diem)} yêu cầu mỗi nhóm; power ở mức 5 điểm còn 0,64)')
    return dict(n_5_diem=n_5_diem, n_6_diem=n_6_diem, de_75=de_75, n_theo_75=n_theo_75,
                nguoi_moi_nhom=nguoi_moi_nhom, toi_da_20_nguoi=toi_da_20_nguoi,
                toi_da_6_depot=toi_da_6_depot, m_6_diem=m_6_diem, de_6_diem=de_6_diem)


def ti_le_mo_lai(reqs, loai=None):
    """Tỉ lệ yêu cầu mở lại trong 7 ngày (mo_lai_trong_7_ngay = 1) của đợt chạy thử.
    Trả về (số ca, tổng số yêu cầu, tỉ lệ)."""
    du_lieu = reqs if loai is None else reqs[reqs['loai'].isin(loai)]
    so_ca = int((du_lieu['mo_lai_trong_7_ngay'] == 1).sum())
    return so_ca, len(du_lieu), so_ca / len(du_lieu)


def chay_D3(reqs):
    """D3 · In tỉ lệ mở lại hiện tại (toàn mẫu và phạm vi pilot) trước khi chốt ngưỡng an toàn."""
    ca, tong, ti_le = ti_le_mo_lai(reqs)
    ca_pv, tong_pv, ti_le_pv = ti_le_mo_lai(reqs, ['noi_dia', 'hang_nang'])
    print('\n=== D3 · Tỉ lệ mở lại trong 7 ngày của đợt chạy thử (dữ liệu giả lập) ===')
    print(f'Toàn mẫu: {ca}/{tong} = {_so_vn(ti_le * 100, 2)}%')
    print(f'Phạm vi noi_dia + hang_nang: {ca_pv}/{tong_pv} = {_so_vn(ti_le_pv * 100, 2)}%')
    print('Ngưỡng tuyệt đối 3% sẽ dừng pilot ngay tuần đầu → dùng chênh +2 điểm so với đối chứng, kèm trần 6%')
    return dict(ca=ca, tong=tong, ti_le=ti_le, ca_pv=ca_pv, tong_pv=tong_pv, ti_le_pv=ti_le_pv)


# ---------- Nhiệm vụ E · Tính thử chỉ số (M4) ----------
def chay_E(reqs):
    """TODO CP5 · Nhiệm vụ E1 (M4): tính thử chỉ số chính, tỉ lệ bỏ qua gợi ý, tỉ lệ lỗi lọt đến khách."""
    print('\n=== E1 · Chỉ số: chưa làm (M4 phụ trách, TODO CP5) ===')
    return None


# ---------- Nhiệm vụ E1 · Đặc tả chỉ số (Member 4) ----------
def tinh_chi_so_e1(reqs):
    """Tính thử ba chỉ số E1 trên mẫu 1.200 yêu cầu (đọc bằng keep_default_na=False)."""
    chinh_num = int(((reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)).sum())
    xem = reqs[reqs['duoc_xem_lai'] == 1]
    bo_qua_num = int(xem['quyet_dinh_xem_lai'].isin(['sua', 'bo']).sum())
    an_toan_num = int((reqs['mo_lai_trong_7_ngay'] == 1).sum())
    return dict(
        chinh_num=chinh_num,
        chinh=chinh_num / len(reqs),
        bo_qua_num=bo_qua_num,
        xem_num=len(xem),
        bo_qua=bo_qua_num / len(xem),
        an_toan_num=an_toan_num,
        an_toan=an_toan_num / len(reqs),
    )


if __name__ == '__main__':
    # In được tiếng Việt cả khi stdout là pipe trên Windows (mặc định cp1252)
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua_A = chay_A(runs, reqs)
    ket_qua_B = chay_B(runs, reqs)
    ket_qua_D = chay_D()
    ket_qua_D3 = chay_D3(reqs)
    ket_qua_E = chay_E(reqs)
