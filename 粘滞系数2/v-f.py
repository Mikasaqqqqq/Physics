import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
matplotlib.rcParams['axes.unicode_minus'] = False   # 正常显示负号
# 实验数据
v = np.array([0.51, 0.66, 1.10, 1.47, 1.76, 2.02, 2.24, 2.48, 2.71, 2.87, 3.06, 3.28])  # m/s
f = np.array([7.85, 10.58, 15.63, 20.05, 24.04, 27.62, 30.86, 33.94, 36.76, 39.47, 41.67, 43.86])  # Hz

# 一次线性拟合（v = k*f + b）
p = np.polyfit(f, v, 1)
k, b = p

# 计算拟合值和 R²
v_pred = np.polyval(p, f)
ss_res = np.sum((v - v_pred)**2)
ss_tot = np.sum((v - np.mean(v))**2)
r2 = 1 - ss_res/ss_tot

# 生成适当外推的数据范围
f_fit = np.linspace(min(f) - 5, max(f) + 5, 200)
v_fit = np.polyval(p, f_fit)

# 绘图
plt.figure(figsize=(7,5))
plt.scatter(f, v, color='b', label='实验数据')
plt.plot(f_fit, v_fit, 'r-', linewidth=1.5, 
         label=f'拟合: v = {k:.4f}f + {b:.4f}')
plt.xlabel('频率 f (Hz)')
plt.ylabel('风速 v (m/s)')
plt.title('v-f')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 输出结果
print(f"线性拟合方程: v = {k:.4f} * f + {b:.4f}")
# print(f"拟合优度 R² = {r2:.4f}")
