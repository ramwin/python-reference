#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2019-12-16 20:05:29

import pprint
text = '''
Accept: */*
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Connection: keep-alive
Content-Length: 42
Content-type: application/x-www-form-urlencoded
Cookie: UM_distinctid=16f0e90a15326b-02ba3d0c2f81b4-2e04407d-1fa400-16f0e90a154136; CNZZDATA1273275351=1029689493-1576494103-%7C1576494103
Host: m.ylpc07.com
Origin: http://m.ylpc07.com
Referer: http://m.ylpc07.com/
User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36
'''

headers = text.strip().split('\n')
header_dict = {}
for key, value in map(
        lambda x: x.split(': ', 1),
        headers):
    header_dict[key] = value
print(header_dict)
