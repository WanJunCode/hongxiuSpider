import pymysql
db = pymysql.connect("localhost","root","1942548635wj","book" )

# 使用cursor()方法获取操作游标
cursor = db.cursor()
cursor.execute('book_id char(20) not null primary key, book_href char(40) not null, book_title char(20) not null,'
               ' book_image_src char(40),book_author char(20), book_class char(20), book_isfinish tinyint,'
               ' book_numofword int,book_intro text)')

cursor.close()
# 关闭数据库连接
db.close()