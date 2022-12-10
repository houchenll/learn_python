# python中没有声明变量的命令。
# 变量在第一次为它赋值的时候创建。
x = 5
y = "John"
print(x)
print(y)

# 变量可以在赋值后修改
x = 4
x = "Sally"
print(x)

# Python允许您在一行中将值分配给多个变量
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# 可以在一行中将同一个值赋值给多个变量
x = y = z = "Orange"
print(x)
print(y)
print(z)

# 定义在方法外的变量叫做全局变量，全局变量可在方法内、外使用
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

# 定义在方法中的变量叫做局部变量，只能在方法内部使用。
# 局部变量和全局变量同名时，方法内使用和改变局部变量，不影响全局变量
def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

# 使用`global`关键字，可以在方法中创建全局变量
def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)

# 另外，使用global关键字，可以在方法中修改全局变量，否则就是定义局部变量
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)
