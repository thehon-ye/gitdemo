import requests
from bs4 import BeautifulSoup
from lxml import etree

#headers = {
#    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
#}


#def get_detail_url():
    start_urls_A=['https://www.ximalaya.com/search/album/english/p{}'.format(pn)  for pn in range(1,52,2)]
    start_urls_B=['https://www.ximalaya.com/search/album/english/sc/p{}'.format(pn)  for pn in range(0,52,2)]
    start_urls_C=start_urls_B[1:10]
    start_urls_D=[]
    for i in range(0,10):
        start_urls_D.append(start_urls_A[i])
        start_urls_D.append(start_urls_C[i]
    print(start_urls_D)


    #for start_url in start_urls:
    #    response = requests.get(start_url,headers=headers).text#没有伪装成浏览器去访问
    #    soup = BeautifulSoup(response,'lxml')
    #   for item in soup.find_all('div',class_='xm-album-cover'):
     #       print(item)
      #      break
       # break


        #print(response)

if __name__ == '__main__':
    get_detail_url()
    #获取首页的音频详情