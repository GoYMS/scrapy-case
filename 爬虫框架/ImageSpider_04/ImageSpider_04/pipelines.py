# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

#使用自带的图片存储，先导包
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

class Imagespider04Pipeline(object):
    def process_item(self, item, spider):
        return item

class ImageSpiderPipeline(ImagesPipeline):
    #自带的方法
    def get_media_requests(self, item, info):
        for imge_url in item['imgurl']:
            yield Request(imge_url)
