#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2018-12-14 11:54:27

import requests
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename='./test.log',
    filemode='a')
formatter = logging.Formatter("%(asctime)s %(filename)s")

count = 3
url = "https://httpbin.org/get"
url = "https://publicstatic.duishang.net/avatar-2586"

start1 = time.time()
for i in range(count):
    requests.get(url)
end1 = time.time()


start2 = time.time()
s = requests.Session()
for i in range(count):
    s.get(url)
end2 = time.time()

print("直接使用requests.get请求{}, {}次耗时{}秒".format(url, count, end1-start1))  # 9.81
print("直接使用session.get请求{}, {}次耗时{}秒".format(url, count, end2-start2))  # 3.2
