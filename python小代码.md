[TOC]





# 提取一个文件夹中的所有的文件名及其大小

详细描述：用python提取一个文件夹中的所有的文件名及其大小，文件名称不包含后缀，大小单位达到1G用G作为单位，没达到 就用MB，并将最后的结果装进Excel表格中。

```python
# ecoding:utf-8 
import os
import pandas as pd

def format_size(size_bytes):
    if size_bytes >= 1 << 30:  # 1 GB = 1 << 30 bytes
        return f"{size_bytes / (1 << 30):.2f} GB"
    else:
        return f"{size_bytes / (1 << 20):.2f} MB"  # 1 MB = 1 << 20 bytes

def get_files_info(directory):
    files_info = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            file_name_without_extension = os.path.splitext(file)[0]
            formatted_size = format_size(file_size)
            files_info.append((file_name_without_extension, formatted_size))
    return files_info

def save_files_info_to_csv(files_info, output_file):
    df = pd.DataFrame(files_info, columns=['File Name', 'Size'])
    df.to_csv(output_file, index=False, encoding='utf-8')

if __name__ == "__main__":
    directory = r"D:\移动云盘同步盘\蠢沫沫全套版本【不包含单卖版本】【第二版本】"
    files_info = get_files_info(directory)
    output_file = r"D:\移动云盘同步盘\files_info.csv"  # 可以根据需要更改输出文件路径
    save_files_info_to_csv(files_info, output_file)
    print(f"File information has been saved to {output_file}")

```

#  批量创建Chrome浏览器分身

> 源码地址【作者：S64959】：https://github.com/TAGRENLA/Interesting-Projects

---

## 谷歌浏览器多开代码

```txt
 --user-data-dir=E:\Users\谷歌浏览器多开缓存\1




最后一个1进行更换   【最前面有个空格】
```

## 基于原文件夹路径创建快捷方式

创建的快捷方式是基于本机最初下载的Chrome浏览器的！其实就是单纯的快捷方式！

```python
import os
import shutil

# 源文件路径
source_path = r'E:\Users\TAGRENLA\Desktop\Google Chrome.lnk'


# 目标文件夹路径
target_dir = r'E:\Users\TAGRENLA\Desktop\Google222'

# 确保目标文件夹存在
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# 循环从3到100，为每个数字创建一个快捷方式副本
for i in range(101, 1001):
    # 为每个副本创建一个唯一的文件名
    target_path = os.path.join(target_dir, f'Google Chrome - {i} - .lnk')
    # 复制文件
    shutil.copy(source_path, target_path)

print(f'完成复制，总共创建了{range(3, 101).stop - range(3, 101).start}个副本。')

```

## 读取相关的数据，方便进行查看

```python
import os
import win32com.client

# 目标文件夹路径，包含需要读取目标属性的快捷方式
target_dir = r'E:\Users\TAGRENLA\Desktop\Google222'

# 创建COM对象
shell = win32com.client.Dispatch('WScript.Shell')

# 遍历目标目录中的所有文件
for filename in os.listdir(target_dir):
    if filename.endswith(".lnk"):  # 确保只处理快捷方式文件
        # 构造快捷方式的完整路径
        shortcut_path = os.path.join(target_dir, filename)

        # 读取快捷方式
        shortcut = shell.CreateShortCut(shortcut_path)

        # 输出快捷方式的详细属性
        print(f"快捷方式名称: {filename}")
        print(f"目标路径: {shortcut.TargetPath}")
        print(f"参数: {shortcut.Arguments}")
        print(f"工作目录: {shortcut.WorkingDirectory}")
        print(f"窗口样式: {shortcut.WindowStyle}")
        print(f"快捷键: {shortcut.Hotkey}")
        print(f"图标路径: {shortcut.IconLocation}")
        print(f"描述: {shortcut.Description}")
        # 如果有其他需要，可以继续添加属性输出

        print("----------")

```

![image-20240618113354595](https://tagrenla.oss-cn-beijing.aliyuncs.com/image-20240618113354595.png)

其实本质上就是添加参数在3.4，3.2中创建的快捷方式参数为空，所以还是会指向之前的快捷方式，并不是分身！

## 配置快捷方式参数

~~~python
import os
import win32com.client

# 目标文件夹路径，包含需要读取目标属性的快捷方式
target_dir = r'E:\Users\TAGRENLA\Desktop\Google'

# 创建COM对象
shell = win32com.client.Dispatch('WScript.Shell')

# 遍历目标目录中的所有文件
for filename in os.listdir(target_dir):
    if filename.endswith(".lnk"):  # 确保只处理快捷方式文件
        # 构造快捷方式的完整路径
        shortcut_path = os.path.join(target_dir, filename)

        # 读取快捷方式
        shortcut = shell.CreateShortCut(shortcut_path)

        # 输出快捷方式的详细属性
        print(f"快捷方式名称: {filename}")
        print(f"目标路径: {shortcut.TargetPath}")
        print(f"参数: {shortcut.Arguments}")
        print(f"工作目录: {shortcut.WorkingDirectory}")
        print(f"窗口样式: {shortcut.WindowStyle}")
        print(f"快捷键: {shortcut.Hotkey}")
        print(f"图标路径: {shortcut.IconLocation}")
        print(f"描述: {shortcut.Description}")
        # 如果有其他需要，可以继续添加属性输出

        print("----------")

~~~

# 提取文件夹中的所有的文件名称包括后缀！

~~~python

import os

# 文件夹路径
folder_path = r"E:\Users\TAGRENLA\Desktop\wodeshijie\PCL\minercraft\versions\1.20.1-Forge_47.3.0_原版生存\mods"

# 获取文件名和后缀
files_info = []
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        # 分割文件名和后缀
        name, extension = os.path.splitext(filename)
        files_info.append((name, extension))
# 输出文件名和后缀
for name, extension in files_info:
    print(f"{name}{extension}")
~~~

# Python密码生成器

- 生成密码在8-20包含大小写字母 数字

~~~python
import random
import string

def generate_password(min_length=8, max_length=20):
    # 确保至少包含一位数字、大写字母和小写字母
    numbers = random.choice(string.digits)
    uppercase_letters = random.choice(string.ascii_uppercase)
    lowercase_letters = random.choice(string.ascii_lowercase)
    
    # 剩余的字符随机选择
    remaining_length = random.randint(min_length, max_length) - 3
    all_characters = string.ascii_letters + string.digits
    remaining_characters = ''.join(random.choices(all_characters, k=remaining_length))
    
    # 拼接并打乱顺序
    password = numbers + uppercase_letters + lowercase_letters + remaining_characters
    password = ''.join(random.sample(password, len(password)))  # 打乱字符顺序
    
    return password

# 生成一个符合要求的密码
print("Generated password:", generate_password())


~~~

