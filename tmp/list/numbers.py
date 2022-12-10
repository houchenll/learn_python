# range(start, end) 函数生成数字列表，该列表不是list；
numbers = range(1, 5)
print(numbers)    # range(1, 5)

# 列表从start开始，到end前结束，不包含end；
for number in numbers:
    print(number)    # 1/2/3/4

# 若想生成list数字列表，需对range()返回结果作list()处理
numbers = list(numbers)
print(numbers)    # [1, 2, 3, 4]

# range(start, end, step) 函数还可以指定步长，从start开始，每次增加step，直到达到end结束，不包含end
even_numbers = list(range(2, 11, 2))
print(even_numbers)    # [2, 4, 6, 8, 10]

# 例1：添加1到10各个整数的平方到列表中，并打印列表
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)    # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 例2：使用列表解析生成1到10整数的平方和列表
# 1. 定义列表变量名，并用[]为它指定一个空列表
# 2. 在[]中添加表达式 value ** 2
# 3. 在表达式后用for循环为value赋值，中间用空格分开
squares = [value ** 2 for value in range(1, 11)]
print(squares)    # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# python提供内置函数，用于获取数字列表最小值、最大值、总和
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("min", min(digits))    # min 0
print("max", max(digits))    # max 9
print("sum", sum(digits))    # sum 45
