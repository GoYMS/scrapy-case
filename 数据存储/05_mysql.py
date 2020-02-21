"""
Ubunto环境安装mysql：
     -sudo apt-get update
     -sudo apt-get install mysql-server
     -sudo apt-get install mysql-client
     - sudo apt-get install libmysqlclient-dev
登录数据库
    sudo mysql -u root -p
"""




#Python 操作mysql 创建数据表


import pymysql
# try:
#         #获取一个数据库链接
#         #打开数据库链接
#         #host: 数据库服务器地址
#         #user :登录数据库的用户
#         #password 用户密码
#         #db ：所要连接的数据库名
#         #port ： 数据库端口号，默认是3306
#         db = pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='test',port=3306)
#         #创建游标，对数据进行操作，使用cursor()方法
#         cursor = db.cursor()
#         #使用execute()执行sql语句
#         cursor.execute('DROP TABLES IF EXISTS FIRST')   #判断表格是否存在
#         #写sql语句
#
#         sql = """
#             CREATE TABLE FIRST(
#             FIRST_NAME CHAR(20) NOT NULL,
#             LAST_NAME CHAR(20),
#             AGE INT,
#             SEX CHAR(1),
#             INCOME FLOAT
#             )
#         """
#         cursor.execute(sql)
#         db.close()
# except Exception as e:
#     print(e)




#数据库插入操作




db = pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='test',port=3306)
#利用cursor（）创建游标对象
cursor = db.cursor()

#sql语句
sql = 'INSERT INTO FIRST(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME) VALUES ("li","qi",18,"w","10000")'

#为了防止sql注入，执行以下sql语句也可以
"""
sql = "INSERT INTO FIRST(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME) VALUES ('%s','%s','%d','%c','%d')"%('li','qi',16,'M','99999')
"""
try:
    #执行sql语句
   cursor.execute(sql)
    #提交执行
   db.commit()

except Exception as e:
    #发生意外
    print(e)
    # 就是数据库里做修改后，未commit 之前 使用rollback 可以恢复数据到修改之前。
    db.rollback()
#关闭
db.close()



# #数据库查询操作
#
#
# try :
#     db = pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='test',port=3306)
#     #创建游标
#     cursor = db.cursor()
#     cursor.execute('select * from FIRST')
#     # datas = cursor.fetchall()  #fetchall 接受全部返回结果
#     # for data in datas:
#     #     print(data)
#     datas = cursor.fetchone()  #获取下一个查询结果
#     print(datas)
#     db.close()
#     cursor.close()
#
# except Exception as e:
#     print(e)
#
#


