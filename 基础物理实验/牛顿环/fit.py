import numpy as np
import matplotlib.pyplot as plt

# ---------------------------
# 实验数据
# ---------------------------
k = np.array([10, 15, 20, 25, 30, 35, 40], dtype=float)

xL = np.array([31.454, 32.034, 32.539, 32.993, 33.42, 33.729, 34.056])
xR = np.array([24.788, 24.162, 23.618, 23.151, 22.74, 22.326, 21.951])

# 计算弦长与弦长平方
l = xL - xR               # mm
l2 = l**2                 # mm^2

# ---------------------------
# 线性拟合 l_k^2 = A k + B
# ---------------------------
A, B = np.polyfit(k, l2, 1)

# 拟合结果
l2_fit = A * k + B

# ---------------------------
# 计算 R^2
# ---------------------------
ss_res = np.sum((l2 - l2_fit)**2)
ss_tot = np.sum((l2 - np.mean(l2))**2)
R2 = 1 - ss_res / ss_tot

# ---------------------------
# 计算曲率半径 R
# A = 4 λ R   →  R = A/(4 λ)
# λ = 589.3 nm = 589.3e-6 mm
# ---------------------------
lam = 589.3e-6   # mm
R = A / (4 * lam) / 1000   # 转换为 m

# 偏心修正量 s（若 B>0 则一般可忽略）
if B < 0:
    s = np.sqrt(-B / 4)
else:
    s = None

# ---------------------------
# 输出结果
# ---------------------------
print("拟合方程: $l_k^2$ = {:.6f} k + {:.6f}".format(A, B))
print("曲率半径 R = {:.4f} m".format(R))
print("决定系数 R^2 = {:.6f}".format(R2))

if s is not None:
    print("偏心修正量 s = {:.4f} mm".format(s))
else:
    print("B > 0, 偏心修正项可忽略，不计算 s。")

# ---------------------------
# 美观绘图
# ---------------------------
plt.figure(figsize=(7,5))
plt.scatter(k, l2, color='r', marker='.', s=80, label="Data")
plt.plot(k, l2_fit, linewidth=2, label="Fit")
plt.xlabel("k", fontsize=12)
plt.ylabel("$l_k^2\ (\mathrm{mm}^2)$", fontsize=12)
plt.title("Newton Rings Linear Fit", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()
