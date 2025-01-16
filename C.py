# ecoding:utf-8
import tkinter as tk
from tkinter import messagebox


def swap_coordinates():
    try:
        # 获取用户输入的数据
        input_data = text_input.get("1.0", tk.END).strip()

        if not input_data:
            raise ValueError("输入内容不能为空")

        # 获取用户输入的分隔符
        input_delimiter = input_delimiter_entry.get().strip() or ","
        output_delimiter = output_delimiter_entry.get().strip() or " "

        # 按行拆分输入数据
        lines = input_data.split('\n')

        # 处理每一行数据
        swapped_data = []
        for line in lines:
            # 跳过空行
            if line.strip() == "":
                continue
            parts = line.split(input_delimiter)
            if len(parts) != 2:
                raise ValueError("每行数据必须包含两个部分（例如：A,B）")
            # 对调
            swapped_data.append(f"{parts[1]}{output_delimiter}{parts[0]}")

        # 将结果显示在输出框中
        output_text.delete("1.0", tk.END)  # 清空之前的内容
        output_text.insert(tk.END, "\n".join(swapped_data))

    except ValueError as e:
        messagebox.showerror("输入错误", str(e))


# 创建主窗口
root = tk.Tk()
root.title("数据对调程序【作者：S64959】")

# 设置窗口大小和可调整
root.geometry("502x500")
root.resizable(True, True)

# 标签：输入
label_input = tk.Label(root, text="请输入数据（每行A,B-->B A）：", font=('Arial', 10))
label_input.pack(pady=5)

# 创建输入框和滚动条的容器
input_frame = tk.Frame(root)
input_frame.pack(fill=tk.BOTH, expand=True, pady=5)

# 输入框
text_input = tk.Text(input_frame, height=10, width=70)
text_input.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# 输入框滚动条
input_scrollbar = tk.Scrollbar(input_frame, orient="vertical", command=text_input.yview)
input_scrollbar.pack(side=tk.RIGHT, fill="y")
text_input.config(yscrollcommand=input_scrollbar.set)

# 标签：分隔符选择
separator_frame = tk.Frame(root)
separator_frame.pack(pady=5)

input_delimiter_label = tk.Label(separator_frame, text="原始数据分隔符：", font=('Arial', 10))
input_delimiter_label.pack(side=tk.LEFT, padx=5)

# 默认分隔符为逗号
input_delimiter_entry = tk.Entry(separator_frame, width=10)
input_delimiter_entry.insert(tk.END, ",")  # 默认逗号
input_delimiter_entry.pack(side=tk.LEFT, padx=5)

output_delimiter_label = tk.Label(separator_frame, text="新数据分隔符：", font=('Arial', 10))
output_delimiter_label.pack(side=tk.LEFT, padx=5)

# 默认分隔符为空格
output_delimiter_entry = tk.Entry(separator_frame, width=10)
output_delimiter_entry.insert(tk.END, "***")  # 默认空格
output_delimiter_entry.pack(side=tk.LEFT, padx=5)

# 按钮：对调
btn_swap = tk.Button(root, text="对调", command=swap_coordinates, font=('Arial', 12), width=15)
btn_swap.pack(pady=10)

# 标签：输出结果
label_output = tk.Label(root, text="对调后的结果：", font=('Arial', 10))
label_output.pack(pady=5)

# 创建输出框和滚动条的容器
output_frame = tk.Frame(root)
output_frame.pack(fill=tk.BOTH, expand=True, pady=5)

# 输出框
output_text = tk.Text(output_frame, height=10, width=70)
output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# 输出框滚动条
output_scrollbar = tk.Scrollbar(output_frame, orient="vertical", command=output_text.yview)
output_scrollbar.pack(side=tk.RIGHT, fill="y")
output_text.config(yscrollcommand=output_scrollbar.set)

# 运行主循环
root.mainloop()
