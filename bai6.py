import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import re

def dem_tu():
    s = text_input.get("1.0", tk.END).strip()
    word = entry_word.get().strip().lower()
    
    if not s or not word:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập chuỗi và từ cần tìm!")
        return
    
    # Tách chuỗi thành các từ (xử lý dấu cách, dấu câu)
    words = re.findall(r'\b\w+\b', s.lower())
    
    # Đếm số lần xuất hiện của word
    count = words.count(word.lower())
    
    # Hiển thị kết quả
    result_label.config(text=f"Số từ '{word}' là: {count}")
    result_text.delete("1.0", tk.END)
    result_text.insert("1.0", f"Kết quả: Số từ '{word}' là {count}\n\n")
    result_text.insert("2.0", f"Tổng số từ trong chuỗi: {len(words)}\n")
    result_text.insert("3.0", f"Số lần '{word}' xuất hiện: {count}")

def load_van_ban():
    van_ban = '''Chiều chiều trước bến Văn Lâu
Ai ngồi, ai câu, ai sầu, ai thảm
Ai thương, ai cảm, ai nhớ, ai trông
Thuyền ai thấp thoáng ven sông
Đưa câu mái vẩy chạnh lòng nước non'''
    text_input.delete("1.0", tk.END)
    text_input.insert("1.0", van_ban)
    entry_word.delete(0, tk.END)
    entry_word.insert(0, "ai")

def clear_all():
    text_input.delete("1.0", tk.END)
    entry_word.delete(0, tk.END)
    result_label.config(text="")
    result_text.delete("1.0", tk.END)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Đếm số từ trong chuỗi")
root.geometry("700x600")
root.configure(bg="#f0f0f0")

# Style
style = ttk.Style()
style.configure("Title.TLabel", font=("Arial", 16, "bold"))

# Tiêu đề
title_label = ttk.Label(root, text="🔍 CHƯƠNG TRÌNH ĐẾM SỐ TỪ", style="Title.TLabel")
title_label.pack(pady=10)

# Frame nhập liệu
input_frame = ttk.LabelFrame(root, text="Nhập dữ liệu", padding="10")
input_frame.pack(pady=10, padx=20, fill="x")

# Nhập chuỗi
ttk.Label(input_frame, text="Chuỗi S:").pack(anchor="w")
text_input = scrolledtext.ScrolledText(input_frame, height=8, width=70, wrap=tk.WORD)
text_input.pack(pady=5, fill="both", expand=True)

# Nhập từ cần tìm
word_frame = ttk.Frame(input_frame)
word_frame.pack(pady=5, fill="x")

ttk.Label(word_frame, text="Từ cần tìm:", font=("Arial", 10, "bold")).pack(side="left")
entry_word = ttk.Entry(word_frame, font=("Arial", 12), width=15)
entry_word.pack(side="left", padx=5)

# Nút Load văn bản mẫu
ttk.Button(word_frame, text="📄 Load mẫu", command=load_van_ban).pack(side="left", padx=5)

# Frame nút chức năng
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

ttk.Button(button_frame, text="✅ Đếm từ", command=dem_tu, 
           style="Accent.TButton").pack(side="left", padx=5)
ttk.Button(button_frame, text="🗑️ Xóa tất cả", command=clear_all).pack(side="left", padx=5)

# Frame kết quả
result_frame = ttk.LabelFrame(root, text="Kết quả", padding="10")
result_frame.pack(pady=10, padx=20, fill="both", expand=True)

result_label = ttk.Label(result_frame, text="", font=("Arial", 14, "bold"), 
                        foreground="blue")
result_label.pack(pady=5)

result_text = scrolledtext.ScrolledText(result_frame, height=6, state="normal")
result_text.pack(pady=5, fill="both", expand=True)

# Hướng dẫn
info_label = ttk.Label(root, text="💡 Nhập chuỗi và từ cần tìm, sau đó nhấn 'Đếm từ'", 
                      font=("Arial", 10), foreground="gray")
info_label.pack(pady=5)

# Load văn bản mẫu khi khởi động
load_van_ban()

# Chạy ứng dụng
root.mainloop()