# python支持的数据类型有：整型 int、布尔类型 bool、字符串 str、浮点型 float
# 没有 long，再大的整数都是 int
# list, tuple, dict

# python 中所有类型都是对象，分为可变对象和不可变对象
# 可变对象：list, dict
# 不可变对象：int, float, bool, string, tuple

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

# type()，获取变量的类型
print(type(520))    # <class 'int'>
print(type(5201234567222882828282882828228289283742983479287423892423922222222222289))    # <class 'int'>
print(type(5.2))    # <class 'float'>
print(type(5e15))   # <class 'float'>
print(type(True))   # <class 'bool'>
print(type('ni hao'))    # <class 'str'>
print('type (1, 2)', type((1, 2)))  # <class 'tuple'>
print('type {a: 2}', type({'a': 2}))  # <class 'dict'>

# compare type
print('compare type int false', type(1) == 'int')  # False
print('compare type int true', isinstance(1, int))  # True

# isinstance()，确定变量的类型。
# 接受两个参数，第1个参数是数据，第2个参数是类型
# 返回值是True或False，表示第1个参数是否是第2个参数的类型
print(isinstance('ni hao', str))    # True
print(isinstance('ni hao', int))    # False
