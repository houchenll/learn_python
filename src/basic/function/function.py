

# 函数定义方法一：def
# 没有return或只调用return没有表达式时，函数调用返回None
def hello(name, age):
    """
    函数内部开始位置，可用3个双引号存放函数说明
    :return:
    """
    print('name is %s, age is %d' % (name, age))


# 函数定义方法二：lambda定义匿名函数
# 不建议使用这种方法定义函数，建议使用def
# lambda和：中间是参数列表，:后是一个表达式
# lambda不能访问参数列表之外的全局空间的参数
add = lambda arg1, arg2: arg1 + arg2


# 参数传递：python中所有类型都是对象，其中包含可变对象和不可变对象，可变对象包括列表、字典等，不可变对象包含字符串、
#         数字、元组等。参数传递时，可变对象是传递的对象本身的引用，函数内部修改了对象后，函数外部的原对象也被修改，
#         不可变对象传递的是值，是原对象的复制，函数内部修改对象，不影响函数外原对象
def change_int(num, arr):
    num *= 10
    arr.append([4, 5, 6])


# 参数包括：必备参数、关键字参数、默认参数、不定长参数
# 必备参数须以正确的顺序传入函数，调用时的数量必须和声明时的一样，如name, age
# 关键字参数定义时和必备参数一样，区别在于调用时指定参数名，这样调用时传递参数的顺序不用和定义时的顺序相同。
#        注意！调用时关键字参数必须放在最后，其后不能再有positioned参数
# 默认参数定义时指定默认值，等号两边不能有空格，调用时不传默认参数就使用默认值，传递参数时可以按必备参数的方式按顺序传递，
#        也可以按关键字参数的方式指定值传递
# 不定长参数使用*定义，传入的参数存放在元组中
def test_param(name, age, gender='male', *other):
    print(name, age, gender, other)   # david 22 female ('a',)


# 3.8 引入强制位置参数，/前的必须是位置参数，/和*中间的可以是位置参数或关键字参数，*后的必须是关键字参数
# def f(a_, b, /, c, d, *, e, f_):
#     print(a_, b, c, d, e, f_)


# print(hello('jack', 22))  # None
a = 3
nums = [1, 2, 3]
# print(a, nums)  # 3 [1, 2, 3]
change_int(a, nums)
# print(a, nums)  # 3 [1, 2, 3, [4, 5, 6]]

# test_param('jack', 23)  # jack 23 male ()
# test_param(age=18, name='lucy')  # lucy 18 male ()
# test_param('david', 22, 'female', 'a')  # david 22 female ('a',)

# print(add(1, 2))  # 3
# f(1, 2, 3, d=4, e=5, f_=6)
