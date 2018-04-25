#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","root","1942548635wj","book",charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

cursor.execute('SELECT * FROM book2')

values=cursor.fetchall()

print(values)

cursor.close()
# 关闭数据库连接
db.close()