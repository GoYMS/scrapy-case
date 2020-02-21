"""
新知识：如果在URL中看到# 说明这个不是真地址，需要在f12中查看
网易云歌手信息爬取，重要的是请仔细看源码
URL= 'https://music.163.com/discover/artist/cat?id=4001&initial=0'
"""
import requests
import csv
from lxml import etree
from bs4 import  BeautifulSoup
def Get_songer(url):
    headers ={
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36",
        "Referer":"https://music.163.com/",

    }

    html = requests.get(url,headers=headers)
    #随手标记，html.text是得到的网页html
    soup = BeautifulSoup(html.text,'lxml')
    for item in soup.find_all('a',attrs={'class':'nm nm-icn f-thide s-fc0'}):
        name = item.string
        #下边是将得到的 /artist?id=   替换成空的   也就是说只得到数字
        id = item['href'].replace('/artist?id=','').strip()
        print(id,name)
        try:
            csvfile.writerow((id,name))
        except Exception as e:
            print("存储失败")
            print(e)


    #下边是用xpath
    # html = etree.HTML(html.text)
    #
    # for i in  html.xpath('//a[@class="nm nm-icn f-thide s-fc0"]/text()'):
    #     name = i
    #
    # for j in  html.xpath('//a[@class="nm nm-icn f-thide s-fc0"]/@href'):
    #    id = j
    # print(i,j)


if __name__ == '__main__':
    id_list = [1001,1002,1003,2001,2002,2003,6001,6002,6003,7001,7002,7003,4001,4002,4003]
    init_list = [-1,0,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90]
    #文件存储位置
    f =  open ('01_songer.csv','w')
    csvfile = csv.writer(f)
    #这一点要注意！使用的是writerow，也就是说只能写入一行，所以外边还有再有一个括号
    csvfile.writerow(('id','name'))
    for i in id_list:
        for j in init_list:
            url = 'https://music.163.com/discover/artist/cat?id={0}&initial={1}'.format(i,j)
            Get_songer(url)
