# -*- coding: utf-8 -*-
import scrapy
from qidian_scrapy_07.items import QidianItem

class QidianSpider(scrapy.Spider):
    name = 'qidian'
    allowed_domains = ['qidian.com']
    start_urls = ['https://www.qidian.com/free']

    def parse(self, response):
        infos = response.xpath('//div[@class="book-img-text"]/ul/li')
        for info in infos :
            #标题
            title = info.xpath('.//div[@class="book-mid-info"]/h4/a/text()').extract()[0]
            #详情页链接
            hrefs = info.xpath('.//div[@class="book-mid-info"]/h4/a/@href').extract()[0]
            href = 'https:'+hrefs
            item = QidianItem()

            item['title'] = title
            item['href'] = href
            yield item

            #接着请求详情页面内容
            yield scrapy.Request(url=href,callback=self.parse_detail,meta={'data':item,'phantomjs':True},dont_filter=True)

    def parse_detail(self,response):
        item = response.meta['data']

        author = response.xpath('//div[@class="book-info "]//span/a/text()').extract()
        item['author'] = author

