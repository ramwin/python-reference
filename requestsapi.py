#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-08-17 13:32:31

import requests
import json
import random
import string
import pprint
import time
start = time.time()

headers = {
    # 'Authorization': 'Token 76ec5ef11050fefd51deb836b3c795b7ddca3bee', # wangxiang
    'Authorization': 'Token 43a215c5de33d99f8a3c049310c5186dfaea1947', # zoe
    'Content-Type': 'Application/json',
}

params = {
    'name': '拼音',
}

data = {
    'group'
}

def result(r):
    pprint.pprint('status_code: %d' % r.status_code)
    pprint.pprint('content: %s' % r.text)

# 获取单个简报
# response = requests.get(
#     url = 'http://localhost:8000/api/v1/weeklypaper/brief/1',
#     headers = headers,
# )
# 获取所有简报
# response = requests.get(
#     url = 'http://localhost:8000/api/v1/weeklypaper/brief',
#     headers = headers,
# )
# 制作简报
# response = requests.post(
#     url = 'http://localhost:8000/api/v1/weeklypaper/brief',
#     data = {
#         "opr_user": 6,
#         "weekly_paper": 89, "comment": "测试简报",
#     },
#     headers = headers,
# )

# 上传头像
# url = 'http://localhost:8000/api/v1/user/avatar'
# data = {
#     "avatar": open("test/png.txt", "r").read(),
#     "filename": "test/123.png",
# }
# response = requests.post(url, headers=headers, data=data)
# 标签
# response = requests.get(
#     url='http://localhost:8000/api/v1/weeklypaper/label',
#     headers=headers,
#     params = {
#         'tag_name': 'se'
#     }
# )

# 获取周报
response = requests.get(
    url='http://localhost:8000/api/v1/weeklypaper/?page=1',
    headers=headers,
    params = {
        'user_id': 28,
        # 'user_id': 6,
        # 'page': 4,
    }
)

# 创建周报
# data = {
#     'title': "周报测试" + "".join(random.sample(string.ascii_letters,10)),
#     'status': 2,
#     'todos': {
#         # 'achievements': [13,],
#         # 'plans': [3,],
#     }
# }
# response = requests.post(
#     url='http://localhost:8000/api/v1/weeklypaper/',
#     headers=headers,
#     data=json.dumps(data)
# )

# 查看周报
# response = requests.get(
#     url='http://localhost:8000/api/v1/weeklypaper/110',
#     headers=headers,
# )

    

# response = requests.post(
#     url='http://localhost:8000/api/v1/weeklypaper/1/todolist/1',
# )



# 快速创建 todo
# response = requests.post(
#     url='http://localhost:8000/api/v1/todo/quickcreate',
#     headers=headers,
#     data=json.dumps({"title": "测试创建todo", "status":0, "type": "plan"}),
# )

# 获取 todo 列表
# response = requests.get(
#     url='http://localhost:8000/api/v1/todo',
#     headers=headers,
#     params = {'style': 'simple'})

# 修改TODO
# response = requests.patch(
#     url='http://localhost:8000/api/v1/todo/2',
#     headers=headers,
#     data=json.dumps({'group':12}),
#     )

# 导入数据
# response = requests.post(
#     url='http://localhost:8000/api/v1/common/test',
# )

# 获取group
# response = requests.get(
#     url='http://localhost:8000/api/v1/todo/group',
#     headers=headers,
# )

# 获取group detail
# response = requests.get(
#     url='http://localhost:8000/api/v1/todo/group/26',
#     headers=headers,
# )

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
end = time.time()
result(response)
print('耗时 %0.2f 秒' % (end-start))
