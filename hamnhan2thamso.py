def luy_thua(a, b):
    # Điều kiện dừng: bất kỳ số nào mũ 0 cũng bằng 1
    if b == 0:
        return 1
    # Đệ quy: a^b = a * a^(b-1)
    return a * luy_thua(a, b - 1)

# Chạy thử
a = int(input("Nhập cơ số a: "))
b = int(input("Nhập số mũ b: "))
print(f"{a}^{b} = {luy_thua(a, b)}")