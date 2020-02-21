# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
from openpyxl import Workbook


class LianjiaScrapy04Pipeline(object):
    def process_item(self, item, spider):
        return item

class LianjiaJsonPipeline(object):
    def __init__(self):
        self.file = open('lianjia.json','w',encoding='utf-8')
    def process_item(self,item,spider):


        #ensure_ascii=False,这是因为json.dumps 序列化时对中文默认使用的ascii编码.
        # 想输出真正的中文需要指定ensure_ascii=False：

        str = json.dumps(dict(item),ensure_ascii=False)

        str = str +'\n'

        self.file.write(str)

        return item
    #关闭文件
    def closejson(self):
        self.file.close()

class LianjiaExclePipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['house_title','house_href','house_name','house_num','house_price','house_style','house_ting','house_size','house_fangxiang'])

    def process_item(self, item, spider):
        line = [item['house_title'],item['house_href'],item['house_name'],item['house_num'],item['house_price'],item['house_style'],item['house_ting'],item['house_size'],item['house_fangxiang'],]
        self.ws.append(line)
        self.wb.save('lianjia.xlsx')