# python数组中数据可以是整数、浮点数、字符串、对象
# python数组中可以放不同类型数据

# 创建列表
members = ['小甲鱼', '小不丁', '黑夜']
numbers = [1, 2, 3, 4, 5]
mix = [1, '小甲鱼', 3.14, [1, 2, 3]]
empty = []

# 添加元素
members.append('福禄娃娃')  # 在尾部添加1个元素，只能添加1个元素
members.extend(['迷途', '怡静'])  # 在尾部添加1个数组，用一个列表扩展另一个列表
members.insert(0, '牡丹')  # 在指定位置添加1个元素
print(members)

# 查询
print(members[0])

# 删除
members.remove('怡静')  # 删除指定元素
del members[1]  # 删除指定位置的元素
members.pop(3)  # 取出指定位置的元素，并返回这个元素
members.pop()   # 取出最后一个元素并返回

# 分片
print(members[1:3])  # 返回1个复制出的子数组，从1开始，到3结束，不包含3
print(members[:3])   # 默认从0开始
print(members[1:])   # 从1到最后
print(members[:])    # 复制整个数组

# 比较数组大小
list1 = [123]
list2 = [234]
print(list1 > list2)  # False
list1 = [123, 456]
list2 = [234, 123]
print(list1 > list2)  # False，只比较第1个元素
# 数组拼接 == extend()，不推荐
list3 = list1 + list2
list3 *= 3

# 判断元素是否在数组中
print('小甲鱼' in list1)
print('小甲鱼' not in list1)

# 内置函数
list2.count(123)  # 返回元素在数组中存在的数量
list2.index(123)   # 返回元素在数组中的索引
list2.index(123, 1, 3)  # 后两个参数表示查找时索引的范围
list2.reverse()  # 数组原地翻转，没有返回值，改变原数组
list6 = [4, 3, 2, 5, 1, 9, 23, 32, 0]
list6.sort()
print(list6)  # [0, 1, 2, 3, 4, 5, 9, 23, 32]
list6.sort(reverse=True)
print(list6)  # [32, 23, 9, 5, 4, 3, 2, 1, 0]
