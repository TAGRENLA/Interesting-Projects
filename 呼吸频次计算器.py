# ecoding:utf-8
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def calculate():
    try:
        # 获取用户输入
        tem1 = int(min_value_entry.get())
        tem2 = int(max_value_entry.get())

        # 计算平均值和呼吸频次
        T = (tem2 - tem1) * 0.1 / 4
        num = round(60 / T)

        # 显示结果
        result_text = (f"四个呼吸周期的平均值为：（{tem2} - {tem1}） * 0.1 /4 = {T:.2f}s\n"
                       f"每分钟的呼吸次数或呼吸频次为：  60 / 四个呼吸周期的平均值 = {num}次/分钟")
        result_label.config(text=result_text)

        # 更新复制按钮功能
        def copy_to_clipboard():
            root.clipboard_clear()
            root.clipboard_append(result_text)
            root.update()  # 现在更新剪贴板内容
            messagebox.showinfo("复制成功", "结果已复制到剪贴板！")

        copy_button.config(command=copy_to_clipboard)
        copy_button.pack()  # 显示复制按钮

    except ValueError:
        messagebox.showerror("输入错误", "请输入有效的整数！")

# 创建主窗口
root = tk.Tk()
root.title("呼吸频次计算器 【作者：赵锦博】闲来无事整一个玩玩")
root.geometry("400x300")  # 初始窗口大小

# 动态调整输入框和结果框大小的函数
def resize_widgets(event):
    new_width = event.width - 20
    min_value_entry.config(width=new_width // 10)
    max_value_entry.config(width=new_width // 10)
    result_label.config(wraplength=new_width - 20)

root.bind("<Configure>", resize_widgets)

# 输入最小波形数值
min_value_label = tk.Label(root, text="请输入最小波形数值【四周期型】：")
min_value_label.pack()
min_value_entry = tk.Entry(root, width=50)
min_value_entry.pack(fill="x", padx=10)

# 输入最大波形数值
max_value_label = tk.Label(root, text="请输入最大波形数值【四周期型】：")
max_value_label.pack()
max_value_entry = tk.Entry(root, width=50)
max_value_entry.pack(fill="x", padx=10)

# 计算按钮
calculate_button = tk.Button(root, text="计算", command=calculate)
calculate_button.pack(pady=5)

# 显示结果
result_label = tk.Label(root, text="", fg="blue", wraplength=380, justify="left")
result_label.pack(fill="x", padx=10, pady=5)

# 复制按钮（默认隐藏，计算后显示）
copy_button = tk.Button(root, text="复制结果")

# 运行主循环
root.mainloop()