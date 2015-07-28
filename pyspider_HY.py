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
'''河源'''

class Handler(My):
    name = "HY"
    mkdir = '/home/sheldon/web/'

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://www.ghjsj-heyuan.gov.cn/certificate.asp?categoryid=282&page=1', 
            callback=self.index_page, save={'type':'工程规划许可证'})
        self.crawl('http://www.ghjsj-heyuan.gov.cn/certificate.asp?categoryid=301&page=1', 
            callback=self.index_page, save={'type':'项目选址意见书'})
        self.crawl('http://www.ghjsj-heyuan.gov.cn/certificate.asp?categoryid=403&page=1', 
            callback=self.index_page, save={'type':'用地规划许可证'})

    def index_page(self, response):
        soup = BeautifulSoup(response.text)
        page_count = int(soup('a', {'href': re.compile(r'certificate')})[-1]['href'].split('=')[-1])

        url = response.url[:-1]
        for i in range(2, page_count + 1):
            link = url + str(i)
            self.crawl(link, callback=self.content_page, save=response.save)

        self.crawl(response.url, callback=self.content_page, force_update=True, save=response.save)