import pymysql


#数据库链接操作

db = pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='test',port=3306)

#创建游标
cursor = db.cursor()

#sql语句更新

sql= "DELETE FROM FIRST WHERE FIRST_NAME = 'YANG'"


try:
    cursor.execute(sql)
    #提交
    db.commit()

except Exception as e:
    db.rollback()
    print(e)

db.close()