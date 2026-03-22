import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
matplotlib.rcParams['axes.unicode_minus'] = False   # 正常显示负号

# 实验数据
frequencies = np.array([8.214, 7.408, 6.879, 5.49, 5.196])  # ×10^14 Hz
cutoff_voltages = np.array([-1.647, -1.318, -1.135, -0.574, -0.462])  # V
cutoff_voltages = -cutoff_voltages  # 转为正值

# 转换为实际频率 (Hz)
frequencies_actual = frequencies * 1e14

# 定义线性拟合函数 (光电效应方程: U_0 = (h/e)ν - W_0/e)
def linear_func(nu, slope, intercept):
    return slope * nu + intercept
# 
# 进行线性拟合
popt, pcov = curve_fit(linear_func, frequencies_actual, cutoff_voltages)
slope, intercept = popt
slope_err, intercept_err = np.sqrt(np.diag(pcov))

# 计算物理参数
e = 1.602e-19  # 电子电荷量 (C)
h = slope * e  # 普朗克常数
W_0 = -intercept * e  # 逸出功 (J)
W_0_ev = W_0 / e      # 逸出功 (eV)

# 计算截止频率 (当U_0=0时的频率)
nu_0 = -intercept / slope  # 截止频率 (Hz)
nu_0_thz = nu_0 / 1e12     # 转换为 THz

# 计算相对误差 (与标准值比较)
h_standard = 6.626e-34  # 标准普朗克常数
h_error = abs((h - h_standard) / h_standard) * 100

print("=" * 50)
print("光电效应实验数据分析结果")
print("=" * 50)
print(f"拟合直线方程: U₀ = ({slope:.3e} ± {slope_err:.3e})ν + ({intercept:.3f} ± {intercept_err:.3f})")
print(f"斜率: {slope:.3e} ± {slope_err:.3e} V/Hz")
print(f"截距: {intercept:.3f} ± {intercept_err:.3f} V")
print("=" * 50)
print(f"普朗克常数 h = {h:.3e} J·s")
print(f"相对误差: {h_error:.2f}%")
print(f"逸出功 W₀ = {W_0:.3e} J = {W_0_ev:.3f} eV")
print(f"截止频率 ν₀ = {nu_0:.3e} Hz = {nu_0_thz:.2f} THz")
print("=" * 50)

# 绘制拟合图像
plt.figure(figsize=(9, 6))

# 绘制数据点
plt.scatter(frequencies, cutoff_voltages, color="blue", alpha=0.7, s=20, 
            label='Data points', zorder=5)

# 绘制拟合直线（延长到截止频率之前）
freq_fit = np.linspace(nu_0/1e14 - 0.5, 9.0, 200)  # 延长到截止频率前0.5
freq_fit_actual = freq_fit * 1e14
voltage_fit = linear_func(freq_fit_actual, slope, intercept)

plt.plot(freq_fit, voltage_fit, color="blue", alpha=0.8, linewidth=2, 
         label=r'Fiting curve: $\mathrm{|U_0|} = \frac{h}{e}\nu - \frac{W_0}{e}$', zorder=4)

# 标注截止频率点
plt.axhline(y=0, color="orange", linestyle='--', alpha=0.7, linewidth=2)
plt.axvline(x=nu_0/1e14, color="red", linestyle='--', alpha=0.7, linewidth=2,
           label=fr'Cut-off Voltage: $\nu_0 = {nu_0/1e14:.2f} \times 10^{{14}}$ Hz')

# 在截止频率点添加标记点
plt.scatter([nu_0/1e14], [0], color='black', s=15, alpha=0.8, zorder=6, marker='x')

# 添加截止频率点的数值标注
plt.annotate(f'$\\nu_0 = {nu_0/1e14:.2f} \\times 10^{{14}}$ Hz', 
             xy=(nu_0/1e14, 0), 
             xytext=(nu_0/1e14 + 0.1, -0.1), 
             fontsize=15 
            #  arrowprops=dict(arrowstyle='->', color='orange', alpha=0.7, lw=1),
             )

plt.xlabel(r'frequency $\nu (\times 10^{-14} \mathrm{Hz})$', fontsize=12)
plt.ylabel(r'Cut-off Voltage $\mathrm{|U_0| (V)}$', fontsize=12)
plt.title('Photoelectric Effect: Cut-off Voltage vs Frequency', fontsize=14, fontweight='bold')

plt.legend(loc='lower right', fontsize=12)
plt.grid(True ,alpha=0.2)
plt.tight_layout()

# 设置坐标轴范围，确保显示截止频率点
plt.xlim(nu_0/1e14 - 0.8, 8.8)
plt.ylim(-0.2, max(cutoff_voltages) + 0.2)
plt.minorticks_on()
plt.grid(True, which='minor', alpha=0.2)

plt.show()
