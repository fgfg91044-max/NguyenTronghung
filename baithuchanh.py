# a) Hàm nhận 1 đối số n và trả về trị tuyệt đối của n
abs_val = lambda n: abs(n)

# Chạy thử
n = int(input("Nhập số nguyên n: "))
print(f"Trị tuyệt đối của {n} là: {abs_val(n)}")