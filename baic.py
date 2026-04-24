# c) Hàm nhận 2 đối số (x, y) và trả về tích x * y
multiply = lambda x, y: x * y

# Chạy thử
x = int(input("Nhập x: "))
y = int(input("Nhập y: "))
print(f"Tích của {x} và {y} là: {multiply(x, y)}")