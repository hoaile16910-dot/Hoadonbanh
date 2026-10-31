import streamlit as st

st.set_page_config(page_title="Hóa Đơn Bán Hàng Nhà Diem", page_icon="🥐", layout="centered")

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

st.markdown("---")
st.markdown("### 🧾 BẢNG HÓA ĐƠN CHI TIẾT")

if not hoa_don_chi_tiet:
    st.info("👈 Hãy mở menu bên cạnh để nhập số lượng bánh, bảng hóa đơn sẽ tự động hiển thị ngay!")
else:
    # Hiển thị thông tin ngày tháng
    st.markdown(f"**Ngày lập hóa đơn:** {ngay}")
    
    # Tạo bảng ngang chuyên nghiệp bằng HTML thuần túy tối ưu cho màn hình di động
    html_table = """
    <div style="overflow-x: auto;">
        <table style="width: 100%; border-collapse: collapse; font-family: sans-serif; font-size: 14px; background-color: #fff; border: 1px solid #ddd;">
            <thead>
                <tr style="background-color: #bc6c25; color: white; text-align: left;">
                    <th style="padding: 10px; border: 1px solid #ddd;">Tên bánh</th>
                    <th style="padding: 10px; border: 1px solid #ddd; text-align: center;">SL (kg)</th>
                    <th style="padding: 10px; border: 1px solid #ddd; text-align: right;">Đơn giá</th>
                    <th style="padding: 10px; border: 1px solid #ddd; text-align: right;">Thành tiền</th>
                </tr>
            </thead>
            <tbody>
    """
    
    for ten, sl, dg, tt in hoa_don_chi_tiet:
        html_table += f"""
                <tr>
                    <td style="padding: 10px; border: 1px solid #ddd; font-weight: bold; color: #333;">{ten}</td>
                    <td style="padding: 10px; border: 1px solid #ddd; text-align: center; color: #555;">{sl}</td>
                    <td style="padding: 10px; border: 1px solid #ddd; text-align: right; color: #555;">{dg:,.0f} đ</td>
                    <td style="padding: 10px; border: 1px solid #ddd; text-align: right; font-weight: bold; color: #283618;">{tt:,.0f} đ</td>
                </tr>
        """
        
    html_table += f"""
            </tbody>
        </table>
    </div>
    <div style="margin-top: 15px; padding: 12px; background-color: #fefae0; border: 1px solid #dda15e; border-radius: 8px; display: flex; justify-content: space-between; align-items: center;">
        <span style="font-size: 16px; font-weight: bold; color: #333;">TỔNG CỘNG:</span>
        <span style="font-size: 20px; font-weight: bold; color: #9b2226;">{tong_cong:,.0f} VNĐ</span>
    </div>
    """
    
    st.markdown(html_table, unsafe_allow_html=True)
    st.success("💡 Bảng hóa đơn ngang hiển thị trực quan, các cột Tên, Số lượng, Đơn giá và Thành tiền được sắp xếp ngay ngắn, rõ ràng để bạn kiểm tra nhanh chóng!")
