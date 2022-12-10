# for

# 1. 遍历列表
members = ['小甲鱼', '小不丁', '黑夜', '迷途', '怡静']
for each in members:
    print(each, len(each))

# 1.1. continue
scores = (75, 98, 59, 81, 66, 43, 69, 85)
total = 0
num = 0
for score in scores:
    if score < 60:
        continue
    total += score
    num += 1
print('avg score:', total / num)  # 79.0

# 2. 遍历 range
# range([start=0,] stop[, step=1])
# 有3个参数，其中[]中的两个参数是可选的，start默认值为0，step默认值为1
# 作用是生成一个从start开始到stop参数值结束的数字序列，不包括stop
print(range(0, 5))  # range(0, 5)
print(list(range(5)))  # [0, 1, 2, 3, 4]
for i in range(5):
    print(i)

# 2.1 range and get
friends = ['Jim', 'Karen', 'Kevin']
for index in range(len(friends)):
    print(index, friends[index])

# 3. 遍历字符串
favourite = 'FishC'
for letter in favourite:
    print(letter, end=' ')  # F i s h C
