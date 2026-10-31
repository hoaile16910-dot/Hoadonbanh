import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

st.set_page_config(page_title="Hóa Đơn Bán Hàng Nhà Diem", page_icon="🥐", layout="centered")

st.title("🛒 TIỆM BÁNH NHÀ DIEM - XUẤT ẢNH HÓA ĐƠN")

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

if not hoa_don_chi_tiet:
    st.info("👈 Hãy mở menu bên cạnh để nhập số lượng bánh.")
else:
    st.markdown("### 📸 TẠO VÀ TẢI ẢNH HÓA ĐƠN")
    
    # Hàm tự động vẽ ảnh hóa đơn
    def tao_anh_hoa_don():
        # Kích thước khung ảnh
        img_width = 600
        img_height = 250 + (len(hoa_don_chi_tiet) * 50)
        
        # Tạo ảnh nền màu kem sáng
        img = Image.new('RGB', (img_width, img_height), color='#fdfbf7')
        draw = ImageDraw.Draw(img)
        
        # Sử dụng font mặc định hệ thống (hoặc có thể dùng font chữ cơ bản)
        try:
            font_title = ImageFont.truetype("arial.ttf", 22)
            font_bold = ImageFont.truetype("arial.ttf", 16)
            font_normal = ImageFont.truetype("arial.ttf", 15)
        except:
            font_title = ImageFont.load_default()
            font_bold = ImageFont.load_default()
            font_normal = ImageFont.load_default()

        # Vẽ nội dung lên ảnh
        draw.text((200, 30), "TIỆM BÁNH NHÀ DIEM", fill="#bc6c25", font=font_title)
        draw.text((230, 65), f"Ngày: {ngay}", fill="#666666", font=font_normal)
        draw.line([(30, 95), (570, 95)], fill="#d4a373", width=2)
        
        y = 120
        stt = 1
        for ten, sl, dg, tt in hoa_don_chi_tiet:
            draw.text((40, y), f"{stt}. {ten}", fill="#222222", font=font_bold)
            draw.text((40, y + 22), f"   SL: {sl} kg x {dg:,.0f}đ", fill="#666666", font=font_normal)
            draw.text((420, y + 10), f"{tt:,.0f} đ", fill="#283618", font=font_bold)
            y += 55
            stt += 1
            
        draw.line([(30, y + 10), (570, y + 10)], fill="#d4a373", width=2)
        draw.text((40, y + 30), "TỔNG CỘNG:", fill="#000000", font=font_title)
        draw.text((380, y + 30), f"{tong_cong:,.0f} VNĐ", fill="#9b2226", font=font_title)
        
        draw.text((180, y + 85), "Cảm ơn quý khách và hẹn gặp lại! ❤️", fill="#888888", font=font_normal)
        
        # Lưu vào bộ nhớ đệm dạng bytes để tải về
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()
        return byte_im

    # Nút bấm tạo ảnh và tải về
    anh_bytes = tao_anh_hoa_don()
    
    st.image(anh_bytes, caption="Xem trước ảnh hóa đơn", use_container_width=True)
    
    st.download_button(
        label="📥 TẢI ẢNH HÓA ĐƠN VỀ MÁY",
        data=anh_bytes,
        file_name=f"HoaDon_{ngay.replace('/', '-')}.png",
        mime="image/png",
        type="primary"
    )
