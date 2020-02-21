# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class MeijuScrapy02Pipeline(object):
    def process_item(self, item, spider):
        return item


class MeijuSpiderPipeline(object):
    def __init__(self):
        self.file = open('02_meiju.json','w',encoding='utf-8')
    def process_item(self,item,spider):
        #数据存储
        json.dump(dict(item),open("02_meiju.json",'a'),ensure_ascii=False)
        return item
    def close_spider(self):
        self.file.close()