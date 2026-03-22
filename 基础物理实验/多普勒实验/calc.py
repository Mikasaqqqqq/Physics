import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# ---- 可选：设置中文字体以避免乱码（会自动选可用字体） ----
preferred = ["Microsoft YaHei", "SimHei", "Noto Sans CJK SC", "PingFang", "WenQuanYi Zen Hei"]
available = {f.name for f in fm.fontManager.ttflist}
for name in preferred:
    if name in available:
        plt.rcParams['font.sans-serif'] = [name]
        plt.rcParams['font.family'] = 'sans-serif'
        break
plt.rcParams['axes.unicode_minus'] = False

# 数据
L = np.array([29.2, 40.7, 52, 68.4]) / 100  # 摆长，转为米
T = np.array([1.19, 1.32, 1.58, 1.76])      # 周期，单位秒

# 计算 T^2
T2 = T**2

# 线性拟合 T^2 = k * L
coef = np.polyfit(L, T2, 1)  # coef[0] = k, coef[1] = b
k, b = coef
g = 4 * np.pi**2 / k

print(f"拟合直线：T² = {k:.4f} * L + {b:.4f}")
print(f"计算得到的重力加速度 g = {g:.4f} m/s²")

# 绘制拟合图
L_fit = np.linspace(min(L), max(L), 100)
T2_fit = k * L_fit + b

plt.scatter(L, T2, color='blue', label='实验数据')
plt.plot(L_fit, T2_fit, color='red', label=f'拟合曲线\n$T^2 = {k:.3f}L + {b:.3f}$')
plt.xlabel('摆长 L (m)')
plt.ylabel('$T^2$ (s²)')
plt.title('单摆周期平方与摆长的关系')
plt.legend()
plt.grid(True)
plt.show()
