# 循环：while for range() break continue

# while
guess = 0

# while guess != 8:
#     temp = input('请输入一个数字：')
#     guess = input(temp)
#     print(guess)

print('end')

# for
favourite = 'FishC'
for i in favourite:
    print(i, end=' ')

members = ['小甲鱼', '小不丁', '黑夜', '迷途', '怡静']
for each in members:
    print(each, len(each))

# range([start=0,] stop[, step=1])
# 有3个参数，其中[]中的两个参数是可选的，start默认值为0，step默认值为1
# 作用是生成一个从start开始到stop参数值结束的数字序列，不包括stop
print(range(0, 5))  # range(0, 5)
print(list(range(5)))  # [0, 1, 2, 3, 4]
for i in range(5):
    print(i)
