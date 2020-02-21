"""
酷狗音乐top500抓取

url = ‘https://www.kugou.com/yy/rank/home/1-8888.html?from=rank’

一页只有22个，查看更多内容需要下载客户端，但观察url发现，将1改为2后会跳转到第二页

"""

#//div[@class="pc_temp_songlist"]/ul/li/@title  歌名

import requests
from lxml import etree
import re

def Get_data(url):
    headers ={
       "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
    }
    html = requests.get(url,headers=headers)
    html = etree.HTML(html.text)
    #获得歌曲和作者
    title = html.xpath('//div[@class="pc_temp_songlist "]/ul/li/@title')
    songers = ','.join(title)

    #获得歌曲序号
    num = html.xpath('//div[@class="pc_temp_songlist "]/ul/li/span[@class="pc_temp_num"]/text()')
    number = ','.join(num)
    # pattern= re.compile(r'^[0-9]*$')
    # numbers = pattern.match(number)
    # print(numbers)
    print(number.strip())


if __name__ == '__main__':

    for i in range(1,24):
        url = 'https://www.kugou.com/yy/rank/home/{0}-8888.html?from=rank'.format(i)
        Get_data(url)