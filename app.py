import streamlit as st

st.set_page_config(page_title="Hóa Đơn Bán Hàng Nhà Diem", page_icon="🥐", layout="centered")

# Tiêu đề ứng dụng
st.title("🛒 TIỆM BÁNH NHÀ DIEM")

# --- THANH BÊN (SIDEBAR) ĐỂ NHẬP LIỆU ---
st.sidebar.header("📝 Nhập thông tin đơn hàng")
ngay = st.sidebar.text_input("Ngày ghi hoá đơn:", "31/10/2026")

st.sidebar.markdown("---")
st.sidebar.markdown("### Nhập số lượng các loại bánh (kg):")

bbo = st.sidebar.number_input("1. Bánh bò (45,000 đ)", min_value=0.0, step=0.1, format="%.1f", key="bbo")
bbo_nuong = st.sidebar.number_input("2. Bánh bò nướng (130,000 đ)", min_value=0.0, step=0.1, format="%.1f", key="bbo_nuong")
bbo_chuoi = st.sidebar.number_input("3. Bánh bò chuối hồng (50,000 đ)", min_value=0.0, step=0.1, format="%.1f", key="bbo_chuoi")
bbo_bong = st.sidebar.number_input("4. Bánh bò bông (55,000 đ)", min_value=0.0, step=0.1, format="%.1f", key="bbo_bong")
bbo_da_lon = st.sidebar.number_input("5. Bánh bò da lợn (65,000 đ)", min_value=0.0, step=0.1, format="%.1f", key="bbo_da_lon")
banh_da_lon = st.sidebar.number_input("6. Bánh da lợn (50,000 đ)", min_value=0.0, step=0.1, format="%.1f", key="banh_da_lon")
bbo_cot_dua = st.sidebar.number_input("7. Bánh bò cốt dừa (60,000 đ)", min_value=0.0, step=0.1, format="%.1f", key="bbo_cot_dua")
bbo_thotnot = st.sidebar.number_input("8. Bánh bò thốt nốt (65,000 đ)", min_value=0.0, step=0.1, format="%.1f", key="bbo_thotnot")

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

# --- MÀN HÌNH CHÍNH: HIỂN THỊ HÓA ĐƠN RÕ RÀNG, CỠ CHỮ TO ---
st.markdown("### 🧾 HÓA ĐƠN BÁN HÀNG")
st.markdown("---")

if not hoa_don_chi_tiet:
    st.info("👈 Hãy mở menu bên cạnh để nhập số lượng bánh, hóa đơn sẽ tự động hiển thị ngay tại đây!")
else:
    with st.container(border=True):
        st.markdown("<h3 style='text-align: center; color: #bc6c25;'>🥐 TIỆM BÁNH NHÀ DIEM</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; color: #666;'>Ngày: <b>{ngay}</b></p>", unsafe_allow_html=True)
        st.markdown("---")
        
        stt = 1
        for ten, sl, dg, tt in hoa_don_chi_tiet:
            # Tăng kích thước chữ cho số lượng và thành tiền hiển thị to rõ nổi bật
            st.markdown(f"#### **{stt}. {ten}**")
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown(f"<span style='font-size: 16px; color: #333;'>📦 SL: <b>{sl} kg</b></span>", unsafe_allow_html=True)
                st.markdown(f"<span style='font-size: 13px; color: #666;'>ĐG: {dg:,.0f} đ</span>", unsafe_allow_html=True)
            with col2:
                st.markdown(f"<div style='text-align: right; font-size: 18px; font-weight: bold; color: #283618;'>{tt:,.0f} đ</div>", unsafe_allow_html=True)
            
            st.markdown("<hr style='margin: 8px 0; border-top: 1px dashed #ddd;'>", unsafe_allow_html=True)
            stt += 1
            
        st.markdown("---")
        col_t1, col_t2 = st.columns([1, 1])
        with col_t1:
            st.markdown("#### **TỔNG CỘNG:**")
        with col_t2:
            st.markdown(f"<div style='text-align: right; font-size: 20px; font-weight: bold; color: #9b2226;'>{tong_cong:,.0f} VNĐ</div>", unsafe_allow_html=True)
            
        st.markdown("<p style='text-align: center; font-size: 12px; color: #888; margin-top: 15px;'>🙏 Cảm ơn quý khách và hẹn gặp lại! ❤️</p>", unsafe_allow_html=True)

    st.success("💡 Bạn có thể chụp màn hình khung hóa đơn phía trên để gửi cho khách hàng cực kỳ rõ nét!")
