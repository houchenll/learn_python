# -*- coding:utf-8 -*-

# print

print("hello world")    # hello world

# , can used to combine values to string in print(), values can be int/string
# , will be displayed as a blank
print("hello", "world")    # hello world
print("my age is", (29 + 1))    # my age is 30
print(1, 2, 3, 4)    # 1 2 3 4

# 22, 44 formed a tuple not a string outside of print
numbers = 22, 44
print(numbers)    # (22, 44)
numbers = 22,
print(numbers)    # (22,)

age = 18
name = 'zara'
print("%s's age is %d" % (name, age))  # zara's age is 18
print(name, age)  # zara 18 逗号分隔的变量之间会自动加上空格
