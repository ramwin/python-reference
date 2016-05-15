#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-05-07 22:51:28


import time
import requests

clock = time.time()
requests.get(url='http://180.97.33.107')
requests.get(url='http://121.40.228.140')
requests.get(url='http://58.213.63.170')
# requests.get(url='http://121.43.18.33')
# requests.get(url='http://128.199.67.128')
iptime = time.time() - clock
clock = time.time()
requests.get('http://www.baidu.com')
requests.get('http://www.zettage.com')
requests.get('http://www.zettage.net')
# requests.get('http://www.taobao.com')
domaintime = time.time() - clock
clock = time.time()
print('IP访问耗时 %s 秒'%(iptime))
print('域名访问   %s 秒'%(domaintime))
