"""
代理服务器
"""
from urllib import request
import random

def Proxy():
    proxy_list = [
        #前边是类型，后边是IP+端口号
        {"https":"49.86.176.144:9999"},
        {"http":"120.83.109.18:9999"},
        {"http":"27.43.190.188:9999"}
    ]

    proxy = random.choice(proxy_list)
    #构建代理服务器
    proxy_handler = request.ProxyHandler(proxy)
    #创建网络请求对象opener
    opener = request.build_opener(proxy_handler)
    url = "http://www.langlang2017.com/"
    header = {
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
    }
    req = request.Request(url,headers=header)
    rsp = opener.open(req)
    html = rsp.read().decode()
    print(html)


if __name__ == '__main__':
    Proxy()