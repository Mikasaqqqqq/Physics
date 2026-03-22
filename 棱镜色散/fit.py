import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from scipy.optimize import curve_fit

# ---- 可选：设置中文字体以避免乱码（会自动选可用字体） ----
preferred = ["Microsoft YaHei", "SimHei", "Noto Sans CJK SC", "PingFang", "WenQuanYi Zen Hei"]
available = {f.name for f in fm.fontManager.ttflist}
for name in preferred:
    if name in available:
        plt.rcParams['font.sans-serif'] = [name]
        plt.rcParams['font.family'] = 'sans-serif'
        break
plt.rcParams['axes.unicode_minus'] = False

# 实验数据
lam = np.array([579.1, 577.0, 546.1, 435.8, 404.7])  # nm
n = np.array([1.6739, 1.6745, 1.6818, 1.6864, 1.6996])

# 构造矩阵
x1 = lam ** (-2)
x2 = lam ** (-4)
m = len(lam)

# 正态方程矩阵
M = np.array([
    [m, np.sum(x1), np.sum(x2)],
    [np.sum(x1), np.sum(x1**2), np.sum(x1*x2)],
    [np.sum(x2), np.sum(x1*x2), np.sum(x2**2)]
])
Y = np.array([
    np.sum(n),
    np.sum(x1 * n),
    np.sum(x2 * n)
])

# 解方程组，求 A, B, C
A, B, C = np.linalg.solve(M, Y)
print(f"A = {A:.6f},  B = {B:.6e},  C = {C:.6e}")

# 拟合曲线
lam_fit = np.linspace(400, 600, 300)
n_fit = A + B / lam_fit**2 + C / lam_fit**4

# 绘图
plt.scatter(lam, n, color='red', label='实验数据')
plt.plot(lam_fit, n_fit, color='blue', label='柯西公式拟合', linewidth=1.5)
plt.xlabel('波长 λ (nm)')
plt.ylabel('折射率 n')
plt.title('折射率-波长关系（柯西公式拟合）')
plt.legend()
plt.grid(True)
plt.show()

