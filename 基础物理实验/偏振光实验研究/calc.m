theta = xlsread("data.xlsx","sheet1","B1:AL1"); 
r = xlsread("data.xlsx","sheet1","B16:AL16"); 
theta=theta/180*pi
polarplot(theta,r)