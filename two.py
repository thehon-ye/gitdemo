from bs4 import BeautifulSoup   #获取网页的内容的
import requests
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
def get_detail_url():
    start_urls=('http://sports.sina.com.cn/run/2019-03-22/doc-ihsxncvh4719137.shtml')

    for start_url in start_urls:
        response=requests.get(start_url,headers=headers).text
        soup= BeautifulSoup(response,'html')
        soup.encode(encoding='utf-8')
        for item in soup.find_all('div',class_='article'):
            print(item)


get_detail_url()

