% 光电效应数据拟合与普朗克常数计算
% 数据输入
v_data = [8.214, 7.408, 6.879, 5.49, 5.196]; % 频率，单位 10^14 Hz
U0_data = [-1.647, -1.318, -1.135, -0.607, -0.51]; % 截止电压，单位 V

% 取截止电压的绝对值
U0_abs = abs(U0_data);

% 转换频率到 Hz
nu = v_data * 1e14; % 频率，单位 Hz

% 线性拟合：|U0| = a * nu + b
p = polyfit(nu, U0_abs, 1); % 一次多项式拟合
a = p(1); % 斜率 (h/e)
b = p(2); % 截距 (-φ/e)

% 计算普朗克常数 h
e = 1.602e-19; % 电子电荷，单位 C
h_calculated = a * e; % 单位 J·s

% 计算拟合值
U0_fit = polyval(p, nu);

% 计算 R-squared 以评估拟合优度
ss_res = sum((U0_abs - U0_fit).^2);
ss_tot = sum((U0_abs - mean(U0_abs)).^2);
r_squared = 1 - (ss_res / ss_tot);

% 显示结果
fprintf('拟合结果:\n');
fprintf('斜率 a = %.4e V/Hz\n', a);
fprintf('截距 b = %.4f V\n', b);
fprintf('普朗克常数 h = %.4e J·s\n', h_calculated);
fprintf('R-squared = %.4f\n', r_squared);

% 绘制数据点和拟合直线（频率单位 10^14 Hz）
figure(2);
plot(v_data, U0_abs, 'r.', 'MarkerSize', 10, 'LineWidth', 0.8);
hold on;
v_fit = linspace(min(v_data), max(v_data), 100);
nu_fit = v_fit * 1e14;
U0_fit_v = polyval(p, nu_fit);
plot(v_fit, U0_fit_v, 'b-', 'LineWidth', 1.5);
xlabel('频率 \nu (10^{14} Hz)');
ylabel('截止电压 |U_0| (V)');
title('光电效应: |U_0| vs \nu');
legend('实验数据', '线性拟合', 'Location', 'northwest');
grid on;

% 添加暂停，等待用户查看图形
fprintf('\n图形已绘制。按任意键关闭图形并继续...\n');
pause;

% 关闭所有图形窗口（可选，如果需要自动关闭）
close all;
fprintf('图形已关闭。程序结束。\n');
