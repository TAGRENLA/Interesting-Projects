import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import pandas as pd
from tkinter import Menu


# 获取文件信息，包括文件类型
def get_files_info(directory):
    files_info = []

    # 遍历文件夹及子文件夹
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            # 获取文件大小（单位: 字节）
            file_size = os.path.getsize(file_path) / (1024 * 1024)  # 转换为MB
            # 获取文件扩展名（不包括文件名）
            file_name_without_ext = os.path.splitext(filename)[0]
            file_extension = os.path.splitext(filename)[1][1:].upper()  # 获取扩展名并转为大写
            files_info.append((file_name_without_ext, file_extension, round(file_size, 2), file_path))

    # 将文件信息转换为DataFrame
    df = pd.DataFrame(files_info, columns=['File Name', 'File Type', 'Size (MB)', 'File Path'])
    return df


# 浏览文件夹并更新表格
def browse_directory():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        # 获取文件信息
        df = get_files_info(folder_selected)

        # 清除现有的表格
        for row in tree.get_children():
            tree.delete(row)

        # 添加新数据到表格
        for i, row in df.iterrows():
            tree.insert('', 'end', values=(row['File Name'], row['File Type'], row['Size (MB)'], row['File Path']))


# 复制选中的文件信息
def copy_selected_item(event):
    selected_item = tree.selection()
    if selected_item:
        file_name, file_type, file_size, file_path = tree.item(selected_item)['values']
        clipboard_content = f"File Name: {file_name}\nFile Type: {file_type}\nSize (MB): {file_size}\nFile Path: {file_path}"
        root.clipboard_clear()  # 清空剪贴板
        root.clipboard_append(clipboard_content)  # 将信息复制到剪贴板
        messagebox.showinfo("Copied", "File information copied to clipboard.")



# 创建主窗口
root = tk.Tk()
root.title("File Information Viewer")

# 创建选择文件夹按钮
btn_select_folder = tk.Button(root, text="Select Folder", command=browse_directory)
btn_select_folder.pack(pady=10)


# 创建表格框架
columns = ('File Name', 'File Type', 'Size (MB)', 'File Path')
tree = ttk.Treeview(root, columns=columns, show='headings')

# 设置列宽和标题
tree.heading('File Name', text='File Name')
tree.heading('File Type', text='File Type')
tree.heading('Size (MB)', text='Size (MB)')
tree.heading('File Path', text='File Path')

tree.column('File Name', width=150)
tree.column('File Type', width=80)
tree.column('Size (MB)', width=80)
tree.column('File Path', width=400)

# 绑定右键点击事件
tree.bind("<Button-3>", copy_selected_item)

tree.pack(fill=tk.BOTH, expand=True)

# 运行GUI应用
root.mainloop()
