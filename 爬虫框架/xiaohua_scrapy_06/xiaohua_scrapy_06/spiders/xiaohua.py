# -*- coding: utf-8 -*-
import scrapy
from xiaohua_scrapy_06.items import XiaohuaScrapy06Item




"""
使用selenium  自定义下载中间件
"""
class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    allowed_domains = ['xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/2014.html']

    def parse(self, response):
        infos = response.xpath('//div[@class="item masonry_brick masonry-brick"]')

        for info in infos:
            title = info.xpath('./div[@class="title"]/span/a/text()').extract()[0]
            hrefs = info.xpath('./div[@class="title"]/span/a/@href').extract()[0]
            try:
                href = 'http://www.xiaohuar.com'+hrefs
            except Exception as e:
                href = '未知'

            item = XiaohuaScrapy06Item()

            item['title'] = title
            item['href'] = href

            yield item
