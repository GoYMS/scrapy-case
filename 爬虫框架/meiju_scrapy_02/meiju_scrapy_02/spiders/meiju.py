# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from meiju_scrapy_02.items import  MeijuSpiderItem


class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    start_urls = ['https://www.meijutt.com/new100.html']

    def parse(self, response):
        content = etree.HTML(response.body.decode('GBK'))
        movies = content.xpath('//ul[@class="top-list  fn-clear"]/li')
        for movie in movies:
            a_list = movie.xpath('./h5/a')
            a = a_list[0].text #电影名

            #电影状态
            stats = movie.xpath('.//span[@class="state1 new100state1"]/font')[0].text
            item = MeijuSpiderItem()
            item['name'] = a
            item['state'] = stats

            yield item

