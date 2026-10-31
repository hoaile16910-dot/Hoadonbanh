import streamlit as st

st.set_page_config(page_title="Hóa Đơn Bán Hàng Nhà Diem", page_icon="🛒", layout="centered")

st.title("🛒 HÓA ĐƠN BÁN HÀNG NHÀ DIEM")
ngay = st.text_input("Ngày ghi hoá đơn:", "31/10/2026")

st.markdown("### Nhập số lượng các loại bánh (kg):")

# Thêm key riêng biệt cho từng ô để tránh hoàn toàn lỗi trùng lặp ID
bbo = st.number_input("1. Bánh bò (45,000 đ)", min_value=0.0, step=0.1, format="%.1f", key="bbo")
bbo_nuong = st.number_input("2. Bánh bò nướng (130,000 đ)", min_value=0.0, step=0.1, format="%.1f", key="bbo_nuong")
bbo_chuoi = st.number_input("3. Bánh bò chuối hồng (50,000 đ)", min_value=0.0, step=0.1, format="%.1f", key="bbo_chuoi")
bbo_bong = st.number_input("4. Bánh bò bông (55,000 đ)", min_value=0.0, step=0.1, format="%.1f", key="bbo_bong")
bbo_da_lon = st.number_input("5. Bánh bò da lợn (65,000 đ)", min_value=0.0, step=0.1, format="%.1f", key="bbo_da_lon")
banh_da_lon = st.number_input("6. Bánh da lợn (50,000 đ)", min_value=0.0, step=0.1, format="%.1f", key="banh_da_lon")
bbo_cot_dua = st.number_input("7. Bánh bò cốt dừa (60,000 đ)", min_value=0.0, step=0.1, format="%.1f", key="bbo_cot_dua")
bbo_thotnot = st.number_input("8. Bánh bò thốt nốt (65,000 đ)", min_value=0.0, step=0.1, format="%.1f", key="bbo_thotnot")

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
        st.success("Hóa đơn đã được lập thành công!")
        st.markdown("---")
        st.markdown(f"### 🧾 HÓA ĐƠN BÁN HÀNG")
        st.markdown(f"**Ngày:** {ngay}")
        st.markdown("---")
        
        # Dùng bảng trực quan của Streamlit thay vì khung chữ thô để không bị tràn màn hình điện thoại
        for idx, (ten, sl, dg, tt) in enumerate(hoa_don_chi_tiet, 1):
            st.markdown(f"**{idx}. {ten}**")
            st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;• SL: `{sl} kg` | ĐG: `{dg:,.0f}đ`")
            st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;• **Thành tiền: `{tt:,.0f} đ`**")
            st.markdown("---")
            
        st.markdown(f"### 💰 TỔNG CỘNG: {tong_cong:,.0f} VNĐ")
        st.markdown("---")
