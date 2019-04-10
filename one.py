from bs4 import BeautifulSoup
import requests
from lxml import etree
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',}
def get_detail_url():
    start_urls=['https://www.ximalaya.com/ertong/p{}/'.format(pn) for
                pn in range(1,35)]#列表推导式
    print(start_urls)
get_detail_url()