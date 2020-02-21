"""
csv  逗号分隔符
CSV文件由任意的数据记录组成，记录间以某种换行符进行分割，每行记录由换行符组成
例如：
ID,UserName,Age,Country
1001,yms,18,CH
1002,ll,19,USA

"""
import csv

headers = ['ID','UserName','Age','Country']
rows = [
    (1001,'yms',18,'CH'),
    (1002,'ll',19,'USA')
]

with open('02_est.csv','w') as f :
    f_csv = csv.writer(f)
    #单行数据用writerow，多行加s
    f_csv.writerow(headers)
    f_csv.writerows(rows)
