"""
原来访问人人网时通过查看源代码就知道登录成功的url，但是华为在源码中没有给出，方法是：
 使用正确的用户名和错误的密码，点击登录后查看NetWork，上边会显示将要访问的URL即登录成功的地址，下边form data有用户名和密码对应的name


action_url:'https://uniportal.huawei.com/uniportal/login.do'
uid:1789353033@qqcom
password:123456
data传入的数据必须为bytes格式

"""
from urllib import request,parse
from http import cookiejar

def  Opener():

    #生成cookie对象
    cookie = cookiejar.CookieJar()
    #生成cookie管理器
    cookie_handler = request.HTTPCookieProcessor(cookie)
    #生成http请求管理器
    http_handler = request.HTTPHandler()
    #生成https请求管理器
    https_handler = request.HTTPSHandler()
    #构建发起请求管理器
    global opener
    opener = request.build_opener(cookie_handler,http_handler,https_handler)


def HuaweiLogin(url):
    data = {
        "userName":"Tom_yangm",
        "pwd":"07221201ymslhq?",
        "languages":"zh",
        "fromsite":"www.huawei.com",
        "authMethod":"password"
    }
    data = parse.urlencode(data).encode()
    req = request.Request(url,data=data)
    response = opener.open(req)
    html = response.read().decode()
    print(html)
if __name__ == '__main__':
    url = 'https://www.huawei.com/en/accounts/LoginPost'
    Opener()
    HuaweiLogin(url)