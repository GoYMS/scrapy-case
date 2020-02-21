import pymysql

from Xc_scrapy_03 import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

#链接数据库
db = pymysql.connect(user=MYSQL_USER,password=MYSQL_PASSWORD,host=MYSQL_HOSTS,port=MYSQL_PORT,database=MYSQL_DB,charset="utf8")  #此处写utf8就行

cursor = db.cursor()

class Sql():
    #classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，
    # 但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等
    @classmethod
    def insert_db_lianjia(cls,house_title,house_href,house_name,house_num,house_price,house_style,house_ting,house_size,house_fangxiang):
        sql = 'insert into lianjia(house_title,house_href,house_name,house_num,house_price,house_style,house_ting,house_size,house_fangxiang) ' \
              'VALUES (%(house_title)s,%(house_href)s,%(house_name)s,%(house_num)s,%(house_price)s,%(house_style)s,%(house_ting)s,%(house_size)s,%(house_fangxiang)s)'

        value = {
                  "house_title":house_title,
                  "house_href": house_href,
                  "house_name":house_name,
                  "house_num":house_num,
                  "house_price":house_price,
                  "house_style":house_style,
                  "house_ting":house_ting,
                  "house_size":house_size,
                  "house_fangxiang":house_fangxiang

        }
        try:
            #执行语句
            cursor.execute(sql,value)
            ##提交执行
            db.commit()
        except Exception as e:
            print('插入失败',e)

            db.rollback()
    #去重
    @classmethod
    def select_name(cls,house_title):
        sql = "select exists(select 1 from lianjia where house_title=%(house_title)s)"
        value = {
            'house_title' : house_title
        }
        cursor.execute(sql,value)
        return cursor.fetchall()[0]

            # house_title
            # house_href
            # house_name
            # house_num
            # house_price
            # house_style
            # house_ting
            # house_size
            # house_fangxiang