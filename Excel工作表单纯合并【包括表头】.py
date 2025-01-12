# ecoding:utf-8
import os
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import openpyxl
import xlrd

# 函数：合并工作簿中的所有工作表
def merge_sheets(input_file, output_file):
    try:
        # 创建一个新的 DataFrame 来存储所有数据
        combined_data = pd.DataFrame()

        # 读取工作簿中的所有工作表
        xls = pd.ExcelFile(input_file)
        for sheet_name in xls.sheet_names:
            sheet_data = pd.read_excel(input_file, sheet_name=sheet_name)
            sheet_data['Source_Sheet'] = sheet_name  # 添加一个列标明数据来源
            combined_data = pd.concat([combined_data, sheet_data], ignore_index=True)

        # 保存到新的文件
        combined_data.to_excel(output_file, index=False)
        return True

    except Exception as e:
        messagebox.showerror("错误", f"发生错误：{str(e)}")
        return False

# GUI：主窗口
def main():
    def select_input_file():
        file_path = filedialog.askopenfilename(
            title="选择一个Excel文件",
            filetypes=[("Excel文件", "*.xls;*.xlsx;*.xlsm")]
        )
        if file_path:
            input_file_var.set(file_path)

    def select_output_directory():
        directory = filedialog.askdirectory(title="选择输出目录")
        if directory:
            output_dir_var.set(directory)

    # 开始合并功能逻辑
    def start_merge():
        input_file = input_file_var.get()
        output_dir = output_dir_var.get()
        output_file_name = output_file_name_var.get()
        output_format = output_format_var.get()

        if not input_file or not output_dir:
            messagebox.showwarning("警告", "请先选择输入文件和输出目录！")
            return

        if not output_file_name:
            messagebox.showwarning("警告", "请先输入输出文件名！")
            return

        if output_format not in ["xlsx", "xls"]:
            messagebox.showwarning("警告", "请选择有效的文件格式！")
            return

        # 弹窗提示用户表头信息
        response = messagebox.askquestion(
            "重要提示",
            "作者声明：\n默认将表格第一行作为表头，其余均为具体元素！\n并且注意命名，会直接覆盖同名文件！！！\n\n是否继续合并？",
            icon="warning"
        )

        if response == "no":
            return  # 用户选择返回，不执行合并

        # 构建输出文件路径
        output_file = os.path.join(output_dir, f"{output_file_name}.{output_format}")

        # 开始合并
        success = merge_sheets(input_file, output_file)
        if success:
            messagebox.showinfo("成功", f"合并完成！文件已保存到：{output_file}")

    # 初始化主窗口
    root = tk.Tk()
    root.title("Excel工作表合并工具")
    root.geometry("500x500")

    # 输入文件选择
    input_file_var = tk.StringVar()
    tk.Label(root, text="选择输入文件：").pack(pady=5)
    tk.Entry(root, textvariable=input_file_var, width=50).pack(pady=5)
    tk.Button(root, text="浏览", command=select_input_file).pack(pady=5)

    # 输出目录选择
    output_dir_var = tk.StringVar()
    tk.Label(root, text="选择输出目录：").pack(pady=5)
    tk.Entry(root, textvariable=output_dir_var, width=50).pack(pady=5)
    tk.Button(root, text="浏览", command=select_output_directory).pack(pady=5)

    # 输出文件名输入
    output_file_name_var = tk.StringVar()
    tk.Label(root, text="输入输出文件名（不含扩展名）：").pack(pady=5)
    tk.Entry(root, textvariable=output_file_name_var, width=50).pack(pady=5)

    # 输出格式选择
    output_format_var = tk.StringVar(value="xlsx")
    tk.Label(root, text="选择输出文件格式：").pack(pady=5)
    tk.Radiobutton(root, text="Excel (.xlsx)", variable=output_format_var, value="xlsx").pack()
    tk.Radiobutton(root, text="Excel 97-2003 (.xls)", variable=output_format_var, value="xls").pack()

    # 开始合并按钮
    tk.Button(root, text="开始合并", command=start_merge, bg="green", fg="white").pack(pady=20)

    # 运行主窗口
    root.mainloop()

if __name__ == "__main__":
    main()
