import tkinter as tk
from tkinter import ttk, messagebox


def calculate_blood_type(father, mother):
    blood_type_chart = {
        ('A', 'A'): ['A', 'O'],
        ('A', 'B'): ['A', 'B', 'AB', 'O'],
        ('A', 'O'): ['A', 'O'],
        ('A', 'AB'): ['A', 'B', 'AB'],
        ('B', 'B'): ['B', 'O'],
        ('B', 'O'): ['B', 'O'],
        ('B', 'AB'): ['A', 'B', 'AB'],
        ('O', 'O'): ['O'],
        ('O', 'AB'): ['A', 'B'],
        ('AB', 'AB'): ['A', 'B', 'AB'],
    }

    possible_blood_types = blood_type_chart.get((father, mother), blood_type_chart.get((mother, father), []))
    return possible_blood_types


def on_calculate():
    father = father_var.get()
    mother = mother_var.get()
    if not father or not mother:
        messagebox.showerror("错误", "请选择父母的血型")
        return

    possible_blood_types = calculate_blood_type(father, mother)
    messagebox.showinfo("计算结果", f"可能的血型: {', '.join(possible_blood_types)}")


# 创建主窗口
root = tk.Tk()
root.title("绿帽子检测器")
root.geometry("300x250")

# 标签
tk.Label(root, text="男方血型:").pack(pady=5)
father_var = ttk.Combobox(root, values=['A', 'B', 'O', 'AB'])
father_var.pack()

tk.Label(root, text="女方血型:").pack(pady=5)
mother_var = ttk.Combobox(root, values=['A', 'B', 'O', 'AB'])
mother_var.pack()

# 按钮
tk.Button(root, text="开始检测，做好心理纯呗呦！！！", command=on_calculate).pack(pady=10)

# 运行主循环
root.mainloop()