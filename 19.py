from math import *
a, x, y = input().split()
a = int(a)
x = float(x)
y = float(y)
TT = pow((y*y+exp(x)+pow((exp(x)+a/(x*x+2)),1/2)+(pow((cos(x)),2)/(sin(x*x)))),1/2)+pow((cos(x)),3)
print('%.2f' %TT)