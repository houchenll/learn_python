注释可以用来解释代码；  
注释可以用来在测试时防止代码执行；  

## 单行注释
使用 `#` 添加单行注释  

```Python
#This is a comment
print("Hello, World!") #This is a comment
```

## 多行注释
python中没有专门的多行注释语法  
可以通过在每行开头添加`#`添加多行注释  
也可以通过多行字符串添加多行注释，因为python会忽略带没有赋值的多行字符串  

```
#This is a comment
#written in
#more than just one line
print("Hello, World!")

"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")
```
