#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
a+=1: ops: %f 31236671.01098492
time.time: ops: %f 12999990.701682067
redis.get: %f 20952.91381253447
"""


import redis
import time


def test_add():
    start = time.time()
    size = 1_000_000
    a = 0
    for i in range(size):
        a += 1
    print("a+=1: ops: %f", size / (time.time() - start))


def test_time():
    size = 1_000_000
    start = time.time()
    for i in range(size):
        a = time.time()
    print("time.time: ops: %f", size / (time.time() - start))


def test_redis():
    c = redis.Redis()
    size = 10_000
    start = time.time()
    for i in range(size):
        c.get("foo")
    print("redis.get: %f", size / (time.time() - start))


test_add()
test_time()
test_redis()
