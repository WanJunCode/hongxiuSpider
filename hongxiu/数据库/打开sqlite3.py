import sqlite3
conn = sqlite3.connect('test2.db')
cursor = conn.cursor()
# 执行查询语句:
cursor.execute('select * from person')

# cursor.fetchone()
# cursor.fetchmany()

values = cursor.fetchall()

for i in values:
    print(i)

cursor.close()
conn.close()