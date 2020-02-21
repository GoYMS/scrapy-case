from selenium import webdriver
from scrapy.http.response.html import HtmlResponse
import time
class Xiaohuadownmiddlerwares(object):
    def process_request(self,request,spider):
        """
        自定义下载中间件
        :param request: 请求对象
        :param spider: 请求爬虫
        :return:
        """
        driver = webdriver.PhantomJS()

        driver.get(request.url)
        time.sleep(2)
        driver.save_screenshot('1.png')
        js = 'document.body.scrollTop=10000'
        driver.execute_script(js)
        time.sleep(3)
        driver.save_screenshot('2.png')
        html = driver.page_source
        driver.quit()

        #一定记住return
        #HtmlResponse对应的是爬虫中的parse函数，也就是 xiaohua.py 中的函数
        return HtmlResponse(url=request.url,encoding='utf-8',body=html,request=request)