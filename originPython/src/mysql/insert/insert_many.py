import mysql.connector

testdb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='liulei_0905',
    database='test',
    auth_plugin='mysql_native_password'
)

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
