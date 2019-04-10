import requests
from bs4 import BeautifulSoup

headers={'User-Agent':'....'}

result=requests.get('url',headers=headers) 
result.encoding=('utf-8')
soup=BeautifulSoup(result.text,'html.parser')                   #将访问内容转化成text文件
userInfos=soup.find_all('div',{'id':'doc-bd'})  #在文档中查找在文档中的一个大的模块
#bs4 find 获取一个元素  find_all获取所有符合条件的
for userInfo in userInfos:
    content={
        'href':userInfo.x['href'],
        'title':userInfo.x['alt']
        ...#在相当的位置找到对应的需要的东西
    }


f=userInfo.find('div',{'class':'mod-bd js-tabs-live'}).img.attrs['src']    #在大的块中找指定的小的需要的
print(f)
