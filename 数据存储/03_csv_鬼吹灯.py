import requests
from lxml import etree
import csv
import re

headers = {
    "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
}

url = 'http://www.seputu.com/'
html = requests.get(url,headers=headers)
html = etree.HTML(html.text)
all_books = html.xpath('//div[@class="mulu"]')

rows = []
for book in all_books:
    #获取大标题
    big_title = book.xpath('.//div[@class="mulu-title"]/center/h2/text()')
    #因为得到的大标题上边有空的，所以判断一下
    if len(big_title) >0:
        #因为得到的是list集合，如果想要的到纯文本，加个【0】
        bigtitle = big_title[0]
        #得到章节url和名称
        url_zhangjie = book.xpath('//div[@class="box"]/ul/li/a')
        for url_and_zhangjie in url_zhangjie:
            #查找章节地址
            url = url_and_zhangjie.xpath('./@href')[0]
            #查找章节名称
            zhangjie = url_and_zhangjie.xpath('./@title')[0]

            #通过正则将章节名称中的时间提取出来
            pattern = re.compile(r'\s*\[(.*)\]\s+(.*)')
            match = pattern.search(zhangjie)
            if match != None:
                date = match.group(1)
                little_title = match.group(2)
                content =(bigtitle,little_title,url,date)
                rows.append(content)

headers = (['Title','little_title','url','date'])

#newline='' 是防止取到的数据中间由换行
with open('03_guichuideng.csv','w',newline='') as f :
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)