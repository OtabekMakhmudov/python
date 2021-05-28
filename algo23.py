from math import *
a, b, c, d, x = input().split()
a, b, c, d = int(a), int(b), int(c), int(d)
x = float(x)
if a ==0 and b == 0:
	pass
	y2 = cos(fabs((a*x+b)/(c*x+d+pow(2,c))))
	print("%.2f" %y2)
else:
	y2 = (a*x*x+b*x+c)/(x*a**3+a*a+pow(a,b-c))+cos(fabs((a*x+b)/(c*x+d+pow(2,c))))
	print("%.2f" %y2)
