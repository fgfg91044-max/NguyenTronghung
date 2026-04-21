import re

def chuan_hoa_chuoi(s):
    # 1. Xử lý từng dòng (dành cho bài thơ)
    lines = s.splitlines()
    ket_qua_dong = []
    
    for line in lines:
        # Loại bỏ khoảng trắng ở đầu và cuối dòng
        line = line.strip()
        
        # Nếu dòng trống thì bỏ qua hoặc giữ nguyên tùy ý (ở đây giữ dòng)
        if not line:
            ket_qua_dong.append("")
            continue
            
        # 2. Thay thế nhiều khoảng trắng giữa các từ bằng 1 khoảng trắng
        line = re.sub(r'\s+', ' ', line)
        
        # 3. Xử lý dấu phẩy và dấu chấm:
        # Tìm khoảng trắng đứng trước dấu phẩy/chấm và xóa nó đi
        # Ví dụ: "ngọt . " -> "ngọt."
        line = re.sub(r'\s+([,.])', r'\1', line)
        
        ket_qua_dong.append(line)
    
    # Nối các dòng lại bằng ký tự xuống dòng
    return "\n".join(ket_qua_dong)

# --- CHẠY THỬ NGHIỆM ---
chuoi_chua_hoan_chinh = """    Quê  hương
Quê hương là   chùm khế   ngọt.
   Cho con trèo hái  mỗi  ngày  .
Quê   hương là   đường đi học .
  Con  về  rợp bướm  vàng bay  .
  Đỗ     Trung Quân    """

print("--- Chuỗi sau khi chuẩn hóa: ---")
chuoi_sach = chuan_hoa_chuoi(chuoi_chua_hoan_chinh)
print(chuoi_sach)