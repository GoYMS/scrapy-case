from selenium import webdriver

from scrapy.http.response.html import HtmlResponse
import time

class Qidianmiddlewares(object):


    def process_request(self,request,spider):
        #只处理情况页面请求
        if request.meta.get('phantomjs',True):
            print('走自定义中间件')
            driver = webdriver.PhantomJS()
            driver.get(request.url)
            time.sleep(1)
            #得到页面
            html = self.driver.page_source

            #返回得到的信息
            return HtmlResponse(url=request.url,body=html,encoding='utf-8',request=request)