import math

# i) Kiểm tra 3 cạnh có lập thành tam giác và đó là tam giác gì
# Bước 1: Lambda kiểm tra tính hợp lệ
is_valid = lambda a, b, c: a + b > c and a + c > b and b + c > a

def check_triangle_type(a, b, c):
    if not is_valid(a, b, c):
        return "Không phải là 3 cạnh của 1 tam giác"
    
    # Logic phân loại
    if a == b == c:
        return "Tam giác đều"
    
    # Kiểm tra tam giác vuông bằng định lý Pythagoras
    sides = sorted([a, b, c])
    is_vuong = math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)
    
    if a == b or b == c or a == c:
        return "Tam giác vuông cân" if is_vuong else "Tam giác cân"
    if is_vuong:
        return "Tam giác vuông"
    
    return "Tam giác thường"

# Chạy thử
a = float(input("Cạnh a: "))
b = float(input("Cạnh b: "))
c = float(input("Cạnh c: "))
print(f"Kết quả: {check_triangle_type(a, b, c)}")