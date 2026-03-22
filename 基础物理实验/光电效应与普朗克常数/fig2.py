import matplotlib.pyplot as plt
import numpy as np

# 数据定义
wavelengths = [365.0, 404.7, 435.8, 546.1, 577.0]  # 波长 (nm)
U_AK = [-1, 0, 1, 5, 10, 15, 20, 25, 30]  # 电压 (V)

# 电流数据 (×10^-11 A)
currents = [
    [8.5, 36.4, 67.2, 215, 350, 471, 570, 652, 711],    # 365nm
    [1.4, 11, 23.5, 70.7, 113.2, 151.6, 181.2, 205, 220], # 404.7nm
    [2.1, 30.4, 68.2, 195, 309, 408, 482, 538, 569],    # 435.8nm
    [0.1, 2.3, 7.7, 21.9, 31.4, 37.5, 40.8, 43.1, 44.2], # 546.1nm
    [-0.1, 0.9, 4.2, 11.8, 16.7, 19.5, 21, 22.1, 22.8]   # 577nm
]

# 创建图形
plt.figure(figsize=(12, 8))

# 颜色列表
colors = ['blue', 'red', 'green', 'orange', 'purple']

# 绘制每条曲线
for i, (wavelength, current_data, color) in enumerate(zip(wavelengths, currents, colors)):
    plt.plot(U_AK, current_data, 
             marker='o', 
             linewidth=2, 
             markersize=6,
             color=color,
             label=f'{wavelength} nm')

# 设置图表属性
plt.xlabel(r'$\mathrm{U_{AK}}$ (V)', fontsize=12)
plt.ylabel('I (×10$^{-11}$ A)', fontsize=12)
plt.title('Photoelectric Effect: Current vs Voltage at Different Wavelengths', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=10)

# 设置坐标轴范围
plt.xlim(-2, 32)
plt.ylim(-20, 750)

# 添加次要网格
plt.minorticks_on()
plt.grid(True, which='minor', alpha=0.2)

plt.tight_layout()
plt.show()

# 可选：分别绘制每个波长的图表
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

for i, (wavelength, current_data, color) in enumerate(zip(wavelengths, currents, colors)):
    axes[i].plot(U_AK, current_data, 
                 marker='o', 
                 linewidth=2, 
                 markersize=6,
                 color=color)
    axes[i].set_title(f'{wavelength} nm', fontsize=12)
    axes[i].set_xlabel(r'$U_{AK}$ (V)')
    axes[i].set_ylabel('I (×10$^{-11}$ A)')
    axes[i].grid(True, alpha=0.3)
    axes[i].set_xlim(-2, 32)

# 隐藏多余的子图
for i in range(len(wavelengths), 6):
    axes[i].set_visible(False)

plt.tight_layout()
plt.show()
