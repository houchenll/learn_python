
# python操作mysql

## 连接

### Install MySQL Driver
python需要MySQL Driver来操作mysql数据库。这里使用的mysql driver是`mysql-connector`，下面使用pip命令来安装`mysql-connector`。pip一般跟随python环境一起安装  
```bash
sudo pip install --upgrade pip
sudo python -m pip install mysql-connector
```

### Test MySQL Connector
执行下面的程序，如果没有提示错误，表明`mysql-connector`已安装成功  
```python
import mysql.connector
```

### Create Connection
使用用户名和密码连接数据库，如下：  
```python
import mysql.connector

testdb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='xxxx',
    auth_plugin='mysql_native_password',
    database='test'
)

print(testdb)
```

## 读

## 插入

### 插入单行
使用cursor执行sql语句来插入数据。  
> 注意： 无论字段实际数据是什么类型，sql中通配符一律使用%s  
```python
cursor = testdb.cursor()

# 注意：无论字段实际数据类型是什么，通配符一律使用%s
sql = "INSERT INTO person (name, age, weight) VALUES (%s, %s, %s)"
val = ("liulei", 29, 56.7)
cursor.execute(sql, val)

testdb.commit()

print(cursor.rowcount, "record inserted.")
```

### 插入多行
使用executemany方法来一次性插入多行数据到表中，方法的第2个参数是一个tuple列表  
```python
cursor = testdb.cursor()

sql = "INSERT INTO person (name, address) VALUES (%s, %s)"
val = [
       ('Peter', 'Lowstreet 4'),
       ('Amy', 'Apple st 652'),
       ('Hannah', 'Mountain 21'),
       ('Michael', 'Valley 345'),
       ('Sandy', 'Ocean blvd 2'),
       ('Betty', 'Green Grass 1'),
       ('Richard', 'Sky st 331'),
       ('Susan', 'One way 98'),
       ('Vicky', 'Yellow Garden 2'),
       ('Ben', 'Park Lane 38'),
       ('William', 'Central st 954'),
       ('Chuck', 'Main Road 989'),
       ('Viola', 'Sideway 1633')
]

cursor.executemany(sql, val)

testdb.commit()

print(cursor.rowcount, "was inserted.")
```

### 获取最后一行id
使用cursor的lastrowid字段，可以获取插入的最后一行数据的id  
```python
print(cursor.rowcount, "record inserted. id:", cursor.lastrowid)
```

## 修改

## 删除
