
# dict 表示字典，使用 {} 表示，存储 key:value 对
# key: 不可变量可以用为key，包括字符串、整数、小数、元组、bool值。可变量不可作为key，包括列表、字典
# python使用key的hash作为存储地址，因为可变量的hash值会变化，导致找不到原存储值，所以要求Key是不可变量
# value: 任何python数据

# dict的第一个特点是查找速度快，无论dict有一个元素还是10万个元素，查找速度是一样的。而list查找速度随元素的增加而下降。不过dict查找速度快的代价是占用内存大。
# 因为dict是根据Key查找的，所以Key不能重复
# dict的第二个特点是存储的key-value对没有顺序
# dict的第三个特点是作为key的元素必须是不可变的

# 声明、创建
a = {
    'name': 'll',
    22: 'age',
    1.68: 'weight',
    True: 'true element',
    (1, 2, 3): 2
}
print('a', a)    # {'name': 'll', 22: 'age', 1.68: 'weight', True: 'true element', (1, 2, 3): 2}

# 读取，获取信息，遍历
# 使用len()函数可以计算所有集合的大小，包括dict
print('len of a', len(a))  # 5

# 使用key从dict中查找对应的value，value = a[key]
# 如果key不存在，会直接报错
print('name of a', a['name'])  # ll
# print('unknown key', a[3])  # KeyError: 3, 因为字典中没有这个key，所以报错

# 为避免key不存在时报的KeyError，有两种办法
# 1. 使用in判断key是否存在
if 'name' in a:
    print('test in 1:', a['name'])  # ll
if (1, 2, 3) in a.keys():
    print('test in 2:', a[(1, 2, 3)])  # 2
# 2. 使用dict本身提供的一个get方法，在key不存在的时候，返回None
print('get 22', a.get(22))  # age
print('get 23', a.get(23))  # None

# dict.keys()，列出字典中所有key，放在一个列表中
print('get keys:', a.keys())    # dict_keys(['name', 22, 1.68, True, (1, 2, 3)])

# dict.values()，列出字典中所有value，放在一个列表中
print('get values:', a.values())  # dict_values(['ll', 'age', 'weight', 'true element', 2])

# dict.items()，得到一个列表，每一项是一个元组
# dict_items([('name', 'll'), (22, 'age'), (1.68, 'weight'), (True, 'true element'), ((1, 2, 3), 2)])
print('get items:', a.items())

# 遍历一
for key in a.keys():
    value = a.get(key)
    print('foreach 1: key is %s, value is %s' % (key, value))

# 遍历二
for item in a.items():
    key, value = item
    print('foreach 2: key is %s, value is %s' % (key, value))

# 遍历三，推荐！ 循环时直接把元组拆包赋值到变量中
for key, value in a.items():
    print('foreach 3: key is %s, value is %s' % (key, value))

# 遍历四，对返回的无序键列表进行排序
scores = {
    'lucy': 80,
    'jack': 90,
    'david': 85
}
# 不能对 a 执行这个操作，因为不同类型的常量之间不能比较大小，如 int 和 str
for key in sorted(scores.keys()):
    value = scores.get(key)
    print('foreach 4: %s : %d' % (key, value))

# 添加键值对
alien = {'color': 'green'}
alien['x_position'] = 0
alien['y_position'] = 25
print('alien', alien)  # {'color': 'green', 'x_position': 0, 'y_position': 25}

# 删除键值对: 使用del语句，指定字典名和要删除的键
del alien['color']
print('alien after delete:', alien)  # {'x_position': 0, 'y_position': 25}
