import streamlit as st

st.set_page_config(page_title="Hóa Đơn Bán Hàng Nhà Diem", page_icon="🛒", layout="centered")

st.title("🛒 HÓA ĐƠN BÁN HÀNG NHÀ DIEM")
ngay = st.text_input("Ngày ghi hoá đơn:", "31/10/2026")

st.markdown("### Nhập số lượng các loại bánh (kg):")

# Sử dụng number_input để nhập liệu trực quan, hỗ trợ tăng giảm số lượng hoặc gõ trực tiếp
bbo = st.number_input("1. Bánh bò (45,000 đ)", min_value=0.0, step=0.1, format="%.1f")
bbo_nuong = st.number_input("2. Bánh bò nướng (130,000 đ)", min_value=0.0, step=0.1, format="%.1f")
bbo_chuoi = st.number_input("3. Bánh bò chuối hồng (50,000 đ)", min_value=0.0, step=0.1, format="%.1f")
bbo_bong = st.number_input("4. Bánh bò bông (55,000 đ)", min_value=0.0, step=0.1, format="%.1f")
bbo_da_lon = st.number_input("5. Bánh bò da lợn (65,000 đ)", min_value=0.0, step=0.1, format="%.1f")
banh_da_lon = st.number_input("6. Bánh da lợn (50,000 đ)", min_value=0.0, step=0.1, format="%.1f")
bbo_cot_dua = st.number_input("7. Bánh bò cốt dừa (60,000 đ)", min_value=0.0, step=0.1, format="%.1f")
bbo_thotnot = st.number_input("8. Bánh bò thốt nốt (65,000 đ)", min_value=0.0, step=0.1, format="%.1f")

# Danh sách dữ liệu
danh_sach = [
    ("Bánh bò", bbo, 45000),
    ("Bánh bò nướng", bbo_nuong, 130000),
    ("Bánh bò chuối hồng", bbo_chuoi, 50000),
    ("Bánh bò bông", bbo_bong, 55000),
    ("Bánh bò da lợn", bbo_da_lon, 65000),
    ("Bánh da lợn", banh_da_lon, 50000),
    ("Bánh bò cốt dừa", bbo_cot_dua, 60000),
    ("Bánh bò thốt nốt", bbo_thotnot, 65000)
]

# Xử lý tính toán và lọc bỏ món số lượng = 0
hoa_don_chi_tiet = []
tong_cong = 0

for ten, sl, dg in danh_sach:
    if sl > 0:
        thanh_tien = sl * dg
        tong_cong += thanh_tien
        hoa_don_chi_tiet.append((ten, sl, dg, thanh_tien))

# Nút bấm xuất hóa đơn
if st.button("IN HÓA ĐƠN", type="primary"):
    if not hoa_don_chi_tiet:
        st.warning("Vui lòng nhập số lượng ít nhất một loại bánh!")
    else:
        # Tạo khung hóa đơn thẳng tắp dùng font chữ cố định
        ket_qua = "="*65 + "\n"
        ket_qua += "                 HÓA ĐƠN BÁN HÀNG NHÀ DIEM\n"
        ket_qua += f"Ngày: {ngay}\n"
        ket_qua += "="*65 + "\n"
        
        stt = 1
        for ten, sl, dg, tt in hoa_don_chi_tiet:
            ket_qua += f"{stt}. {ten.ljust(18)} | SL: {str(sl):<4} kg | ĐG: {dg:>7,.0f} | T.Tiền: {tt:>9,.0f} đ\n"
            stt += 1
            
        ket_qua += "="*65 + "\n"
        ket_qua += f"TỔNG CỘNG: {tong_cong:,.0f} VNĐ\n"
        ket_qua += "="*65
        
        st.code(ket_qua, language="text")
import streamlit as st

st.set_page_config(page_title="Hóa Đơn Bán Hàng Nhà Diem", page_icon="🛒", layout="centered")

st.title("🛒 HÓA ĐƠN BÁN HÀNG NHÀ DIEM")
ngay = st.text_input("Ngày ghi hoá đơn:", "31/10/2026")

st.markdown("### Nhập số lượng các loại bánh (kg):")

# Sử dụng number_input để nhập liệu trực quan, hỗ trợ tăng giảm số lượng hoặc gõ trực tiếp
bbo = st.number_input("1. Bánh bò (45,000 đ)", min_value=0.0, step=0.1, format="%.1f")
bbo_nuong = st.number_input("2. Bánh bò nướng (130,000 đ)", min_value=0.0, step=0.1, format="%.1f")
bbo_chuoi = st.number_input("3. Bánh bò chuối hồng (50,000 đ)", min_value=0.0, step=0.1, format="%.1f")
bbo_bong = st.number_input("4. Bánh bò bông (55,000 đ)", min_value=0.0, step=0.1, format="%.1f")
bbo_da_lon = st.number_input("5. Bánh bò da lợn (65,000 đ)", min_value=0.0, step=0.1, format="%.1f")
banh_da_lon = st.number_input("6. Bánh da lợn (50,000 đ)", min_value=0.0, step=0.1, format="%.1f")
bbo_cot_dua = st.number_input("7. Bánh bò cốt dừa (60,000 đ)", min_value=0.0, step=0.1, format="%.1f")
bbo_thotnot = st.number_input("8. Bánh bò thốt nốt (65,000 đ)", min_value=0.0, step=0.1, format="%.1f")

# Danh sách dữ liệu
danh_sach = [
    ("Bánh bò", bbo, 45000),
    ("Bánh bò nướng", bbo_nuong, 130000),
    ("Bánh bò chuối hồng", bbo_chuoi, 50000),
    ("Bánh bò bông", bbo_bong, 55000),
    ("Bánh bò da lợn", bbo_da_lon, 65000),
    ("Bánh da lợn", banh_da_lon, 50000),
    ("Bánh bò cốt dừa", bbo_cot_dua, 60000),
    ("Bánh bò thốt nốt", bbo_thotnot, 65000)
]

# Xử lý tính toán và lọc bỏ món số lượng = 0
hoa_don_chi_tiet = []
tong_cong = 0

for ten, sl, dg in danh_sach:
    if sl > 0:
        thanh_tien = sl * dg
        tong_cong += thanh_tien
        hoa_don_chi_tiet.append((ten, sl, dg, thanh_tien))

# Nút bấm xuất hóa đơn
if st.button("IN HÓA ĐƠN", type="primary"):
    if not hoa_don_chi_tiet:
        st.warning("Vui lòng nhập số lượng ít nhất một loại bánh!")
    else:
        # Tạo khung hóa đơn thẳng tắp dùng font chữ cố định
        ket_qua = "="*65 + "\n"
        ket_qua += "                 HÓA ĐƠN BÁN HÀNG NHÀ DIEM\n"
        ket_qua += f"Ngày: {ngay}\n"
        ket_qua += "="*65 + "\n"
        
        stt = 1
        for ten, sl, dg, tt in hoa_don_chi_tiet:
            ket_qua += f"{stt}. {ten.ljust(18)} | SL: {str(sl):<4} kg | ĐG: {dg:>7,.0f} | T.Tiền: {tt:>9,.0f} đ\n"
            stt += 1
            
        ket_qua += "="*65 + "\n"
        ket_qua += f"TỔNG CỘNG: {tong_cong:,.0f} VNĐ\n"
        ket_qua += "="*65
        
        st.code(ket_qua, language="text")
