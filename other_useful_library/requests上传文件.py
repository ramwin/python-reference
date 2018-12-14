#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-07-04 14:08:42

import requests

url = 'http://localhost:8000/api/v1/user/avatar'
files = {'files': open('./portrait.png', 'rb')}
headers = {
    # 'Authorization': 'Token 76ec5ef11050fefd51deb836b3c795b7ddca3bee', # wangxiang
    'Authorization': 'Token 43a215c5de33d99f8a3c049310c5186dfaea1947', # zoe
    # 'Content-Type': 'Application/json',
}
r = requests.put(url, files=files, headers=headers)

# url = 'http://192.168.1.60:8080/api/v1/crm/LandSeaDocReceptionRecord'
# files = {'file': ('test.txt', 'test text')}
# values = {
# }
# r = requests.post(url, files=files, data=values)
