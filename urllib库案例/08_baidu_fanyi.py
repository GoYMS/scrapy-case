from urllib import request,parse
import json

def  Fanyi(information):
    url = 'https://fanyi.baidu.com/sug'
    data = {
        'kw':information
    }
    data = parse.urlencode(data)
    headers = {
        'content-length':len(data),
        'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
    }

    req = request.Request(url,data=data.encode(),headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    json_data = json.loads(html)
    for data in json_data['data']:
        print(data['k'],data['v'])



if __name__ == '__main__':
    information = input("请输入想要翻译的单词：")
    Fanyi(information)