# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class HongxiuItem(scrapy.Item):
    # define the fields for your item here like:
    book_id = scrapy.Field()
    book_name = scrapy.Field()
    book_href = scrapy.Field()
    book_author = scrapy.Field()
    book_intro = scrapy.Field()
    book_class = scrapy.Field()
    book_numofword = scrapy.Field()
    book_isfinish = scrapy.Field()
    book_image_src = scrapy.Field()
    pass
