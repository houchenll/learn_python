# 条件判断 if else elif 三元操作符
# 断言 assert

age = 13
if age >= 18:
    print('adult')
else:
    print('children')

score = int(input("请输入一个分数："))
if 100 >= score >= 90:
    print('A')
elif 90 > score >= 80:
    print('B')
elif 80 > score >= 60:
    print('C')
elif 60 > score >= 0:
    print('D')
else:
    print('输入错误')

# python的三元操作符，不同于类C语言
x, y = 4, 5
small = x if x < y else y
print(small)

# 断言 assert
# 当这个关键字后边的条件为假的时候，程序自动崩溃并抛出AssertionError的异常
# 一般来说我们可以用它在程序中置入检查点，当需要确保程序中的某个条件一定为真才能让程序正常工作的话，assert关键字就起作用了
assert 3 > 4
