# 打印双引号
print('Learn "Python" in imooc.')

# 打印单引号
print("I'm Chinese.")

# 既打印单引号，也打印双引号，使用转义
print('Bob said \"I\'m Ok\".')
print("Bob said \"I\'m Ok\".")
print('Bob said "I\'m Ok".')
print("Bob said \"I'm Ok\".")
#print(r'Bob said "I'm Ok".')   not ok

# r字符串不做转义
str1 = r'\(~_~)/\(~_~)/'
print(str1)

# 多行字符串
str1 = '''第一行
第二行
第三行'''
print(str1)

str1 = '第一行\n第二行\n第三行'
print(str1)

# 多行文本中的引号不用转义
str1 = '''Python is created by "Guido".
It is free and easy to learn.
Let's start learn Python in imooc!'''
print(str1)

# 中文
str1 = '云横秦岭家何在，雪拥蓝关马不前。'    # OK
str2 = u'云横秦岭家何在，雪拥蓝关马不前。'    # OK
print(str1)
print(str2)

# 通过索引获取字符串中字符
str1 = 'Hello everyone.'
print(str1[0])
print(str1[-1])    # 最后一个字符是-1，而不是-0

# 通过:截取字符串中的值
print(str1[0:4])
print(str1[:4])    # 等价于 [0:4]
print(str1[:-1])   # 前n-1个字符
print(str1[:])     # 所有字符
print(str1[-4:])   # -4到最后

# 分割字符串
print('ab,cde,fgh,ijk'.split(','))  # ['ab', 'cde', 'fgh', 'ijk']

# 拼接字符串
print('\t'.join(['ab', 'cde', 'fgh', 'ijk']))  # ab\tcde\tfgh\tijk

# 字符串连接 +
str1 = 'Hello'
str2 = 'World'
str3 = str1 + str2
str1 += str2
print(str3)

# 字符串连接 ,
#str3 = str1, str2    ('Hello', 'World')
print(str1, str2)     # 'Hello World'

# 重复字符串 *
str2 = str1 * 3
print(str2)

# 判断字符串是否包含某些字符串
str1 = 'Hello World'
str2 = 'llo'
flag = str2 in str1
flag2 = str2 not in str1
print(flag)
print(flag2)

# 去空格及特殊符号
s = ' \t\nhello, world!'
print(s.strip())    # hello, world!，去除字符串开头和结尾的空格，包括空格、\t，\n
print(s.lstrip(' hello, '))  # world! 去除字符串开头的指定字符串
print(s.rstrip('!'))    #  hello, world，去除字符串结尾的指定字符串

# 查找字符
sStr1 = 'strchr'
nPos = sStr1.index('r')  # r在sStr1中第一次出现的位置，如果不包含r，报异常
print(nPos)  # 2
nPos = sStr1.find('x')  # x在sStr1中第一次出现的位置，如果不包含x，返回-1，优先使用find
print(nPos)  # -1

# 大小写转换
sStr1 = 'JCstrlwr'
print(sStr1.upper())  # JCSTRLWR
print(sStr1.lower())  # jcstrlwr

# 翻转字符串
sStr1 = 'abcdefg'
sStr1 = sStr1[::-1]  # 翻转字符串
print(sStr1)  # gfedcba
