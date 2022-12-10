
# 1. normal
index = 0
while index < 5:
    print('index:', index)
    index += 1


# 2. break
index = 0
while True:
    print('index:', index)
    if index == 5:
        print(index, 'break')
        break
    index += 1
