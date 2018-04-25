import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","root","1942548635wj","book",charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

cursor.execute('INSERT INTO book2(book_id ,book_href ,book_title ,book_image_src ,book_author ,book_class ,book_isfinish ,book_numofword ,book_intro) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',
               ('3937036603950001','https://www.hongxiu.com/book/3937036603950001','回眸医笑，冷王的神秘嫡妃','http://qidian.qpic.cn/qdbimg/349573/c_3937036603950001/90','青酒沐歌', '古代言情',1,256.95,"有种穿越叫技术穿，沐清歌到死都没想到这事会落到她身上。\r\n她本是21世纪的顶级医师，一朝丧命带着医生系统穿越成了丞相府懦弱的草包嫡女，亲爹不疼，庶母不爱，还被太子退了婚！\r\n"))
db.commit()

cursor.close()
db.close()