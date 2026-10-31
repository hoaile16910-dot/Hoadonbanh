import streamlit as st
import pandas as pd

st.set_page_config(page_title="Tiệm Bánh Nhà Diễm", page_icon="🥐", layout="centered")

# --- HIỂN THỊ LOGO THƯƠNG HIỆU ---
try:
    st.image("IMG_1931.png", use_container_width=True)
except:
    st.title("🛒 TIỆM BÁNH NHÀ DIỄM")

# --- NÚT "NHẬP THÔNG TIN" TO RÕ NGAY GIỮA MÀN HÌNH ---
with st.popover("📝 NHẬP THÔNG TIN ĐƠN HÀNG", use_container_width=True):
    st.markdown("### Điền số lượng các loại bánh (kg):")
    ngay = st.text_input("Ngày ghi hoá đơn:", "31/10/2026")
    
    st.markdown("---")
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
data_rows = []
tong_cong = 0

for ten, sl, dg in danh_sach:
    if sl > 0:
        thanh_tien = sl * dg
        tong_cong += thanh_tien
        data_rows.append({
            "Tên bánh": ten,
            "SL (kg)": sl,
            "Đơn giá": f"{dg:,.0f} đ",
            "Thành tiền": f"{thanh_tien:,.0f} đ"
        })

st.markdown("---")
st.markdown("### 🧾 BẢNG HÓA ĐƠN CHI TIẾT")

if not data_rows:
    st.info("👆 Hãy bấm vào nút **'Nhập thông tin đơn hàng'** ở trên để chọn số lượng bánh nhé!")
else:
    # Ngày lập hóa đơn nằm sát ngay phía trên bảng
    st.markdown(f"<p style='margin-bottom: 5px; color: #555;'>📅 Ngày lập hóa đơn: <b>{ngay}</b></p>", unsafe_allow_html=True)
    
    # Thêm dòng tổng cộng vào cuối bảng
    data_rows.append({
        "Tên bánh": "TỔNG CỘNG",
        "SL (kg)": "-",
        "Đơn giá": "-",
        "Thành tiền": f"{tong_cong:,.0f} VNĐ"
    })
    
    df = pd.DataFrame(data_rows)
    st.table(df)
