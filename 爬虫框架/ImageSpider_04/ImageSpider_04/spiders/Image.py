# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from ImageSpider_04.items import Imagespider04Item


"""
使用scrapy自带的方法下载图片
"""

class ImageSpider(scrapy.Spider):
    name = 'Image'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/archives/55.html']

    def parse(self, response):
        infor = Imagespider04Item()
        imgurls = response.xpath('//div[@class="post-content"]/p/img/@src').extract()
        infor['imgurl'] = imgurls
        yield infor

