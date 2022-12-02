# python数据类型：整型、浮点型、布尔类型、
# 转换
# 获取类型

# 整型
# 长度不受限制

# 浮点型
# 大小不受限制
# e记法
num = 2.5e7
print(num)

# 布尔类型 True / False
# True相当于整数1，False相当于整数0
num = True + True
print(num)    # 2
print(True == 1)    # True

# int()，将字符串或浮点数转换为整数
a = '520'
b = int(a)
print(b)
a = 5.99
b = int(a)    # 砍掉小数部分
print(b)

# float()，将字符串或整数转换为小数
a = 520
b = float(a)
print(b)    # 520.0
a = '520'
b = float(a)
print(b)    # 520.0

# str()，将整数或浮点数转换为字符串

# type()，获取变量的类型
print(type(520))    # <class 'int'>
print(type(5.2))    # <class 'float'>
print(type(5e15))   # <class 'float'>
print(type(True))   # <class 'bool'>
print(type('ni hao'))    # <class 'str'>

# isinstance()，确定变量的类型。
# 接受两个参数，第1个参数是数据，第2个参数是类型
# 返回值是True或False，表示第1个参数是否是第2个参数的类型
print(isinstance('ni hao', str))    # True
print(isinstance('ni hao', int))    # False
