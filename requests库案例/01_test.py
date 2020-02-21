import requests

url = 'https://www.baidu.com'

try:
    rsp = requests.get(url)
    print(rsp.url)
    print(rsp.apparent_encoding)
except:
    print("error")