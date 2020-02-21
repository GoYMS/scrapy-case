"""
百度贴吧
首页的url：https://tieba.baidu.com/f?ie=utf-8&kw=%E9%87%91%E5%BA%B8%E5%90%A7&fr=search
urllib.parse: 用来解析各种数据格式的文件


这个案例与原来讲的案例不太一样，对于url后边的参数，有两种做法，
第一是将参数数据进行解码编码后传入request.Request中，例如大拿讲的
第二是直接将baseurl与参数进行拼接，形成一个完整的url，只需要进行解析，不需要再将参数encode，
      也不用在request.Request传入参数，例如下面例子

"""
from urllib import request,parse

def tieba():
    baseurl = 'https://tieba.baidu.com/f?'
    name = input("请输入贴吧名字")
    page = input("请输入页数")
    #这里边的数据名称需要根据页面f12里边的一样
    for i in range(int(page)):
        ps = {
            'kw' : name,
            'pn' : i*50
        }

        #将得到的参数数据进行编码
        data = parse.urlencode(ps)
        #将参数与baseurl进行拼接
        url = baseurl+data

        header = {
            "User-Agent" : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
        }

        req = request.Request(url,headers=header)
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        #还是按照文件打印出来吧
        with open("03_金庸贴吧第{0}页.html".format(i+1),'w',encoding='utf-8') as f:
            f.write(html)

if __name__ == '__main__':
    tieba()





