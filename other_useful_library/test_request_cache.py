#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import urllib

from datetime import timedelta
from urllib.parse import urlparse, parse_qs

import requests
from requests import PreparedRequest

import requests_cache


def timekey(request: PreparedRequest, **kwargs):
    return parse_qs(
        urlparse(request.url).query
    )["time"][0]

URL = "http://localhost:8000/sleep/"

def create_key(request: requests.PreparedRequest, **kwargs) -> str:
    return urllib.parse.parse_qs(urllib.parse.urlparse(request.url).query)["page_size"][0]

session = requests_cache.CachedSession(
        'demo_cache',
        backend="filesystem",
        use_cache_dir=False,
        allowable_methds=["GET"],
        key_fn=timekey,
        expire_after=timedelta(seconds=3),
)


def main():
    res = session.get('http://localhost:18000', params={"time": 1}, only_if_cached=True)
    print("请求发送成功")


main()
