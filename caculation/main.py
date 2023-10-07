import math
import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def sin():
    try:
        angle = float(entry.get())
        result = math.sin(math.radians(angle))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def cos():
    try:
        angle = float(entry.get())
        result = math.cos(math.radians(angle))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def tan():
    try:
        angle = float(entry.get())
        result = math.tan(math.radians(angle))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def power():
    try:
        exponent = float(entry.get())
        result = math.pow(10, exponent)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

window = tk.Tk()
window.title("Calculator")

# 创建一个Frame来容纳计算器的部件
frame = tk.Frame(window, padx=10, pady=10)
frame.pack()

entry = tk.Entry(frame, width=30, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, pady=10)

# 数字按钮
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row = 1
col = 0
for button in buttons:
    btn = tk.Button(frame, text=button, width=5, font=("Arial", 12), command=lambda button=button: entry.insert(tk.END, button))
    btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# 三角函数按钮
sin_btn = tk.Button(frame, text="sin", width=5, font=("Arial", 12), command=sin)
sin_btn.grid(row=2, column=4, padx=5, pady=5)

cos_btn = tk.Button(frame, text="cos", width=5, font=("Arial", 12), command=cos)
cos_btn.grid(row=3, column=4, padx=5, pady=5)

tan_btn = tk.Button(frame, text="tan", width=5, font=("Arial", 12), command=tan)
tan_btn.grid(row=4, column=4, padx=5, pady=5)

# 指数运算按钮
power_btn = tk.Button(frame, text="^", width=5, font=("Arial", 12), command=power)
power_btn.grid(row=5, column=4, padx=5, pady=5)

# 计算按钮
calc_btn = tk.Button(frame, text="=", width=12, font=("Arial", 12), command=calculate)
calc_btn.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

# 清除按钮
clear_btn = tk.Button(frame, text="C", width=12, font=("Arial", 12), command=lambda: entry.delete(0, tk.END))
clear_btn.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()
