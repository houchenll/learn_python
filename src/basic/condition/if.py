# 条件判断 if else elif 三元操作符
# 断言 assert

# 1. if
# if语句，不用小括号，条件末尾有冒号

# 使用 and 检查多个条件，等于java中的&&
age = 20
if age >= 18 and age <= 40:
    print('adult')
else:
    print('else')

# 简化写法，推荐
if 18 <= age <= 40:
    print('adult')
else:
    print('else')

# 使用 or 检查多个条件，等于java中的||
iq = 14
if iq <= 80 or iq >= 120:
    print('minority')
else:
    print('majority')

# 2. if else
age = 13
if age >= 18:
    print('adult')
else:
    print('children')

# 3. if - elif - else 结构
# 使用 not 表达 Java 中非的含义
is_male = False
is_tall = True
if is_male and is_tall:
    print('you are male and is tall')
elif is_male and not is_tall:
    print('you are male but not tall')
elif not is_male and is_tall:
    print('you are not male but is tall')
else:
    print('you are not male nether is tall')

# 4. 三元操作符
# python的三元操作符，不同于类C语言
x, y = 4, 5
small = x if x < y else y
print(small)

# 5. 检查特定值是否在列表中，使用 in
# 检查特定值不在列表中，使用 not in
cars = ['audi', 'bmw', 'subaru', 'toyota']
if 'audi' in cars:
    print('audi in list')
else:
    print('audi not in list')

# 6. if 表达式为 True 的有：非0数字, 非空字符串, 非空数组、元组、字典
# 为 False 的有：0, '', [], {}, (), None
# 引申：可用 if 判断数字是否为0，字符串是否为空，数组、元组、字典是否为空
value = []
if value:
    print('value equals True')
else:
    print('value equals False')
