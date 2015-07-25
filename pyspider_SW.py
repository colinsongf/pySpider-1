from pyspider.libs.base_handler import *
from my import My
from bs4 import BeautifulSoup
import hashlib
import re
import os
import redis
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.parse import urlunparse
'''汕尾'''

class Handler(My):
    name = 'SW'
    mkdir = '/home/sheldon/web/'

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://www.swghj.gov.cn/gs/gd.htm', callback=self.index_page)

    def index_page(self, response):
        soup = BeautifulSoup(response.text)

        next_link = ''
        t = soup('a')
        for i in t:
            if i.get_text() == '上一页':
                link = urljoin(response.url, i['href'])
                next_link = link
                self.crawl(link, callback=self.index_page) 

        lists = soup.find('table', {'width':'100%'}).find_all('a', {'href': re.compile(r'')})
        print(len(lists))
        for i in lists:
            link = urljoin(response.url, i['href'])
            if link != next_link:
                print(link)
                self.crawl(link, callback=self.content_page)

        