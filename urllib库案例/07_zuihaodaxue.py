from urllib import request
from lxml import etree

def University():
    url = 'http://zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    rsp = request.urlopen(url)
    html = rsp.read().decode()

    html = etree.HTML(html)
    items = html.xpath('//tr[@class="alt"]')
    for item in items:
        #排名
        number = item.xpath('./td')[0].text
        #学校
        university = item.xpath('.//div[@align="left"]')[0].text

        #省份
        addr = item.xpath('./td')[2].text
        #总分
        score = item.xpath('./td')[3].text
        print(number+"--"+university+"--"+addr+"--"+score)



if __name__ == '__main__':

    University()