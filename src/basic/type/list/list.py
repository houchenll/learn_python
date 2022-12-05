# 列表创建，及增、删、改、查

# create list: use []
bicycles = []
print('type', type(bicycles))  # <class 'list'>
# print(bicycles)    # []
# list can contains all kind of data, such as string, int, float, bool, list, tuple, dict ...
# different kinds of data can be put into one list
bicycles = ['trek', 3, 5.6, True, ['one', 'two'], ('three', 4), {'name': 'john', 'age': 28}]
# print(bicycles)    # ['trek', 3, 5.6, True, ['one', 'two'], ('three', 4), {'name': 'john', 'age': 28}]

# get item from list by index, index can be > 0 from left to right, and < 0 from right to left
# list can also return a small list by specify index range
bicycles = ['trek', 'cannondale', 'redline']
# print(bicycles[0])    # trek, first item
# print(bicycles[-1])    # redline, -1 means last item
# 返回列表的部分元素称为切片，切片在右边界index的前一个元素停下，不包含右边界index
# print(bicycles[1:3])    # ['cannondale', 'redline'], 如果右index越界，会返回到最后一个item，但不会报错
# print(bicycles[:2])    # ['trek', 'cannondale'], 如果不指定左边界，那么左边界默认使用第1个元素
# print(bicycles[1:])    # ['cannondale', 'redline']，如果不指定右边界，那么右边界默认到最后一个元素
# print(bicycles[-2:])    # ['cannondale', 'redline']，返回列表最后两个元素
copy = bicycles[:]    # 切片中:不指定左右边界，可用来复制列表
# print(copy)    # ['trek', 'cannondale', 'redline']

# 复制方法2 copy
bikes = bicycles.copy()
print('bikes', bikes)  # ['trek', 'cannondale', 'redline']

# append (tail) 追加单个元素
bicycles.append('ducati')
# print(bicycles)    # ['trek', 'cannondale', 'redline', 'ducati'], 在原列表末尾添加一个元素

# insert (position), 原position位置及其右位置的元素会自动右移
bicycles.insert(1, 'phoenix')
# print(bicycles)    # ['trek', 'phoenix', 'cannondale', 'redline', 'ducati']

# combine, 有两种方法合并list，使用+合并列表，原列表值不变，需要把结果保存到一个变量中；使用extend()合并列表，在原列表基础上合并
names = ['one', 'two', 'three']
result = bicycles + names
# print(result)    # ['trek', 'phoenix', 'cannondale', 'redline', 'ducati', 'one', 'two', 'three']
bicycles.extend(names)
# print(bicycles)    # ['trek', 'phoenix', 'cannondale', 'redline', 'ducati', 'one', 'two', 'three']

# del (position)，使用del 删除指定position的元素，其右元素左移，但不能返回删除的元素
del bicycles[2]
# print(bicycles)    # ['trek', 'phoenix', 'redline', 'ducati', 'one', 'two', 'three']

# pop (tail or position), pop()可以删除指定位置的元素并返回被删除的元素，如果不指定位置，默认删除列表最后一个元素
bike = bicycles.pop()
# print(bicycles)    # ['trek', 'phoenix', 'redline', 'ducati', 'one', 'two']
# print(bike)    # three
bike = bicycles.pop(0)
# print(bicycles)    # ['phoenix', 'redline', 'ducati', 'one', 'two']

# remove (value), remove first match value, can't return removed item
bike = bicycles.remove('redline')
print('remove', bicycles)    # ['phoenix', 'ducati', 'one', 'two']
# print(bike)    # None

# 判断列表中是否存在某个元素
# print('index contain', bicycles.index('dragon'))  # ValueError: 'dragon' is not in list

# 获取列表中重复元素的数据，可用来判断数据是否在列表中存在
print('count', bicycles.count('one'))  # 1
print('count', bicycles.count('dragon'))  # 0

# clear, 清空列表
bicycles.clear()
print('clear', bicycles)  # []

cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(cars)    # ['bmw', 'audi', 'toyota', 'subaru']

# sort list one time for use
# 使用sorted(list)排序，不在原列表基础上修改，返回排序后的列表值
# print(sorted(cars))    # ['audi', 'bmw', 'subaru', 'toyota']
# print(sorted(cars, reverse=True))    # ['toyota', 'subaru', 'bmw', 'audi']
# print(cars)    # ['bmw', 'audi', 'toyota', 'subaru']

# sort(), 默认按单词字母在字母表中顺序排序，另外可以添加参数reverse=True，即可倒序排序
# 另外，sort()排序是在原列表内容上直接修改
cars.sort()
# print(cars)    # ['audi', 'bmw', 'subaru', 'toyota']
cars.sort(reverse=True)    # ['toyota', 'subaru', 'bmw', 'audi']
# print(cars)    # ['toyota', 'subaru', 'bmw', 'audi']

# reverse(), 对原列表倒序操作，在原列表上直接修改
# print(cars)    # ['toyota', 'subaru', 'bmw', 'audi']
cars.reverse()
# print(cars)    # ['audi', 'bmw', 'subaru', 'toyota']

length = len(cars)
# print(length)    # 4

