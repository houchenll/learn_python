# 遍历
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# python 可在循环外使用循环变量，循环外用到的循环变量是最后一次循环的值
print(magician.title() + ", that was a great trick!")    # Carolina, that was a great trick!
