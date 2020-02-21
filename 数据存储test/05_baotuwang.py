import requests
from lxml import etree


class Spider(object):
    def __init__(self):
        self.headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}


    def start(self,url):
        rsp = requests.get(url,headers=self.headers)
        html = rsp.text
        html = etree.HTML(html)
        video_src = html.xpath('//div[@class="video-play"]/video/@src')
        video_title = html.xpath('//span[@class="video-title"]/text()')
        self.write_file(video_src,video_title)
    def write_file(self,video_src,video_title):
        for src,title in zip(video_src,video_title):
            response = requests.get("http:"+src,headers = self.headers)
            filename = title+'.mp4'
            with open("/home/tlxy/下载/Pycharm/PycharmDemo/爬虫/数据存储test/05_videos/"+filename,'wb') as f:
                f.write(response.content)

if __name__ == '__main__':
    spider = Spider()
    for i in range(1,2):
        url = 'https://ibaotu.com/shipin/7-0-0-0-0-{}.html'.format(str(i))
        spider.start(url)