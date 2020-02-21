# -*- coding: utf-8 -*-
import scrapy
import time
import random
from lianjia_scrapy_04.items import LianJiaItem
class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']
    #start_urls = ['http://lianjia.com/']


    #自定义url地址
    def start_requests(self):
        start_urls = []
        for page in range(1,3):
            url = 'https://zz.lianjia.com/zufang/erqi/pg{}rp3/'.format(page)
            start_urls.append(url)
        for start_url in start_urls:
            #dont_filter : 过滤去重

            #scrapy.Request   相当于是用scrapy自带的request方法获取页面，
            #callback是将得到的页面返回给哪个函数


            #对于headers： settings中的user_agent适用于整个项目的所有请求，如果需要单独对某些请求设置User-Agent，
            # 就需要在DownloaderMiddleware或scrapy.Request中设置headers
            yield scrapy.Request(url=start_url,callback=self.parse,dont_filter=True)


    def parse(self, response):
        #获取所有的房源信息
        infos = response.xpath('//div[@class="content__list"]/div[@class="content__list--item"]')
        for info in infos:
            #获取房屋标题
            house_titles = info.xpath('.//p[@class="content__list--item--title twoline"]/a/text()').extract()
            #因为得到的有空格  所以将空格去除
            try:
                house_title = house_titles[0].strip().replace(' ','')
            except:
                house_title = '未知'

            #获取房屋详情链接
            house_hrefs = info.xpath('.//p[@class="content__list--item--title twoline"]/a/@href').extract()
            try:
               house_href = 'https://zz.lianjia.com' + house_hrefs[0]
            except:
                house_href = '未知'
            #获取房屋地址
            house_names = info.xpath('.//p[@class="content__list--item--des"]//a/text()').extract()
            try:
                house_name = '-'.join(house_names)
            except:
                house_name = '未知'
            time.sleep(random.choice([1,0.5]))
            #因为下边的函数也要用到上边的信息，所以需要使用meta将信息传送下去，例如下边的写法


            yield scrapy.Request(url=house_href,callback=self.detail_parse,dont_filter=True,meta={'house_href':house_href,'house_name':house_name,'house_title':house_title})

    #获取详情页里边的内容
    def detail_parse(self,response):
        infos = response.xpath('//div[@class="content clear w1150"]')
        for info in infos:
            #获取房源编号
            house_nums = info.xpath('.//i[@class="house_code"]/text()').extract()
            try:
                house_num = house_nums[0].split('： ')[-1]
            except:
                house_num = '未知'

            #获取房屋价格
            house_prices = info.xpath('.//p[@class="content__aside--title"]/span/text()').extract()
            try:
                house_price = house_prices[0]+'元/月'
            except:
                house_price = '未知'

            #租赁方式
            house_infos = info.xpath('.//p[@class="content__article__table"]//span/text()').extract()
            #出租方式
            try:
                house_style = house_infos[0]
            except:
                house_style = '未知'
            #厅室
            try:
                house_ting = house_infos[1]
            except:
                house_ting = '未知'
            #大小
            try:
                house_size = house_infos[2]

            except:
                house_size = '未知'
            #方向
            try:
                house_fangxiang = house_infos[3]
            except:
                house_fangxiang = '未知'

            item = LianJiaItem()

            item['house_title'] = response.meta['house_title']
            item['house_href'] = response.meta['house_href']
            item['house_name'] =  response.meta['house_name']
            item['house_num'] = house_num
            item['house_price'] = house_price
            item['house_style'] = house_style
            item['house_ting'] =  house_ting
            item['house_size'] = house_size
            item['house_fangxiang'] = house_fangxiang

            yield item

            # house_title
            # house_href
            # house_name
            # house_num
            # house_price
            # house_style
            # house_ting
            # house_size
            # house_fangxiang









