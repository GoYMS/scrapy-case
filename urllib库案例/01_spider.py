from urllib import request
"""
百度简单爬取

url = 'http://www.baidu.com'
rsp = request.urlopen(url)
html = rsp.read().decode()
print (html)
"""

url = 'http://www.w3school.com.cn/json/index.asp'
rsp = request.urlopen(url)
#decode里边的内容都需要观察源码用的编码格式，需要一致
html = rsp.read().decode('gbk')
print(html)