import math

a=float(input())
b=float(input())
t=float(input())

D=(a-b)/2/math.sqrt(2)*0.001
V=5

h0=2.0
h1=29.0
h2=21.5

Deltap=1000*9.8*(0.5*(h1+h2)-h0)*0.01


print(math.pi*(D**4)*Deltap*t/(128*0.3*50*0.000001))
print(0.6*((43.252+20)**(-1.54)))
