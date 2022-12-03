
# 类的首字母大写
class Dog():
    # 使用 """ x """ 添加多行注释
    """一次模拟小狗的简单尝试"""

    # 类的函数叫做方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗打滚"""
        print(self.name.title() + " rooled over!")

# 创建实例
my_dog = Dog("willie", 6)
print("my dog's name is " + my_dog.name.title() + ".")
print("my dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()
