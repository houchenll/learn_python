# number

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