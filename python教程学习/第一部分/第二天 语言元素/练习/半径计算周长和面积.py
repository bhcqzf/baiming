#给圆的半径，计算周长和面积
import math
r=float(input("请输入圆的半径："))
C=2*math.pi*r
S=math.pi*(r**2)
# C=2*3.14*r
# S=3.14*(r**2)
print('该圆的周长为%.1f，该圆的面积为%.1f'%(C,S))