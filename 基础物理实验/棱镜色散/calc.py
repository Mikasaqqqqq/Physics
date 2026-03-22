import numpy as np

# 数据
lam = np.array([579.1, 577.0, 546.1, 435.8, 404.7])
n_exp = np.array([1.6739, 1.6745, 1.6818, 1.6864, 1.6996])

# 柯西公式系数
A, B, C = 1.6864, -8.6672e3, 1.7389e9

# 计算拟合值
n_fit = A + B/lam**2 + C/lam**4

# 计算误差指标
residual = n_fit - n_exp
rmse = np.sqrt(np.mean(residual**2))  # 均方根误差
r2 = 1 - np.sum(residual**2) / np.sum((n_exp - np.mean(n_exp))**2)

print(n_fit, rmse, r2)
