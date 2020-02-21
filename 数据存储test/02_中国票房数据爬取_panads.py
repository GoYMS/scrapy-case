"""
使用pandas， 结构化数据分析包
"""

import pandas
import requests
from bs4 import  BeautifulSoup
from lxml import etree




url = 'http://www.cbooo.cn/year?year=2019'
headers = {
   "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
}
html = requests.get(url,headers=headers)
html = etree.HTML(html.text)
#获取所有的信息
items= html.xpath('//div[@class="tabbox tabbox02"]')
for item in items:
    #获取电影名称
    file_name = item.xpath('//td[@class="one"]/a/@title')
    #获取电影主页链接
    file_url = item.xpath('//td[@class="one"]/a/@href')
    #获得电影类型
    #尤其xpath中出现tbody的你需要删除,不知道为什么，反正将tbody删除后正常
    file_type = item.xpath('//table[@class="date date01"]/tr/td[2]/text()')
    #获得总票房
    Box_office = item.xpath('//table[@class="date date01"]/tr/td[3]/text()')
    #获得票价
    file_price = item.xpath('//table[@class="date date01"]/tr/td[4]/text()')
    #获得场均人次
    file_people = item.xpath('//table[@class="date date01"]/tr/td[5]/text()')
    #获得国家及地区
    file_country = item.xpath('//table[@class="date date01"]/tr/td[6]/text()')
    #获得上映日期
    file_date = item.xpath('//table[@class="date date01"]/tr/td[7]/text()')
df = pandas.DataFrame(
    {
        'name':file_name,
        'href': file_url,
        'type':file_type,
        'office':Box_office,
        'mean_people':file_people,
        'mean_price':file_price,
        'country':file_country,
        'time':file_date
    }
)

cols=['name','href','type','office','mean_people','mean_price','country','time']
df=df.ix[:,cols]


df.to_csv('02_movies.csv')

