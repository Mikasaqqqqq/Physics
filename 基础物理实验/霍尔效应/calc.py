import numpy as np
import matplotlib.pyplot as plt

# ================= 中文与负号 =================
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# =============================================

# 实验数据（来自表格最后两列）
B = np.array([52.1, 102.05, 152.7, 202.6, 253.925, 305.0, 365.525, 417.55])  # mT
U_H = np.array([-11.725, -23.35, -34.65, -46.075, -57.9, -70.025, -83.75, -95.875])  # mV

# ================= 最小二乘线性拟合 =================
k, b = np.polyfit(B, U_H, 1)      # 斜率和截距
r = np.corrcoef(B, U_H)[0, 1]     # 相关系数

# 拟合曲线
B_fit = np.linspace(B.min(), B.max(), 200)
U_fit = k * B_fit + b

# ======================== 作图 ========================
plt.figure(figsize=(6.5, 4.2))

# 实验数据点
plt.scatter(B, U_H, color='r', s=35, label='data')

# 拟合直线（细线）
plt.plot(
    B_fit, U_fit,
    color='b',
    linewidth=1.2
)

# 坐标轴与标题
plt.xlabel(r'$B\ /\ \mathrm{mT}$')
plt.ylabel(r'$U_H\ /\ \mathrm{mV}$')
plt.title(r'$U_H - B$ 曲线')

# 网格
plt.grid(True, linestyle=':', linewidth=0.6)

plt.legend(fontsize=9)
plt.tight_layout()
plt.show()

# ======================== 输出结果 ========================
print(f"拟合结果：U_H = k B + b")
print(f"斜率 k = {k:.5f} mV/mT")
print(f"截距 b = {b:.5f} mV")
print(f"相关系数 r = {r:.6f}")
