import math

# e) Tính diện tích hình tròn với bán kính r
circle_area = lambda r: math.pi * r**2

# Chạy thử
r = float(input("Nhập bán kính r: "))
print(f"Diện tích hình tròn là: {circle_area(r):.2f}")