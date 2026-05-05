from collections import Counter

def main():
    s1 = input("Nhập chuỗi S1: ")
    s2 = input("Nhập chuỗi S2: ")

    # a) In ra những ký tự xuất hiện trong cả 2 chuỗi
    print("\n--- Câu a ---")
    # Sử dụng class Counter để chuyển đổi chuỗi thành dictionary đếm tần suất
    c1 = Counter(s1)
    c2 = Counter(s2)
    
    # Thực hiện phép AND (&) trên 2 dict để lấy các ký tự chung
    common_dict = c1 & c2 
    common_chars = list(common_dict.keys())
    print(f"Các ký tự xuất hiện trong cả 2 chuỗi là: {common_chars}")

    # c) In ra những ký tự có trong S1 nhưng không có trong S2 và ngược lại
    # (Thực hiện logic câu c trước để lấy danh sách phục vụ cho việc đếm ở câu b)
    print("\n--- Câu c ---")
    # Đưa mỗi chuỗi vào 1 dict. Dùng dict.fromkeys() để tự động loại bỏ các ký tự trùng lặp.
    dict1 = dict.fromkeys(s1)
    dict2 = dict.fromkeys(s2)

    # Dò tìm S1 trên dict2: Lấy các ký tự (key) trong dict1 mà không có trong dict2
    s1_not_s2 = [char for char in dict1 if char not in dict2]
    
    # Dò tìm S2 trên dict1: Lấy các ký tự (key) trong dict2 mà không có trong dict1
    s2_not_s1 = [char for char in dict2 if char not in dict1]

    print(f"Các ký tự có trong S1 nhưng không có trong S2: {s1_not_s2}")
    print(f"Các ký tự có trong S2 nhưng không có trong S1: {s2_not_s1}")

    # b) Đếm xem có bao nhiêu ký tự có trong S1 nhưng không có S2 và ngược lại
    print("\n--- Câu b ---")
    print(f"Số lượng ký tự có trong S1 nhưng không có trong S2 là: {len(s1_not_s2)}")
    print(f"Số lượng ký tự có trong S2 nhưng không có trong S1 là: {len(s2_not_s1)}")

if __name__ == "__main__":
    main()