import requests
from  bs4 import BeautifulSoup

def Boke():
    headers = {
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36",
        "referer": "https://www.cnblogs.com/cate/python/"
    }
    url = 'https://www.cnblogs.com/cate/python/'

    html = requests.get(url)

    soup = BeautifulSoup(html.text,'lxml')
    items = soup.select('div[class="post_item_body"]')
    for item in items:
        #获取标题
        title = item.select('h3 a[class="titlelnk"]')[0].get_text()
        #print(title)
        #详情链接
        href = item.select('h3 a[class="titlelnk"]')[0]['href']
        #作者
        writer = item.select('div a[class="lightblue"]')[0].get_text()
        #作者主页的信息
        writer_main = item.select('div a[class="lightblue"]')[0].get('href')
        #简要信息
        main = item.select('p[class="post_item_summary"]')[0].get_text()
        print(title,href,writer)

if __name__ == '__main__':
    Boke()