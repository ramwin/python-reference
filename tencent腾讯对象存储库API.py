#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-09-03 20:20:31

import requests


BUCKET_NAME = "ramwinstore"
APP_ID = "10064283"
HOST = "http://ramwinstore-10064283.file.myqcloud.com/"
SECRET_ID = "AKIDVt9Xm2JTsPlUjDGAOuGd4Z5lRlVedbUQ"
SECRET_KEY = "DLX9okBvhE21HnhCwZcdhCYWcbtT6HUW"

# 上传文件
file_name = "test.jpg"
url = HOST + "files/v1/" + APP_ID + "/" + BUCKET_NAME + "/" + file_name
headers = {
    "Content-Type": "multipart/form-data"
}
data = {
    "op": "upload",
    "filecontent": "",
    "sha": "",
    "biz_attr": "test",
    "insertOnly": "1",
}

response = requests.post(
    url=url, headers=headers, data=data
)

print(response.text)
print(response.status_code)
