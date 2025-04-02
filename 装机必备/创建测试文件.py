import os
import shutil

def clear_folder(folder_path):
    """清空指定文件夹内容，但保留文件夹本身"""
    if os.path.exists(folder_path):
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            try:
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.unlink(item_path)  # 删除文件或符号链接
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)  # 删除子文件夹
            except Exception as e:
                print(f"删除 {item_path} 失败: {e}")
    else:
        os.makedirs(folder_path)  # 如果文件夹不存在，则创建

def create_test_files(folder_path):
    """在指定文件夹内创建 a.py 到 z.py 文件"""
    os.makedirs(folder_path, exist_ok=True)  # 确保文件夹存在
    for letter in "abcdefghijklmnopqrstuvwxyz":
        file_path = os.path.join(folder_path, f"{letter}.py")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# ecoding:utf-8\n# 当前的测试文件名称: {letter}.py\n")
            print(f"{letter}.py 已经被创建")
    print("测试文件创建完成！")

if __name__ == "__main__":
    test_folder = "./test_files"
    clear_folder(test_folder)  # 先清空 test_files 文件夹
    create_test_files(test_folder)  # 再创建新的测试文件
