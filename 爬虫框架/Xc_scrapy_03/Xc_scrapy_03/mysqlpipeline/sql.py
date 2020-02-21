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
    def insert_db_xici(cls,country,ipaddress,port,serveraddr,isanonymous,type,alivetime,verifictiontime):
        sql = 'insert into xicidaili(country,ipaddress,port,serveraddr,isanonymous,type,alivetime,verifictiontime) VALUES (%(country)s,%(ipaddress)s,%(port)s,%(serveraddr)s,%(isanonymous)s,%(type)s,%(alivetime)s,%(verifictiontime)s)'

        value = {
            "country":country ,
            "ipaddress":ipaddress,
            "port":port,
            "serveraddr":serveraddr,
            "isanonymous":isanonymous,
            "type":type,
            "alivetime":alivetime,
            "verifictiontime":verifictiontime
        }

        try:
            #执行语句
            cursor.execute(sql,value)
            ##提交执行
            db.commit()
        except Exception as e:
            print('插入失败')
            print(e)
            db.rollback()
    #去重
    @classmethod
    def select_name(cls,ipaddress):
        sql = "select exists(select 1 from xicidaili where ipaddress=%(ipaddress)s)"
        value = {
            'ipaddress' : ipaddress
        }
        cursor.execute(sql,value)
        return cursor.fetchall()[0]
