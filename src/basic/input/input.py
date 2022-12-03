# -*- coding:utf-8 -*-

# python3 中取到的值是字符串类型，包括数字
x = input("x: ")  # 3
y = input("y: ")  # 2
z = x + y
print(z)  # 32(python3) / 5(python2)
x = int(x)
y = int(y)
z = x + y
print(z)

# python2中输入字符串用raw_input
# name = raw_input("请输入姓名")
# print('name is %s' % name)

# python2中input是把输入的内容当做代码执行
# python3中input是把输入内容当做字符串，与python2中raw_input相同
