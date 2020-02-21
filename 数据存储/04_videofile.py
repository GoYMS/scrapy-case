"""
音频文件存储
以前存储方法：
with  open(filename,'wb') as f:
    f.write()
"""
"""
获取到下载文件的url，二进制的方法下载
urllib 模块提供的urlretrieve（），此模块可以进行音频文件的下载
        也支持将远程数据下载到本地
urlretrieve(url, filename=None, reporthook=None, data=None):
url:下载文件的url地址
filename：数据存储路径+文件名
reporthook：要求回调函数，链接上服务器或者相应数据传输下载完毕时触发该回调函数
            显示当前的下载进度
data：(filename,headers) 元组  


"""
from urllib import request
import requests
from lxml import etree
import random
import os

#创建回调函数

def Schedule(blocknum,blocksize,totalsize):
    """
    显示下载进度
    :param blocknum:  已经下载的数据块
    :param blocksize: 数据块的大小
    :param totalsize: 远程文件的大小
    :return:
    """
    per = 100.0 * blocknum*blocksize/totalsize
    if per > 100:
        per = 100
    print("当前下载进度{0}".format(per))



def Dounlod():
    user_angent_list = [
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.33 Safari/534.3 SE 2.X MetaSr 1.0',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201'
    ]
    headers = {
        "User-Agent" : random.choice(user_angent_list)
    }
    url = 'https://www.ivsky.com/tupian/ziranfengguang/'
    html = requests.get(url,headers= headers)
    html = etree.HTML(html.text)
    #获取所有图片的链接
    page_urls = html.xpath('//div[@class="il_img"]/a/img/@src')
    for page_url in page_urls:
        #得到的url不完整，所以需要进行拼接
        img_url = 'https:'+page_url
        #以下创建文件夹的步骤
        root_dir = '04_mg'
        if not os.path.exists(root_dir):  #判断是否创建成功
            os.makedirs(root_dir)     #如果不成功创建文件夹
        filename = img_url.split('/')[-1]   #文件的命名，使用split以 / 进行分割，取最后一个
        #使用这个模块进行下载
        request.urlretrieve(img_url,root_dir+'/'+filename,Schedule)     #数据存储路径 root_dir+'/'+filename 其中虚拟机中是/  ，在win中是//


if __name__ == '__main__':
    Dounlod()
