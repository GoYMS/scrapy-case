"""
郎朗渔家
首页：http://www.langlang2017.com/index.html
来岛路线：http://www.langlang2017.com/route.html
常见问题：http://www.langlang2017.com/FAQ.html
注意：以后写代码，要么在函数里边，要不在面向对象里边，不要自己直接上去就是代码

"""

from urllib import request
import random

def spider(url):
    user_angents = [
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24',
        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3'
    ]
    #随机获取useragent
    user_angent = random.choice(user_angents)
    headers = {
        'User-Agent' : user_angent
    }
    req = request.Request(url,headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    #将文件保存到一个html文件中
    name = url.split('/')
    filename ='02_'+ name[-1]
    with open(filename,'w',encoding='utf-8') as f:
        f.write(html)


if __name__ == '__main__':
    urls = [
            'http://www.langlang2017.com/index.html',
            'http://www.langlang2017.com/route.html',
            'http://www.langlang2017.com/FAQ.html'
    ]
    for url in urls:
        spider(url)