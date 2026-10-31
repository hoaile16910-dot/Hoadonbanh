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
    st.info("👈 Hãy mở menu bên cạnh để nhập số lượng bánh, bảng hóa đơn sẽ tự động hiển thị!")
else:
    # Gom ngày tháng xuống sát ngay phía trên bảng cho gọn gàng
    st.markdown(f"<p style='margin-bottom: 5px; color: #555;'>📅 Ngày lập hóa đơn: <b>{ngay}</b></p>", unsafe_allow_html=True)
    
    # Tạo bảng ngang chuẩn Markdown có sẵn dòng tổng cộng gộp phía dưới
    markdown_table = "| Tên bánh | SL (kg) | Đơn giá | Thành tiền |\n"
    markdown_table += "| :--- | :---: | ---: | ---: |\n"
    
    for ten, sl, dg, tt in hoa_don_chi_tiet:
        markdown_table += f"| **{ten}** | {sl} | {dg:,.0f} đ | {tt:,.0f} đ |\n"
        
    # Gộp hàng tổng cộng vào ngay trong bảng
    markdown_table += f"| **TỔNG CỘNG** | - | - | **{tong_cong:,.0f} VNĐ** |"
        
    st.markdown(markdown_table)
