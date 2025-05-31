import matplotlib.pyplot as plt
import numpy as np

# 设置数轴范围和标记点
start = 15  # 数轴起点
end = 50  # 数轴终点
points = [50,
          33.3,
          25,
          20,
          10,
          12.5,
          11.1,9.1,8.3,7.7,
          6.25,14.3,7.1,16.7,
          5.9,5.6,5.3,
          6.7,
          28.6,13.3,22.2,11.8,18.2,10.5,15.4,9.5,37,42,]  # 要标记的点
'''
          
'''
# 创建图形和坐标轴
fig, ax = plt.subplots(figsize=(15, 2))

# 绘制数轴
ax.axhline(y=0, color='k', linewidth=0.8)  # 绘制水平的数轴
ax.set_xlim(start, end)  # 设置数轴范围

# 隐藏上、右边框
ax.spines[['top', 'right']].set_visible(False)

# 设置x轴刻度位置（包括小数）
ax.xaxis.set_ticks(np.arange(start, end + 1, 1))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.5))  # 小刻度线

# 绘制刻度线和标签
ax.xaxis.set_ticks_position('bottom')
ax.tick_params(axis='x', direction='out', which='both', length=5)
ax.tick_params(axis='x', which='minor', length=3)

# 标记指定的点
for point in points :
    # 绘制标记点（红色圆点）
    if point >= 15:                   # 修改这里  的大于还是小于
        ax.plot(point, 0, 'ro', markersize=8)

        # 添加数值标签（在点上方向偏移显示）
        ax.text(point, 0.08, str(point),
                ha='center', va='bottom', fontsize=18, color='blue',
                bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', boxstyle='round,pad=0.2'))

# 在数轴末端添加箭头
ax.arrow(end, 0, 0.1, 0, head_width=0.3, head_length=0.2,
         fc='k', ec='k', linewidth=0.8, clip_on=False)
ax.arrow(start, 0, -0.1, 0, head_width=0.3, head_length=0.2,
         fc='k', ec='k', linewidth=0.8, clip_on=False)

# 添加标题（可选）
# plt.title('Number Line with Marked Points', pad=20)

# 调整布局并显示
plt.tight_layout()
plt.show()
