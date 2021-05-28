from math import *
x, y, z = input().split()
x = int(x)
y = float(y)
z = float(z)
AF = pow(2,-x)*(pow((x+pow((fabs(y)+2),1/4)),1/2))*(pow((((exp(x-1))/(sin(z+2)))+2),1/3))
print('%.2f' %AF)