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
'''潮州'''

class Handler(My):
    name = 'CZ'
    mkdir = '/home/sheldon/web/'

    @every(minutes = 24 * 60)
    def on_start(self):
        self.crawl('http://czcsgh.gov.cn/yishu_s.asp?Page=1', fetch_type='js', callback=self.index_page)
        self.crawl('http://czcsgh.gov.cn/jsyd_s.asp?Page=1', fetch_type='js', callback=self.index_page)
        self.crawl('http://czcsgh.gov.cn/gcyd_s.asp?Page=1', fetch_type='js', callback=self.index_page)
        self.crawl('http://czcsgh.gov.cn/jsgcFj_s.asp?Page=1', fetch_type='js', callback=self.index_page)

    def index_page(self, response):
        soup = BeautifulSoup(response.text)

        page_count = int(soup('a', {'href': re.compile(r'\?Page=\d+')})[-1]['href'].split('&')[0].split('=')[1])
        url = response.url[:-1]
        for i in range(2, page_count + 1):
            link = url + str(i)
            self.crawl(link, fetch_type='js', callback=self.content_page)

        self.content_page(response) 