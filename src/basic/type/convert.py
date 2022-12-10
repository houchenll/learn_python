# 类型转换

# float()，将字符串或整数转换为小数
# str => float
print(float('3.2'))  # 3.2
print(float('3'))  # 3.0
# print(float('a'))  # ValueError: could not convert string to float: 'a'

# int => float
print(6)  # 6

# int(), 将字符串或浮点数转换为整数
# str => int
print(int('3'))  # 3
# print(int('3.2'))  # ValueError: invalid literal for int() with base 10: '3.2'
# print(int('a'))  # ValueError: invalid literal for int() with base 10: 'a'

# float => int
# 砍掉小数部分
print(int(5.2))  # 5
print(int(-5.2))  # -5

# str()，将整数或浮点数转换为字符串
print(str(100))  # 100
print(str(100.2))  # 100.2
