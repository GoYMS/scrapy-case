# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import  pymysql
class QidianScrapy07Pipeline(object):
    def process_item(self, item, spider):
        return item

class MysqlPipeline(object):
    def __init__(self):
        # ip 用户 密码 数据库 字符集
        self.conn =pymysql.connect('127.0.0.1','root','123456','python',charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self,item,spider):

        sql = 'insert into qidian VALUES (null,%s,%s,%s)'
        data = (item['title'],item['href'],item['info'])
        try:
            self.cursor.execute(sql,data)
            #提交事物
            self.conn.commit()
        except:
            self.conn.rollback()
    def process_close(self,spider):
        self.cursor.close()
        self.conn.close()