#  批量创建Chrome浏览器分身

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
