from lianjia_scrapy_04.items import LianJiaItem
from .sql import Sql

class LianjiaPipeline():
    def process_item(self,item,spider):
        if isinstance(item,LianJiaItem):
            #判断是否存在
            house_title = item['house_title']
            ret = Sql.select_name(house_title)
            if ret[0] == 1:
                print("已经存在啦")

            else:
                house_title =  item['house_title']
                house_href =  item['house_href']
                house_name =  item['house_name']
                house_num =  item['house_num']
                house_price  =  item['house_price']
                house_style =  item['house_style']
                house_ting =  item['house_ting']
                house_size =  item['house_size']
                house_fangxiang =  item['house_fangxiang']
                Sql.insert_db_lianjia(house_title,house_href,house_name,house_num,house_price,house_style,house_ting,house_size,house_fangxiang)






