% 风速-频率数据
v = [0.51 0.66 1.10 1.47 1.76 2.02 2.24 2.48 2.71 2.87 3.06 3.28]; % m/s
f = [7.85 10.58 15.63 20.05 24.04 27.62 30.86 33.94 36.76 39.47 41.67 43.86]; % Hz

% 线性拟合（v = k*f + b）
p = polyfit(f, v, 1);  % 注意这里自变量是 f
k = p(1);  % 斜率
b = p(2);  % 截距

% 生成拟合曲线
f_fit = linspace(min(f), max(f), 100);
v_fit = polyval(p, f_fit);

% 绘图
figure;
plot(f, v, 'o', 'MarkerFaceColor', 'b', 'DisplayName', '实验数据');
hold on;
plot(f_fit, v_fit, 'r-', 'LineWidth', 1.5, ...
    'DisplayName', sprintf('拟合: v = %.4f f + %.4f', k, b));
xlabel('频率 f (Hz)');
ylabel('风速 v (m/s)');
title('风速-频率 线性拟合（v 对 f）');
legend('Location', 'best');
grid on;

% 输出拟合参数
fprintf('线性拟合方程: v = %.4f * f + %.4f\n', k, b);
