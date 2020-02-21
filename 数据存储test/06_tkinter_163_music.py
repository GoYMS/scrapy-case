from tkinter import *
import requests
from urllib import request
from bs4 import BeautifulSoup

"""
通过这个项目明白了爬虫并不是说按照一定的格式就一定会成功的 中间太多的意外等其他情况
"""

"""
网易云音乐有一个外链:http://music.163.com/song/media/outer/url?id=



1.获取页面的源码
2.获取歌曲id和歌曲名称
3.下载音乐
"""


def music_spider():
    #获取用户输入的url地址
    url = entry.get()
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
        'referer': 'https://music.163.com/',
        'upgrade-insecure-requests': '1'

    }
    #请求页面详细信息
    rsp = requests.get(url,headers=headers)

    #创建soup对象
    soup = BeautifulSoup(rsp.text,'lxml')

    #获取id与歌曲名称
    items = soup.find('ul',{'class':'f-hide'}).find_all('a')
    for item in items:
        music_id = item.get('href').strip('/song?id=')  #strip 删除指定字符串
        music_name = item.text
        #歌曲下载地址
        song_url = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(music_id)

        #添加数据到列表框中
        text.insert(END,"正在下载{}".format(music_name))
        #文本框自动向下滚动
        text.see(END)
        #更新
        text.update()

        #下载
        path = '/home/tlxy/下载/Pycharm/PycharmDemo/爬虫/数据存储test/06_music/'+music_name+'.mp3'
        rsp = requests.get(song_url,headers=headers,allow_redirects=False)
        m_url = rsp.headers['Location']
        #urlretrieve()方法直接将远程数据下载到本地
        try:
            request.urlretrieve(m_url,path)
        except:
            print("{}下载失败".format(music_name))


#创建窗口
root =Tk()

#设置标题
root.title("网易云音乐下载器")

#设置窗口大小
root.geometry("850x550")

#设置窗口显示位置
root.geometry("+350+200")

#设置下载器标签，请输入下载的地址
lable = Label(root,text="请输入下载的地址",font=(20))
#定位
lable.grid()

#设置输入框
entry = Entry(root,width=34)
entry.grid(row=0,column=1)

#设置列表框
text = Listbox(root,font=(20),width=100)
text.grid(row=1,columnspan=2)

#设置开始按钮
buttorn = Button(root,text='Start',width=35,command=music_spider).grid(row=2,column=0,sticky='w')  #sticky  上下左右

#设置退出按钮
buttorn = Button(root,text='End',width=35,command=root.quit).grid(row=2,column=1,sticky='e')  #sticky  上下左右


#消息循环，显示窗口
root.mainloop()
