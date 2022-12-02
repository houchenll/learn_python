# 使用`type()`方法可以获取任何对象的数据类型
x = 5
print(type(x))    # <class 'int'>

# 变量的数据类型在向变量赋值时设置
x = "Hello World"    # <class 'str'>
x = 20               # <class 'int'>
x = 20.5             # <class 'float'>
x = 1j               # <class 'complex'>
x = ["apple", "banana", "cherry"]               # <class 'list'>
x = ("apple", "banana", "cherry")               # <class 'tuple'>
x = range(6)                                    # <class 'range'>
x = {"name": "John", "age": 36}                 # <class 'dict'>
x = {"apple", "banana", "cherry"}               # <class 'set'>
x = frozenset({"apple", "banana", "cherry"})    # <class 'frozenset'>
x = True                    # <class 'bool'>
x = b"Hello"                # <class 'bytes'>
x = bytearray(5)            # <class 'bytearray'>
x = memoryview(bytes(5))    # <class 'memoryview'>

# 使用构造函数可以设置数据的类型
x = str("Hello World")
x = int(20)
x = float(20.5)
x = complex(1j)
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = range(6)
x = dict(name="John", age=36)
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))
x = bool(5)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))

