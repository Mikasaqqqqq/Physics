import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# -------------------------
# 数据输入
# -------------------------
L_k = np.array([0, 4.39, 8.63, 12.71, 16.92, 21.1, 25.52, 29.51, 34.01, 37.92])
U_k = np.array([1.52, 1.48, 1.36, 1.24, 1.12, 1.00, 0.88, 0.84, 0.80, 0.76])

# 平移 L_k
L_k_shifted = L_k + 60

# -------------------------
# 定义指数模型
# -------------------------
def exp_func(L, A, k, C):
    return A * np.exp(-k * L) + C

# -------------------------
# 拟合参数
# -------------------------
popt, pcov = curve_fit(exp_func, L_k_shifted, U_k, p0=(1.5, 0.02, 0.7))
A, k, C = popt

# 计算拟合优度 R²
residuals = U_k - exp_func(L_k_shifted, *popt)
ss_res = np.sum(residuals ** 2)
ss_tot = np.sum((U_k - np.mean(U_k)) ** 2)
R2 = 1 - ss_res / ss_tot

# -------------------------
# 拟合曲线生成
# -------------------------
L_fit = np.linspace(min(L_k_shifted), max(L_k_shifted), 300)
U_fit = exp_func(L_fit, *popt)

# -------------------------
# 全局样式设置
# -------------------------
plt.rcParams.update({
    'font.sans-serif': ['SimHei'],       # 中文字体
    'axes.unicode_minus': False,
    'axes.labelsize': 13,
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
    'axes.titlesize': 14,
    'legend.fontsize': 11
})

# -------------------------
# 绘图
# -------------------------
plt.figure(figsize=(8, 5.5), dpi=100)
# 实验点
plt.scatter(L_k_shifted, U_k,
            color="#2535E8", edgecolors='black',
            s=30,alpha=0.7 ,zorder=3, label='实验数据')
# 拟合曲线
plt.plot(L_fit, U_fit, color="#E31814",
         linewidth=1.5, zorder=2, label='指数拟合曲线')

# 坐标轴 & 网格美化
plt.grid(alpha=0.25, linestyle='--')
plt.xlabel("L$_k$ / mm")
plt.ylabel("U$_k$ / V")
plt.title("波长幅度拟合曲线", pad=10)



# 图例放右上角
plt.legend(loc='upper right', frameon=False)

plt.tight_layout()
plt.show()

# -------------------------
# 输出参数
# -------------------------
print(f"A = {A:.4f}, k = {k:.4f}, C = {C:.4f}, R² = {R2:.4f}")
