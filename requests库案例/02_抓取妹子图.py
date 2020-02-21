"""
首先声明，这个案例是按照教学视频来做的，与本人无关！！！
"""
import requests
from lxml import etree

def Meizi(base_url,headers):
    rsp = requests.get(base_url,headers)
    html = etree.HTML(rsp.text)
    #获取详情页信息
    img_src = html.xpath('//div[@class="postlist"]/ul/li/a/@href')
    for url in img_src:
        print(url)
if __name__ == '__main__':
    headers = {

        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36",
        "referer":"https://www.mzitu.com/tag/youhuo/",
        ":authority": "www.mzitu.com",
        ":method": "GET",
        ":path": "/tag/youhuo/page/2/",
        ": scheme":"https",
        "cookie":"Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1564130261,1564130316,1564130605; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1564130605",
        "upgrade-insecure-requests":"1"
    }

    for i in range(1,2):
        base_url = "https://www.mzitu.com/tag/youhuo/page/{}/".format(i)
        Meizi(base_url,headers)