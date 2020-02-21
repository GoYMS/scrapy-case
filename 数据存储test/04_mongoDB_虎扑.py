import requests
from lxml import etree
from pymongo import MongoClient


class MongoAPI(object):
    def __init__(self,db_ip,db_port,db_name,table_name):
           self.db_ip = db_ip
           self.db_port = db_port
           self.db_name = db_name
           self.table_name = table_name
           self.con = MongoClient(host=self.db_ip,port=self.db_port)

           self.db = self.con[self.db_name]
           self.table = self.db[self.table_name]


    #获取一条数据
    def get_one(self,query):
        return self.table.find_one(query,property={"_id":False})
    #获取多条数据
    def get_all(self,query):
        return self.table.find(query)

    #添加数据
    def add(self,kv_dict):
        return self.table.insert(kv_dict)
    #删除数据
    def delete(self,query):
        return self.table.delete_many(query)
    #更新数据
    def updata(self,query,kv_dict):
        self.table.update_one(query,{'$set':kv_dict},upsert=True)
#获得页面初始信息
def spider(url):
    headers = {
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
    }
    #请求页面
    rsp = requests.get(url,headers=headers)
    html = etree.HTML(rsp.text)
    return html

def parse(html):
    #获得页面详情信息链接
    hrefs = html.xpath('//ul[@class="for-list"]//div[@class="titlelink box"]/a[@class="truetit"]/@href')
    global href
    href = ['https://bbs.hupu.com'+ href for href in hrefs]
    title(href)


    #获取作者
    authors = html.xpath('//div[@class="author box"]/a[@class="aulink"]/text()')

    #获取发布时间
    times = html.xpath('//div[@class="author box"]/a[2]/text()')

    #获取回复数和浏览数
    datas = html.xpath('//ul[@class="for-list"]/li/span[@class="ansour box"]/text()')
    datas = [x.split('\xa0/\xa0') for x in datas]

    #回复数
    replies = [x[0] for x in datas]


    #浏览数
    brows = [x[1] for x in datas]

    #最后回复时间
    last_times = html.xpath('//div[@class="endreply box"]/a/text()')


    #最后回复人
    last_names = html.xpath('//div[@class="endreply box"]/span[@class="endauthor "]/text()')


    # print(title(href))
    # print(href)
    # print(authors)
    # print(times)
    # print(replies)
    # print(brows)
    # print(last_times)
    # print(last_names)

    items = zip(title(href),href,authors,times,replies,brows,last_times,last_names)
    return items

def title(href):
    # 获得标题
    title = []
    for href_title in href:
        html = spider(href_title)
        t = html.xpath('//div[@class="bbs-hd-h1"]/h1/text()')
        title.append(t)
    return title

#存储数据
def  data_storage(items):
    hupu_post = MongoAPI("127.0.0.1",27017,"hupu","post")
    for item in items:
        hupu_post.add(
            {
                "title(href)":item[0],
                "href": item[1],
                "authors": item[2],
                "times": item[3],
                "replies": item[4],
                "brows": item[5],
                "last_times": item[6],
                "last_names": item[7],

            }
        )
def main():
    url = 'https://bbs.hupu.com/nba-2'
    html = spider(url)
    parse(html)
    data_storage(parse(html))
if __name__ == '__main__':
    main()