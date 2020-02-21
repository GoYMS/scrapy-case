from Xc_scrapy_03.items import XcdailiItem
from .sql import Sql

class XicidailiPipeline():
    def process_item(self,item,spider):
        if isinstance(item,XcdailiItem):
            #判断是否存在
            ipaddress = item['ipaddress']
            ret = Sql.select_name(ipaddress)
            if ret[0] == 1:
                print("已经存在啦")

            else:
                country =  item['country']
                ipaddress = item['ipaddress']
                port = item['port']
                serveraddr = item['serveraddr']
                isanonymous = item['isanonymous']
                type = item['type']
                alivetime = item['alivetime']
                verifictiontime = item['verifictiontime']
                Sql.insert_db_xici(country,ipaddress,port,serveraddr,isanonymous,type,alivetime,verifictiontime)










