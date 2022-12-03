# division /
# 整数相除的商是小数，如果能整除，小数为x.0，如果能除尽，显示小数，最多显示16位小数，超过16位四舍五入
# 浮点数相除的商是小数，不区分浮点数和双精度浮点数
a = 7
b = 3
quoInt = a / b
print("quoInt:", quoInt)    # quoInt: 2.3333333333333335
c = 5.3
d = 2.1
quoFloat = c / d
print("quoFloat:", quoFloat)    # quoFloat: 2.5238095238095237

# power **
power = 2 ** 3
print(power)    # 8
# float number can also use power
power = 3.1 ** 2.3
print(power)    # 13.493726266519127

# python中有三种数字型数据类型：int, float, complex
x = 1      # int
y = 2.8    # float
z = 1j     # complex

# int 是整数，无长度限制

# float可以使用科学记数法，使用e表示10次方
x = 35e3
y = 12E4
z = -87.7e100

# complex 表示虚数，j表示虚数部分
x = 3+5j
y = 5j
z = -5j

# 可以使用int()、float()、complex()转换数据类型
# 不可以把complex转换为其它数字类型
x = 1      # int
y = 2.8    # float
z = 1j     # complex
a = float(x)    # convert from int to float
b = int(y)      # convert from float to int
c = complex(x)  # convert from int to complex

# python没有内置random()方法生成随机数，但是python有一个内置random模块可用来生成随机数
import random
print(random.randrange(1,10))  # [1,10)

