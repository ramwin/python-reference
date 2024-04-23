#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


from urllib.parse import urlparse, parse_qs
from requests import PreparedRequest

import requests_cache


def timekey(request: PreparedRequest, **kwargs):
    return parse_qs(
        urlparse(request.url).query
    )["time"][0]


session = requests_cache.CachedSession(
        'demo_cache',
        backend="filesystem",
        use_cache_dir=False,
        allowable_methds=["GET"],
        key_fn=timekey,
)


def main():
    res = session.get('http://localhost:18000', params={"time": 1})
    print("请求发送成功")


main()
