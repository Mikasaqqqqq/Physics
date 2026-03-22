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

# ---------------- 1) v-f 校准数据（之前给出的） ----------------
v_cal = np.array([0.51, 0.66, 1.10, 1.47, 1.76, 2.02, 2.24, 2.48, 2.71, 2.87, 3.06, 3.28])  # m/s
f_cal = np.array([7.85, 10.58, 15.63, 20.05, 24.04, 27.62, 30.86, 33.94, 36.76, 39.47, 41.67, 43.86])  # Hz

# 线性拟合 v = k * f + b
p_cal = np.polyfit(f_cal, v_cal, 1)
k_cal, b_cal = p_cal
def v_from_f(f):
    return np.polyval(p_cal, f)

print(f"校准: v = {k_cal:.6f} * f + {b_cal:.6f}  (m/s)")

# ---------------- 2) 两组实验数据（从你图片提取） ----------------
# 球1（表1）
m1_g = 2.768          # mg
D1_cm = 4.01          # 球径 cm
L1_cm = 16            # 悬线长 cm，请根据实际修改
f1 = np.array([7.25, 9.85, 14.79, 19.23, 23.15, 26.88, 30.34, 33.56, 36.59, 39.27, 41.84, 44.25])
delta_d1_cm = np.array([0.10, 0.20, 0.25, 0.40, 0.55, 0.80, 1.00, 1.20, 1.30, 1.50, 1.70, 2.20])

# 球2（表2）
m2_g = 3.134
D2_cm = 3.608
L2_cm = 17
f2 = np.array([7.85, 10.58, 15.63, 20.05, 24.04, 27.65, 31.06, 34.25, 37.04, 39.68, 42.02, 44.44])
delta_d2_cm = np.array([0.05, 0.09, 0.20, 0.30, 0.45, 0.60, 0.80, 1.00, 1.20, 1.40, 1.50, 1.70])

# ---------------- 3) 常量与单位转换 ----------------
g = 9.80665                 # 重力加速度 m/s^2
rho_air = 1.225             # 空气密度 kg/m^3（按需修改）
mu_air = 1.81e-5            # 动粘度 Pa·s（按需修改）

# 单位转换
m1 = m1_g / 1000.0
m2 = m2_g / 1000.0
D1 = D1_cm / 100.0
D2 = D2_cm / 100.0
L1 = L1_cm / 100.0
L2 = L2_cm / 100.0
delta1 = delta_d1_cm / 100.0
delta2 = delta_d2_cm / 100.0

A1 = np.pi * (D1**2) / 4.0
A2 = np.pi * (D2**2) / 4.0

# 校验 delta < L
if np.any(delta1 >= L1):
    raise ValueError("球1存在 delta >= L1，请检查数据/单位")
if np.any(delta2 >= L2):
    raise ValueError("球2存在 delta >= L2，请检查数据/单位")

# ---------------- 4) 计算：v, F_D(严格tan), Re, C_D ----------------
v1 = v_from_f(f1)
v2 = v_from_f(f2)

# 严格关系：tan(theta) = delta / sqrt(L^2 - delta^2)
tan1 = delta1 / L1
tan2 = delta2 / L2

Fd1 = m1 * g * tan1
Fd2 = m2 * g * tan2

Re1 = rho_air * v1 * D1 / mu_air
Re2 = rho_air * v2 * D2 / mu_air

Cd1 = 2.0 * Fd1 / (rho_air * A1 * v1**2)
Cd2 = 2.0 * Fd2 / (rho_air * A2 * v2**2)

# ---------------- 5) 绘图：Cd vs Re（对数坐标） ----------------
plt.figure(figsize=(8,6))
plt.loglog(Re1, Cd1, 'o-', label=f'球1 D={D1*100:.2f} cm, m={m1_g:.3f} g')
plt.loglog(Re2, Cd2, 's--', label=f'球2 D={D2*100:.3f} cm, m={m2_g:.3f} g')
plt.xlabel('Reynolds number $Re$')
plt.ylabel('Drag coefficient $C_D$')
plt.title('球面阻力系数 $C_D$ 随雷诺数 $Re$ 的变化')
plt.grid(True, which='both', ls=':', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()

# ---------------- 6) 打印表格结果 ----------------
print("\n--- 球1 结果 (f Hz, v m/s, Δd m, F_D N, Re, C_D) ---")
for i in range(len(f1)):
    print(f"{f1[i]:5.2f} , {v1[i]:.3f} , {delta1[i]:.4f} , {Fd1[i]:.6e} , {Re1[i]:.1f} , {Cd1[i]:.4f}")

print("\n--- 球2 结果 (f Hz, v m/s, Δd m, F_D N, Re, C_D) ---")
for i in range(len(f2)):
    print(f"{f2[i]:5.2f} , {v2[i]:.3f} , {delta2[i]:.4f} , {Fd2[i]:.6e} , {Re2[i]:.1f} , {Cd2[i]:.4f}")
