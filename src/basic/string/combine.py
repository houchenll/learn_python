# combine string

# method 1. use + to combine string
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)    # ada lovelace
print("Hello, " + full_name.title() + "!")    # Hello, Ada Lovelace!

# error: can't add int to string directly, int should be convert to string first befoure add
# str = "hello" + 5
# print(str)    # TypeError: can only concatenate str (not "int") to str

# to add int with string, int should be convert to string first
str = "hello" + str(5)
print(str)    # hello5

# method 2. %x is used to combine string and other values, include string/int/char/...
age = 18
print('age is %d' % age)    # age is 18
print('name is %s' % "后尘")    # name is 后尘
weight = 55.3
print('weight is %f' % weight)    # weight is 55.300000, %f has 6 after 0 by default
print('weight is %.2f' % weight)    # weight is 55.30
message = 'name is %s, age is %d, weight is %.1f' % ("后尘", age, weight)
print(message)    # name is 后尘, age is 18, weight is 55.3
# 其它格式化符号
# %c    字符
# %s    字符串
# %i    有符号十进制整数
# %d    有符号十进制整数
# %u    无符号十进制整数
# %o    八进制整数
# %x    十六进制整数（小写字母）
# %X    十六进制整数（大写字母）
# %e    科学计数法，索引符号使用小写e
# %E    科学计数法，索引符号使用大写E
# %f    浮点实数
# %g    %f和%e的简写
# %G    %f和%E的简写

# method 3, use , can combine string and int, even can combine int and int to string
height = 183
print("jack's height is", height)    # jack's height is 183
print(11, 33)    # 11 33
