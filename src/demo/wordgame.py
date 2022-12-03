# 引入模块
import random

secret = random.randint(1, 10)

guess = -1

while guess != secret:
    temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
    guess = int(temp)

    if guess == secret:
        print("我草，你是小甲鱼心里的蛔虫吗？！")
        print("哼，猜中了也没有奖励")
    else:
        if guess > secret:
            print('哥，大了大了')
        else:
            print("嘿，小了，小了")

print("游戏结束，不玩啦")
