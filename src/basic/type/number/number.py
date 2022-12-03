from math import *
import random

# python 支持的数字类型有：int, float, complex
# int 是整数，无长度限制
# float 是浮点数，可以使用科学记数法，使用e表示10次方
# complex 表示虚数，j表示虚数部分
x = 1      # int
y = 2.8    # float
y2 = 35e3
y3 = 12E4
y4 = -87.7e100
z = 1j     # complex
z2 = 3+5j
z3 = 5j
z4 = -5j

# 可以使用int()、float()、complex()转换数据类型
# 不可以把complex转换为其它数字类型
a = float(x)    # convert from int to float
b = int(y)      # convert from float to int
c = complex(x)  # convert from int to complex

# python 数字支持的运算有：+ - * / % **
print(2)
print(2.323)
print(-2.323)
print(3 + 4.5)  # + - * /
# 整数相除的商是小数，如果能整除，小数为x.0，如果能除尽，显示小数，最多显示16位小数，超过16位四舍五入
# 浮点数相除的商是小数，不区分浮点数和双精度浮点数
print("division int:", 7 / 3)    # 2.3333333333333335
print("division float:", 5.3 / 2.1)    # 2.5238095238095237
print(10 % 3)  # 1, 模
print(10.3 % 3.2)  # 可以对浮点数求模，0.7000000000000002，保留16位小数
print(2 ** 3)    # 8
print(3.1 ** 2.3)    # 13.493726266519127, float number can also use power

# number functions
print(abs(-5))  # 5
print(pow(3, 2))  # 9，3的2次方
print(max(4, 6))  # 6
print(min(4, 6))  # 4
print(round(3.4))  # 3，四舍五入
print(round(3.5))  # 4，四舍五入

print(floor(3.9))  # 3，向下取整
print(ceil(3.1))  # 4，向上取整
print(sqrt(36))  # 6.0，平方根

# python没有内置random()方法生成随机数，但是python有一个内置random模块可用来生成随机数
print('randrange', random.randrange(1, 10))  # [1,10)中任取一整数
