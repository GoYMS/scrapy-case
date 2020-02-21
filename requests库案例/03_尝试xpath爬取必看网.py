"""
由于妹子网无法爬取，这次尝试爬取一下必看网上的书，纯自己写
经历一小时后....
个人感觉还是比较不错的虽然没有完美，但是还可以

"""
import requests
from lxml import etree
import re
import os


def AllBooks(base_url,headers):
    rsp =requests.get(base_url,headers)
    #传进去的参数必须是string形式
    html = etree.HTML(rsp.text)
    #获取所有的书
    all_books = html.xpath('//div[@class="bookList clearfix"]/ul/li/a/@href')

    #https: // www.biikan.com
    for book_url in all_books:

        Book('https://www.biikan.com'+book_url)

def Book(book_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50"
    }
    rsp = requests.get(book_url,headers)
    html = etree.HTML(rsp.text)
    #此处，想要获取标签内容，需要在相应标签后边加上text()。例如下边
    #获取标题
    title = html.xpath('//div[@class="bookCon"]/h1/text()')[0]
    #获取总共的章数
    pages =  html.xpath('//div[@class="overflow-h bookNavList"]/ul/li/a/text()')[-1]
    page = re.findall(r'\d+\.?\d*',pages)
    num_page = page[0]
    #获取每页的地址
    for num in range(1,int(num_page)+1):
         numpage = num
    #获取每章的地址,进行拼接
    url = html.xpath('//div[@class="overflow-h bookNavList"]/ul/li/a/@href')
    for ii in url:
        bookurl = 'https://www.biikan.com'+ str(ii)
        Download(bookurl,title)

#下载内容
def Download(bookurl,title):
     rsp = requests.get(bookurl)
     html = etree.HTML(rsp.text)
     #获取内容
     write = html.xpath('//div[@class="readContent"]/text()')
     #将list装换成str形式
     writes = ','.join(write)
     with open(title,'w') as f:
         f.write(writes)

if __name__ == '__main__':
    base_url = 'https://www.biikan.com/wenxue'
    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"
    }

    AllBooks(base_url,headers)