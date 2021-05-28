from math import *
a, b, c, d, x = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
x = float(x)
#y2 = (a*x*x+b*x+c)/(x*a*a*a+a*a+pow(a,(b-c)))+(cos(fabs((a*x+b)/(c*x+d+pow(2,c)))))
x1 = a*x*x+b*x+c
x2 = x*a**3+a*a+(pow(a,(b-c)))
x3 = fabs((a*x+b)/(c*x+d+pow(2,c)))
x4 = cos(x3)
y2 = x1/x2+x4
print('%.2f' %y2)