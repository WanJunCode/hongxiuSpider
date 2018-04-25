import sqlite3

con=sqlite3.connect('test2.db')
# con=sqlite3.connect(':memory:')

cur=con.cursor()

cur.execute('create table person(id integer PRIMARY KEY ,name varchar(20),age integer)')

cur.execute('INSERT INTO person VALUES (?,?,?)',(0,'qiye',20))

cur.executemany('INSERT INTO person VALUES (?,?,?)',[(3,'marry',20),(4,'jack',20)])

# 回滚操作
# con.rollback()
con.commit()