from urllib import request
import ssl

#ssl免认证，如果出现ssl报错，可以使用下边一行的方法
ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://www.csls.cdb.com.cn/page.do?targetPage=/OnlineIndex.jsp'
rsp = request.urlopen(url)
html = rsp.read().decode('GBK')
print(html)