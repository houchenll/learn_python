cars = ['audi', 'bmw', 'subaru', 'totota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# if语句，不用小括号，条件末尾有冒号

# 使用and检查多个条件，等于java中的&&
age = 20
if age >= 18 and age <= 40:
    print('adult')
else:
    print('else')

# 使用or检查多个条件，等于java中的||

# 检查特定值是否在列表中，使用in
if 'audi' in cars:
    print('in list')
else:
    print('not in list')

# 检查特定值不在列表中，使用 not in

# if - elif - else 结构
age = 12
if age < 4:
    print('child')
elif age < 18:
    print('young')
else:
    print('adult')

# 判断列表是否为空，使用if加列表名判断
requested_topping = []
if requested_topping:
    print('list is not null')
else:
    print('list is null')

