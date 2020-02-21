# -*- coding: utf-8 -*-
import scrapy
from  Xc_scrapy_03.items import XcdailiItem

class XcdlSpider(scrapy.Spider):
    name = 'xcdl'
    allowed_domains = ['xicidaili.com']
    start_urls = ['https://www.xicidaili.com/']

    def parse(self, response):
       items_1 = response.xpath('//tr[@class="odd"]')
       items_2 = response.xpath('//tr[@class=""]')
       items = items_1+items_2

       infos = XcdailiItem()

       for item in items:
           #获取国家图片链接
           countries = item.xpath('./td[@class="country"]/img/@src').extract()  #extract() :序列化该节点末unicode字符串列表
           if countries !=[]:
               country = countries[0]
           else:
               country = '未知'

           #获取ip地址

           ipaddress = item.xpath('./td[2]/text()').extract()
           try :
               ipaddress = ipaddress[0]
           except:
               ipaddress = '未知'
           #获取端口号

           port = item.xpath('./td[3]/text()').extract()
           try :
               port = port[0]
           except:
               port = '未知'

           #获取服务器地址

           serveraddr = item.xpath('./td[4]/text()').extract()
           try :
               serveraddr = serveraddr[0]
           except:
               serveraddr = '未知'

           #获取是否匿名

           isanonymous = item.xpath('./td[5]/text()').extract()
           try :
               isanonymous = isanonymous[0]
           except:
               isanonymous = '未知'

           #获取类型
           type =  item.xpath('./td[6]/text()').extract()
           try :
               type = type[0]
           except:
               type = '未知'

           #存活时间
           alivetime = item.xpath('./td[7]/text()').extract()
           try :
               alivetime = alivetime[0]
           except:
               alivetime = '未知'

           #验证时间
           verifictiontime = item.xpath('./td[8]/text()').extract()
           try :
               verifictiontime = verifictiontime[0]
           except:
               verifictiontime = '未知'

           print(verifictiontime,alivetime,type)
           infos["country"] =country
           infos["ipaddress"] =ipaddress
           infos["port"] =port
           infos["serveraddr"] =serveraddr
           infos["isanonymous"] =isanonymous
           infos["type"] =type
           infos["alivetime"] =alivetime
           infos["verifictiontime"] =verifictiontime


           yield infos
