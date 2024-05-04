#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import time
from redis import Redis


def test_get():
    r = Redis(decode_responses=True)
    r.set("int", 3)
    start = time.time()
    size = 10000
    for _ in range(size):
        r.get("int")
    end = time.time()
    print("获取", size, "条数据耗时", end-start, "QPS", size / (end-start))


test_get()
