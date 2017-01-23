#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-01-18 17:35:23

# -*- coding: utf-8 -*-
# flake8: noqa

from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
import requests

#需要填写你的 Access Key 和 Secret Key
access_key = 'Zy3HE44UK9tRACuAeEL3mxc8aTTj0jgZkrjxrJAB'
secret_key = 'wLXODkNWpzFj_SI60zu5GjjOVZzxmvlNJ0tLOR3K'

#构建鉴权对象
q = Auth(access_key, secret_key)

#要上传的空间
bucket_name = 'higgs-can-test'

#上传到七牛后保存的文件名
key = "/news/11/123.png";

#生成上传 Token，可以指定过期时间等
token = q.upload_token(bucket_name, key, 3600, policy={'insertOnly':1})
print(token)

#要上传文件的本地路径
localfile = '/home/wangx/Pictures/png.png'

response = requests.post(
    url='http://upload.qiniu.com/',
    data={
        'token': token,
    },
    files = {
        'files': open('/home/wangx/Pictures/123.png','rb')
    },
)
print(response.status_code)
print(response.text)
# ret, info = put_file(token, key, localfile)
# print(ret)
# print(info)
# assert ret['key'] == key
# assert ret['hash'] == etag(localfile)
