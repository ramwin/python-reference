#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import time

from redis import Redis


c = Redis()


def test_is_member_vs_local():
    prefix = "very_long" * 3
    key = "SET"
    c.delete(key)
    for i in range(10):
        c.sadd(key, f"{prefix}_{i}")
    start = time.time()
    for i in range(0, 1000):
        c.sismember(key, f"{prefix}_{i % 20}")
    end = time.time()
    print("使用redis耗时: %f", end-start)

    localset = c.smembers(key)
    start = time.time()
    for i in range(0, 1000):
        f"{prefix}_{i % 20}" in localset
    end = time.time()
    print("使用本地耗时: %f", end-start)


test_is_member_vs_local()
