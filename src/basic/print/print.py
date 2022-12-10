# -*- coding:utf-8 -*-
print("hello world")    # hello world

# combine 1: , recommend
# , can be used to combine values to string in print(), values can be int/string
# , will be displayed as a blank
print("hello", "world")    # hello world
print("my age is", (29 + 1))    # my age is 30
print(1, 2, 3, 4)    # 1 2 3 4

# combine 2: format %s, %d, recommend
age = 18
name = 'zara'
print("%s's age is %d" % (name, age))  # zara's age is 18
print(name, age)  # zara 18 逗号分隔的变量之间会自动加上空格

# combine 3: +
# only str can be combined by +
print(name + " is " + str(age) + " years old.")

# 22, 44 formed a tuple not a string outside of print
numbers = 22, 44
print(numbers)    # (22, 44)
numbers = 22,
print(numbers)    # (22,)

# str_format % (a,b,c)
# format 接受的参数有：%s, %d
# 1. str_format 中参数数量和元组中数量必须相等，否则报错：TypeError: not enough arguments for format string
# 2. %s 可接收任何数据类型
# 3. %d 接收 3.14 时，小数会被丢掉
# 4. %d 接收 bool 时，True 会转换成 1 后被打印，False 会转换成 0 被打印
# 5. %d 接收 str, list, dict 时，会报错 TypeError: %d format: a real number is required, not str|list|dict
# 6. %d 接收 tuple 时，不会报错，但不会输出打印结果
params = ('str', 100, 3.14, False, ['spring', 'summer'], ('good', 'bad'), {'name': 'lucy', 'age': 23})
print('format 1 %s, 2 %s, 3 %s, 4 %s, 5 %s, 6 %s, 7 %s' % params)

# 使用 end 指定最后一个字符，默认为换行
favourite = 'FishC'
for i in favourite:
    print(i, end=' ')
