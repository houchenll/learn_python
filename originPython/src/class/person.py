
class Person:
    """成员类帮助信息，使用3个双引号包裹"""

    feet = 0  # 类成员变量，在Person类的所有实例间共享，可以在内部类或外部类中通过Person.feet访问

    __money = 12  # 两个下划线开头，表示类的私有成员变量，只能在类内引用，不能在类外访问，也不能被子类访问
    # 类内访问时可以使用self或类名引用，注意！！两种引用修改后的变量互相独立

    _foo = 22  # 单下划线开头，表示protected类型的变量，只能被类及子类访问

    # __init__是类的构造函数
    # self代表类实例，self在定义类的方法时是必须有的
    # 实例属性在构造函数中，通过挂载到self上定义
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.feet = 4    # 4只脚
        # print('__secretNumber 1', Person.__money)  # 12
        # print('__secretNumber 2', self.__money)  # 12
        Person.__money = 1
        self.__money = 2
        # print('__secretNumber 1', Person.__money)  # 1
        # print('__secretNumber 2', self.__money)  # 2

    # 析构函数
    # 类没有实例后被垃圾回收机制回收
    # 当是子类创建实例最后被回收时，__name__返回的是子类类名
    def __del__(self):
        print(self.__class__.__name__, '销毁')

    # 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是self
    def test(self):
        print(self)  # <__main__.Person object at 0x7faa01ec2d60>
        print(self.__class__)  # <class '__main__.Person'>

    # self不是必须的，换成其它单词也可以。但为了方便理解和阅读，通常需要使用self
    def print(person):
        print(person)
        print(person.__class__)

    # 运算符重载，打印对象实例时调用
    def __str__(self):
        return 'Person(%s, %d)' % (self.name, self.age)

    # 运算符重载，对象相加时调用
    def __add__(self, other):
        return Person(self.name + other.name, self.age + other.age)

    def rich(self):
        print('I am rich !')

    # 类的内部方法，不能在外部调用，以两个下划线开头
    def __count_money(self):
        print(self.__money)


# python中实例化类类似于函数调用，不用new，python中没有new这个关键字
p1 = Person('Zara', 18)
p1.test()
print(p1.name, p1.age)  # 使用对象.属性访问实例的属性 Zara 18
print(Person.feet)      # 使用类名.属性访问类的属性 4
# print(Person.name)    # error，类不能访问实例属性

p2 = Person('david', 20)
print(p1 + p2)          # Person(Zaradavid, 38)

p1.gender = 'male'      # 添加实例成员变量
p1.gender = 'female'    # 修改实例成员变量值
del p1.gender           # 删除实例成员变量值
# print(p1.gender)        # AttributeError: 'Person' object has no attribute 'gender'

Person.eyeNumber = 2    # 添加类成员变量
Person.eyeNumber = 3    # 修改类成员变量
del Person.eyeNumber    # 删除类成员变量

# 使用内置访问访问实例和类的成员变量
print(hasattr(p1, 'gender'))  # False
print(getattr(p1, 'name', 'jack'))  # Zara
print(setattr(p1, 'age', 24))  # None
print(delattr(p1, 'name'))    # None
print(hasattr(Person, 'feet'))  # True

# python的内置类属性
print(Person.__dict__)  # 字典{}，包括内置属性、类属性、方法等
print(Person.__doc__)  # 成员类帮助信息，使用3个双引号包裹
print(Person.__module__)  # __main__ 类定义所在的模块
print(Person.__bases__)  # (<class 'object'>,) 类的所有父类构成元素（包含了一个由所有父类组成的元组）
print(Person.__name__)  # Person

p2 = p1
p3 = p2
print(id(p1), id(p2), id(p3))  # 140674088107984 140674088107984 140674088107984
del p1
print('end 1')
del p2
print('end 2')
del p3  # 执行到这里时，Person类的所有实例引用被删除，Person类的销毁方法被调用
print('end 3')
print('end module')


class Son(Person):

    def __init__(self, name, age):
        # 调用父类构造函数的两种方法
        Person.__init__(self, name, age)
        # super(Son, self).__init__(name, age)

    # 覆写父类方法
    def rich(self):
        print(self._foo)
        print('I am richer !!')

    def change_foo(self, foo):
        self._foo = foo

    def print_foo(self):
        print('_foo', self._foo)


s1 = Son('jack', 23)
s1.rich()
s1.print_foo()
s1.change_foo(1)

s2 = Son('lucy', 16)
s2.print_foo()

# 判断一个类是否另一个类的子类
print(issubclass(Son, Person))  # True
# 判断一个对象是否是一个类的实例
print(isinstance(s1, Son))      # True
print(isinstance(s1, Person))   # True
