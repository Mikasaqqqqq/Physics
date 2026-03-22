% 第一条曲线的拟合和绘制
[xData1, yData1] = prepareCurveData( x, y4 );
% 设置 fittype 和选项
ft1 = fittype( 'smoothingspline' );
% 对数据进行模型拟合
[fitresult1, gof1] = fit( xData1, yData1, ft1 );

% 第二条曲线的拟合
[xData2, yData2] = prepareCurveData( x, z4 );
% 设置 fittype 和选项
ft2 = fittype( 'smoothingspline' );
% 对数据进行模型拟合
[fitresult2, gof2] = fit( xData2, yData2, ft2 );

% 创建新的图形窗口
figure( 'Name', 'Combined Fit Plot' );

% 绘制第一条拟合曲线
h1 = plot(fitresult1);
% 设置第一条曲线颜色为紫色，不显示数据点
set(h1, 'Color', [0.5 0 0.5], 'Marker', 'none');

% 保持当前图形，以便后续绘图添加到同一图中
hold on;

% 绘制第二条拟合曲线
h2 = plot(fitresult2);
% 设置第二条曲线颜色为橙色，不显示数据点
set(h2, 'Color', [1 0.65 0], 'Marker', 'none');

% 添加图例，更新曲线名称
legend([h1, h2], '黄蓝滤镜叠加', '黄、蓝滤镜透过率相乘', 'Location', 'NorthEast', 'Interpreter', 'none');


xlabel( '光强', 'Interpreter', 'none' );
ylabel( '透过率', 'Interpreter', 'none' );

% 打开网格线
grid on;

% 释放图形窗口
hold off;
