"""
mongoDB:非关系型数据库
mongoDB：更加适合爬虫的数据库
mongoDB：是一个给予分布式文件存储的数据库  由c++编写
主要为web应用提供可扩展的高性能数据存储解决方案


概念说明

mysql        mongoDB       说明

database     database       数据库
table        collection     表/集合
row          document       行/文档
colume       field         字段/域
index      index            索引
primary     primary         主键/_id为主键

"""
#安装mongoDB ：百度

#安装  pip install pymongo  模块

import pymongo

#链接mongodb数据库

client  = pymongo.MongoClient()


db = client.Table_Stu
post = {
    'name' :'yangmingshuai',
    'sex':'m',
    'age':'18'
}

posts = db.posts
post_id = posts.insert_one(post).inserted_id

