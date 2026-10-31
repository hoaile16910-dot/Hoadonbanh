import streamlit as st

st.set_page_config(page_title="Hóa Đơn Bán Hàng Nhà Diem", page_icon="🥐", layout="wide")

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

# --- MÀN HÌNH CHÍNH: HIỂN THỊ HÓA ĐƠN DẠNG THẺ (CARD) CÓ LOGO ---
st.markdown("### 🧾 HÓA ĐƠN BÁN HÀNG (Tự động cập nhật)")
st.markdown("---")

if not hoa_don_chi_tiet:
    st.info("👈 Hãy chọn mở menu bên cạnh để nhập số lượng bánh, hóa đơn có logo sẽ hiện ra ngay tại đây!")
else:
    # Tạo giao diện thẻ hóa đơn chuyên nghiệp bằng HTML/CSS tích hợp sẵn trong Streamlit
    html_hoa_don = f"""
    <div style="background-color: #fdfbf7; border: 2px dashed #d4a373; padding: 20px; border-radius: 12px; font-family: sans-serif; color: #333; max-width: 500px; margin: auto;">
        <div style="text-align: center;">
            <span style="font-size: 40px;">🥐</span>
            <h2 style="color: #bc6c25; margin: 5px 0;">TIỆM BÁNH NHÀ DIEM</h2>
            <p style="font-size: 13px; color: #666; margin: 0;">Chuyên cung cấp các loại bánh bò truyền thống ngon sạch</p>
            <hr style="border: 0; border-top: 1px solid #e0d0c0; margin: 15px 0;">
            <p style="text-align: left; font-weight: bold; margin: 5px 0;">📅 Ngày: {ngay}</p>
        </div>
        <table style="width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 14px;">
            <tr style="border-bottom: 2px solid #ddd; text-align: left; color: #555;">
                <th style="padding: 6px;">Món</th>
                <th style="padding: 6px; text-align: center;">SL</th>
                <th style="padding: 6px; text-align: right;">Thành tiền</th>
            </tr>
    """
    
    for ten, sl, dg, tt in hoa_don_chi_tiet:
        html_hoa_don += f"""
            <tr style="border-bottom: 1px solid #eee;">
                <td style="padding: 8px 6px;"><b>{ten}</b><br><span style="font-size: 11px; color: #775;">({dg:,.0f} đ/kg)</span></td>
                <td style="padding: 8px 6px; text-align: center;">{sl} kg</td>
                <td style="padding: 8px 6px; text-align: right; font-weight: bold; color: #283618;">{tt:,.0f} đ</td>
            </tr>
        """
        
    html_hoa_don += f"""
        </table>
        <hr style="border: 0; border-top: 2px solid #d4a373; margin: 15px 0;">
        <div style="display: flex; justify-content: space-between; align-items: center; font-size: 16px;">
            <span style="font-weight: bold; color: #333;">TỔNG CỘNG:</span>
            <span style="font-weight: bold; color: #9b2226; font-size: 18px;">{tong_cong:,.0f} VNĐ</span>
        </div>
        <div style="text-align: center; margin-top: 20px; font-size: 12px; color: #888;">
            <p>🙏 Cảm ơn quý khách và hẹn gặp lại! ❤️</p>
        </div>
    </div>
    """
    
    # Hiển thị khung hóa đơn lên web
    st.markdown(html_hoa_don, unsafe_allow_html=True)
    
    st.success("💡 Mẹo trên điện thoại: Bạn chỉ cần chụp màn hình khung hóa đơn màu kem phía trên là đã có ngay một bức ảnh hóa đơn kèm logo cực kỳ đẹp mắt để gửi Zalo cho khách!")
