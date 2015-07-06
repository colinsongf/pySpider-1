import urllib2
import os
from multiprocessing.dummy import Pool as ThreadPool
import timeit

def download_attachment(url):
    f = urllib2.urlopen(url)
    fileout = os.getcwd() + '/attachment/' + os.path.basename(url)
    with open(fileout, 'wb') as code:
        code.write(f.read())

def thread_0():
    for url in url_list:
        download_attachment(url)

def thread_n(num):
    pool = ThreadPool(num)
    pool.map(download_attachment, url_list)
    pool.close()

fin = open('list.txt', 'r')
url_list = []
for line in fin.readlines():
    url_list.append(line.strip('\n'))
fin.close()

# t1 = timeit.Timer("thread_0()", 'from __main__ import thread_0, download_attachment')
# print t1.timeit(1)
t2 = timeit.Timer("thread_n(12)", 'from __main__ import thread_n, download_attachment')
print t2.timeit(1)
t3 = timeit.Timer("thread_n(13)", 'from __main__ import thread_n, download_attachment')
print t3.timeit(1)
t4 = timeit.Timer("thread_n(14)", 'from __main__ import thread_n, download_attachment')
print t4.timeit(1)