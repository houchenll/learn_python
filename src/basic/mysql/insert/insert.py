#-*- coding:utf-8 -*-
import mysql.connector

testdb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='liulei_0905',
    auth_plugin='mysql_native_password',
    database='test'
)

#print(testdb)

cursor = testdb.cursor()

# 注意：无论字段实际数据类型是什么，通配符一律使用%s
sql = "INSERT INTO person (name, age, weight) VALUES (%s, %s, %s)"
val = ("liulei", 29, 56.7)
cursor.execute(sql, val)

testdb.commit()

print(cursor.rowcount, "record inserted. id:", cursor.lastrowid)
