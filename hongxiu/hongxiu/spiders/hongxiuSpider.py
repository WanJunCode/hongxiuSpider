# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from hongxiu.items import HongxiuItem

class HongxiuspiderSpider(scrapy.Spider):
    name = 'hongxiuSpider'
    allowed_domains = ['www.hongxiu.com']
    start_urls = ['https://www.hongxiu.com/finish']
    url_head='https://www.hongxiu.com/finish?pageSize=10&gender=2&catId=-1&isFinish=1&isVip=-1&size=-1&updT=-1&orderBy=0&pageNum='
    pageNum=20

    def parse(self, response):
        bs=BeautifulSoup(response.body,'lxml')
        book_images = bs.find_all('div', {'class': 'book-img'})
        book_infos=bs.find_all('div',{'class':'book-info'})
        try:
            for book_img, book_info in zip(book_images, book_infos):
                book_id=book_img.a['href'].split('/')[2]
                book_href = 'https://www.hongxiu.com' + book_img.a['href']
                book_title = book_img.a['title']
                book_image_src = 'http:' + book_img.a.img['src']
                book_author = book_info.h4.text
                book_class = book_info.p.find('span', {'class': 'org'}).text
                book_isFinish = book_info.p.find('span', {'class': 'pink'}).text
                book_NumOfWords = book_info.p.find('span', {'class': 'blue'}).text
                book_intro = book_info.find('p', {'class': 'intro'}).text.strip()
                item = HongxiuItem(book_name=book_title, book_href=book_href, book_author=book_author,
                                   book_intro=book_intro, book_class=book_class,
                                   book_numofword=book_NumOfWords, book_isfinish=book_isFinish,
                                   book_image_src=book_image_src,book_id=book_id)
                yield item
        except:
            print('error')

        self.pageNum = self.pageNum+1
        uuu=self.url_head+str(self.pageNum)
        if(self.pageNum<100):
            yield scrapy.Request(url=self.url_head+str(self.pageNum),callback=self.parse)

