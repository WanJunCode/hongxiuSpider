# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from scrapy.exceptions import DropItem

class HongxiuPipeline(object):
    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "1942548635wj", "book", charset='utf8')
        self.cursor = self.db.cursor()
        self.num=0


    def process_item(self, item, spider):
        if item['book_id']:
            self.cursor.execute('INSERT INTO book2(book_id ,book_title,book_href,book_image_src,book_author,book_class,book_intro ) VALUES(%s,%s,%s,%s,%s,%s,%s)',
                                (item['book_id'],item['book_name'],item['book_href'],item['book_image_src'],item['book_author'],item['book_class'],item['book_intro']))
            self.num=self.num+1
            if(self.num%10==0):
                self.db.commit()
            return item
        else:
            raise DropItem('missing book_id')

    def close_spider(self,spider):
        self.cursor.close()
        self.db.close()



