#获取所有主播ID
#获取主播的花椒ID
#直接匹配数据


from bs4 import BeautifulSoup
import requests
import re
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
def get_liveId():
    liveIds = set()  #一种数据类型(数据不会重复）
    response =requests.get('http://www.huajiao.com/category/1000')
    soup = BeautifulSoup(response.text,'html.parser')
    for link in soup.find_all('a',href = re.compile('^(/l/)')):
        href = link.attrs['href']   #link 是一个标签  取里面的href属性
        liveId = re.findall('[0-9]+',href)  #  +表示匹配一次到多次
        liveIds.add(liveId[0])
    return(liveIds)

def get_userid(liveId):
    live_url = 'http://www.huajiao.com/l/{}'.format(liveId)         #字符串格式化
    response = requests.get(live_url,headers=headers)
    soup =BeautifulSoup(response.text,'html.parser')
    text = soup.title.get_text()
    user_id = re.findall('[0-9]+',text)
    return user_id[0]
def get_UserData(userId):
    print('正在获取ID为：{}的主播信息'.format(userId))
    result = requests.get('http://www.huajiao.com/user/{}'.format(userId))
    soup =BeautifulSoup(result.text,'html.parser')
    data={}
    userInfo = soup.find('div',{'id':'userInfo'})
    data['Actar'] = userInfo.find('div',{'class':'avatar'}).img.attrs['src']
    print(data['Actar'])




if __name__ == '__main__':
    liveIds=get_liveId()
    for liveId in liveIds:
        userid=get_userid(liveId)
        get_UserData(userid)

