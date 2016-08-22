#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-08-17 13:32:31

import requests
headers = {
    'Authorization': 'Token 76ec5ef11050fefd51deb836b3c795b7ddca3bee',
    'Content-Type': 'Application/json',
}

params = {
    'name': '拼音',
}

data = {
}

def result(r):
    print('status_code: %d' % r.status_code)
    print('content: %s' % r.text)


# # 获取周报
# response = requests.get(
#     url='http://localhost:8000/api/v1/weeklypaper/',
#     headers=headers,
# )
# result(response)

# # 删除group
# response = requests.delete(
#     url='http://localhost:8000/api/v1/todo/group/2',
#     headers=headers,
# )
# result(response)




# # 上传group
# url = 'http://localhost:8000/api/v1/todo/group'
# response = requests.post(
#     url=url,
#     data=data,
#     headers=headers,
#     params=params,
#     )
# print(response.text)
# 
# 
# 
# url = 'http://localhost:8000/api/v1/common/pinyin'
# response = requests.get(
#     url=url,
#     # data=data,
#     headers=headers,
#     params=params,
#     )
# print(response.text)
# 
