import requests
from bs4 import BeautifulSoup



def getHTMLText(url):
    '''
	此函数用于获取网页的html文档
	'''
    try:
        #获取服务器的响应内容，并设置最大请求时间为6秒
        res = requests.get(url, timeout = 6)
        #判断返回状态码是否为200
        res.raise_for_status()
        #设置该html文档可能的编码
        res.encoding = res.apparent_encoding
        #返回网页HTML代码
        return res.text
    except:
        return'产生异常'

def main():
    '''
	主函数
	'''
    print("执行中....")
    #目标网页
    url='https://cn.bing.com/';
    
    demo=getHTMLText(url)

    #解析HTML代码
    soup=BeautifulSoup(demo,'html.parser')
	#得到图片网址
    pic=url+soup.find(id='bgLink').get('href')
    print(pic)
    pic=pic[0:pic.rfind('&rf')]
    print(pic)
    pic=pic.replace('_1920x1080','_UHD')
    print(pic)
	#获得图片名字
    name=soup.find(id='sh_cp').get('title')
    print(name)
    #将名字中的/替换
    name=name.replace('/','_',5)
    print(name)
	#储存在D:/bingpicture/下
    name='D:/bingpicture/'+name+'.jpg'
    r=requests.get(pic)
    with open(name,'wb')as f:
        f.write(r.content)

main()
	
