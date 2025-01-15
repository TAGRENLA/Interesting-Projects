# ecoding:utf-8
import folium
from tkinter import Tk, Label, Button, messagebox, ttk, Text, Scrollbar, Menu


def create_map_from_user_input(data, output_file="map.html"):
    """
    根据用户输入的数据生成地图标记，并将地图聚焦到所有点的中心点。
    :param data: 包含纬度、经度和地点名称的列表。
    :param output_file: 输出地图文件名。
    """
    try:
        # 计算所有点的纬度和经度的平均值
        total_lat = 0
        total_lon = 0
        num_points = len(data)

        for row in data:
            total_lat += float(row[0])
            total_lon += float(row[1])

        # 计算中心点坐标
        center_lat = total_lat / num_points
        center_lon = total_lon / num_points

        # 初始化地图，聚焦到中心点
        my_map = folium.Map(location=[center_lat, center_lon], zoom_start=5)

        # 遍历数据添加标记
        for row in data:
            try:
                lat, lon, name = float(row[0]), float(row[1]), row[2]
                folium.Marker(
                    [lat, lon],
                    popup=name,
                    tooltip=name
                ).add_to(my_map)
            except Exception as e:
                print(f"错误：标记 {row[2]} 失败。原因：{e}")

        # 保存地图到文件
        my_map.save(output_file)
        messagebox.showinfo("完成", f"地图已生成并保存为 {output_file}")
    except Exception as e:
        messagebox.showerror("错误", f"生成地图失败：{str(e)}")


def add_location():
    """
    将用户输入的数据添加到表格中。
    """
    user_input = entry.get("1.0", "end-1c").strip()  # 获取多行输入框中的内容
    if not user_input:
        messagebox.showwarning("警告", "请输入地点信息！")
        return

    lines = user_input.splitlines()  # 按行分割输入数据
    for line in lines:
        try:
            # 去除每行的前后空格
            line = line.strip()
            if line:
                lat, lon, name = line.split(",")
                lat, lon = float(lat), float(lon)  # 校验经纬度格式

                # 添加到表格
                table.insert("", "end", values=(lat, lon, name))
        except ValueError:
            messagebox.showerror("错误", "输入格式错误！请使用 纬度,经度,地点名称 的格式。")
            return

    # 清空输入框
    entry.delete("1.0", "end")


def generate_map():
    """
    从表格中获取数据并生成地图。
    """
    data = []
    for row in table.get_children():
        values = table.item(row, "values")
        data.append(values)

    if not data:
        messagebox.showwarning("警告", "表格中没有数据！请先添加地点信息。")
        return

    create_map_from_user_input(data)


def clear_all_locations():
    """
    清空表格中的所有地点信息。
    """
    for row in table.get_children():
        table.delete(row)
    messagebox.showinfo("完成", "所有地点信息已清空。")


def delete_selected_location(event):
    """
    删除选中的地点信息。
    """
    selected_item = table.selection()
    if selected_item:
        table.delete(selected_item)
        messagebox.showinfo("完成", "选中的地点信息已删除。")
    else:
        messagebox.showwarning("警告", "请选择要删除的地点信息。")


# 创建 GUI 界面
root = Tk()
root.title("全球范围地图标记软件【作者：S64959】")
root.geometry("800x600")  # 设置窗口大小

# 提示标签
Label(root, text="请输入地点信息（格式：纬度,经度,地点名称，每次输入一条）").pack(pady=10)

# 创建框架以对齐输入框和表格
frame = ttk.Frame(root)
frame.pack(fill="both", expand=True, padx=10, pady=10)

# 多行输入框，允许输入多个地点，宽度适配
entry = Text(frame, height=8)  # 增大输入框，宽度不指定，使用pack填充
entry.pack(side="left", fill="both", expand=True, pady=5)

# 输入框的滚动条
scrollbar_input = Scrollbar(frame, orient="vertical", command=entry.yview)
scrollbar_input.pack(side="right", fill="y")
entry.config(yscrollcommand=scrollbar_input.set)

# 添加按钮
Button(root, text="添加地点", command=add_location, width=15).pack(pady=5)

# 清空按钮
Button(root, text="清空所有地点", command=clear_all_locations, width=15).pack(pady=5)

# 表格显示区域
frame_table = ttk.Frame(root)
frame_table.pack(fill="both", expand=True, padx=10, pady=10)

# 添加滚动条
scrollbar_y = ttk.Scrollbar(frame_table, orient="vertical")
scrollbar_y.pack(side="right", fill="y")

scrollbar_x = ttk.Scrollbar(frame_table, orient="horizontal")
scrollbar_x.pack(side="bottom", fill="x")

# 表格组件
table = ttk.Treeview(frame_table, columns=("纬度", "经度", "地点名称"), show="headings",
                     yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
table.pack(fill="both", expand=True)

# 配置滚动条
scrollbar_y.config(command=table.yview)
scrollbar_x.config(command=table.xview)

# 表头配置
table.heading("纬度", text="纬度")
table.heading("经度", text="经度")
table.heading("地点名称", text="地点名称")

# 表格列宽自动调整
table.column("纬度", width=150)
table.column("经度", width=150)
table.column("地点名称", width=300)

# 生成地图按钮
Button(root, text="生成地图", command=generate_map, width=15).pack(pady=10)

# 右键菜单
right_click_menu = Menu(root, tearoff=0)
right_click_menu.add_command(label="删除选中的地点", command=lambda: delete_selected_location(None))


def show_right_click_menu(event):
    right_click_menu.post(event.x_root, event.y_root)


# 绑定右键事件
table.bind("<Button-3>", show_right_click_menu)

root.mainloop()
