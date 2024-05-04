#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import time
from redis import Redis


def test_get():
    key = "some_very_long_intger_key_for_python" * 20
    r = Redis(decode_responses=True)
    r.set(key, 3)
    start = time.time()
    size = 10000
    for _ in range(size):
        r.get(key)
    end = time.time()
    print("key的长度为", len(key))
    print("获取", size, "条数据耗时", end-start, "QPS", size / (end-start))


test_get()
