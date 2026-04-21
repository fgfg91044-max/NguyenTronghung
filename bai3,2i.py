from datetime import datetime, timedelta
import math

# ==========================================
# i. Viết chương trình in ra các thông tin hiện tại
# ==========================================
now = datetime.now()

print("--- i. Thông tin hiện tại ---")
print(f"Năm hiện tại: {now.year}")
print(f"Tháng hiện tại bằng chữ: {now.strftime('%B')}")
print(f"Tuần hiện tại là tuần thứ mấy trong năm: {now.strftime('%U')}")

# Tính tuần trong tháng: Lấy ngày hiện tại chia cho 7 và làm tròn lên
week_of_month = math.ceil(now.day / 7)
print(f"Tuần hiện tại là tuần thứ mấy trong tháng: {week_of_month}")

print(f"Ngày hiện tại là ngày thứ mấy trong năm: {now.strftime('%j')}")
print(f"Ngày dương lịch hiện tại là ngày: {now.day}")
print(f"Thứ của ngày hiện tại: {now.strftime('%A')}")
print(f"Giờ phút giây hiện tại: {now.strftime('%H:%M:%S')}")


# ==========================================
# ii. Tính số ngày cách nhau giữa 2 ngày
# ==========================================
print("\n--- ii. Tính khoảng cách giữa 2 ngày ---")
print("Nhập ngày thứ nhất:")
d1 = int(input("Ngày: "))
m1 = int(input("Tháng: "))
y1 = int(input("Năm: "))

print("Nhập ngày thứ hai:")
d2 = int(input("Ngày: "))
m2 = int(input("Tháng: "))
y2 = int(input("Năm: "))

date1 = datetime(y1, m1, d1)
date2 = datetime(y2, m2, d2)
delta = abs((date2 - date1).days)
print(f"Số ngày cách nhau giữa 2 ngày là: {delta} ngày")


# ==========================================
# iii. Chuyển chuỗi S sang kiểu ngày
# ==========================================
print("\n--- iii. Chuyển chuỗi sang kiểu ngày ---")
s = "Sep 18 2019 2:43PM"
# Định dạng: %b (tháng viết tắt), %d (ngày), %Y (năm 4 số), %I (giờ 12), %M (phút), %p (AM/PM)
date_obj = datetime.strptime(s, "%b %d %Y %I:%M%p")
print(f"Chuỗi sau khi chuyển sang đối tượng datetime: {date_obj}")
print(f"Kiểu dữ liệu: {type(date_obj)}")


# ==========================================
# iv. Sử dụng timedelta để thêm 5 giây
# ==========================================
print("\n--- iv. Thêm 5 giây vào thời gian hiện tại ---")
now_plus_5 = now + timedelta(seconds=5)
print(f"Thời gian hiện tại: {now.strftime('%H:%M:%S')}")
print(f"Thời gian sau khi thêm 5 giây: {now_plus_5.strftime('%H:%M:%S')}")