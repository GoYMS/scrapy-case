"""
python对json文件分为编码和解码

编码：

dumps ：字符串
dump ： json对象，可以通过fp文件流写入文件

解码
   load  ：
   loads  ： 针对字符串

"""

import requests,json
from bs4 import BeautifulSoup

headers = {
    "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
}
url = 'http://www.seputu.com/'
rsp = requests.get(url,headers=headers)
soup = BeautifulSoup(rsp.text,'lxml')
#直接属性需要加个下划线
content = []
for mulu in soup.find_all(class_="mulu"):
    #取大标题
    h2 = mulu.find('h2')
    if h2 != None :
        h2_title = h2.string
        list = []
        #获取每个小标题与url地址
        for a in mulu.find(class_="box").find_all('a'):
            href = a.get('href')
            title = a.get('title')
            list.append({'href':href,'little_title':title})
        content.append({'title':h2_title,'content':list})
#将数据以json的格式存入
with open('01_gcd.json','a',encoding='utf-8') as f:
    #indent会使页面整齐
    #这是因为json.dumps 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False：
    json.dump(content,fp=f,indent=4,ensure_ascii=False)