#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"测试pylint的报错"


import requests


print(requests.get("https://baidu.com"))


f = open("info.log", encoding="utf8")
f.read()
