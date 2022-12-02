import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='liulei_0905',
    auth_plugin='mysql_native_password'
)

print(mydb)
