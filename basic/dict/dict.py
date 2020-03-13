
# dict表示字典，使用{}表示，存储key:value对
# key: 不可变量可以用为key，包括字符串，整数，小数，元组。可变量不可作为key，包括列表，字典
# python使用key的hash作为存储地址，因为可变量的hash值会变化，导致找不到原存储值，所以要求Key是不可变量
# value: 任何python数据


a = {
    'name': 'houchenl',
    22: 'age',
    1.68: 'weight',
    (1, 2, 3): 2
}
print(a)    # {'name': 'houchenl', 22: 'age', 1.68: 'weight', (1, 2, 3): 2}

# 使用len()函数可以计算所有集合的大小，包括dict
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}

# 使用key从dict中查找对应的value，value = d[key]
# 如果key不存在，会直接报错
print('Adam:', d['Adam'])

# 为避免key不存在时报的KeyError，有两种办法
# 1. 使用in判断key是否存在
if 'Paul' in d:
    print(d['Paul'])
if 'Paul' in d.keys():
    print(d['Paul'])
# 2. 使用dict本身提供的一个get方法，在key不存在的时候，返回None
print(d.get('Paul'))
# print(d['Paul'])    # 因为字典中没有这个key，所以报错

# dict的第一个特点是查找速度快，无论dict有一个元素还是10万个元素，查找速度是一样的。而list查找速度随元素的增加而下降。不过dict查找速度快的代价是占用内存大。
# 因为dict是根据Key查找的，所以Key不能重复
# dict的第二个特点是存储的key-value对没有顺序
# dict的第三个特点是作为key的元素必须是不可变的。python的基本类型字符串、整数、浮点数都是不可变的，都可以作为key。但是list是可变的，不能作为key

# d.keys()，列出字典中所有key，放在一个列表中
print(d.keys())    # dict_keys(['Adam', 'Lisa', 'Bart'])

# d.values()，列出字典中所有value，放在一个列表中
print(d.values())  # dict_values([95, 85, 59])

# d.items()，得到一个列表，每一项是一个元组
print(d.items())   # dict_items([('Adam', 95), ('Lisa', 85), ('Bart', 59)])

# 遍历一
for key in d.keys():
    value = d.get(key)
    print('foreach 1: key is %s, value is %s' % (key, value))

# 遍历二
for item in d.items():
    key = item[0]     # 元组可以用下标取值
    value = item[1]
    print('foreach 2: key is %s, value is %s' % (key, value))

# 遍历三
for item in d.items():
    key, value = item    # 元组也可以用几个变量，中间加逗号赋值，相当于拆包
    print('foreach 3: key is %s, value is %s' % (key, value))

# 遍历四，推荐！ 循环时直接把元组拆包赋值到变量中
for key, value in d.items():
    print('foreach 4: key is %s, value is %s' % (key, value))

# 遍历五，对返回的无序键列表进行排序
for name in sorted(d.keys()):
    print(name)

# 添加键值对
alien = {'color': 'green'}
alien['x_position'] = 0
alien['y_position'] = 25

# 删除键值对: 使用del语句，指定字典名和要删除的键
del alien['color']
