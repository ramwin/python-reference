#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
a+=1: ops: %f 31236671.01098492
time.time: ops: %f 12999990.701682067
redis.get: %f 20952.91381253447
"""


import time
import uuid

import redis


def test_add():
    # 三千万 QPS
    start = time.time()
    size = 1_000_000
    a = 0
    for _ in range(size):
        a += 1
    print("a+=1: ops: %f", size / (time.time() - start))


def test_time():
    # 一千万 QPS
    size = 1_000_000
    start = time.time()
    for _ in range(size):
        a = time.time()
    print("time.time: ops: %f", size / (time.time() - start))


def test_redis():
    # 18K QPS
    c = redis.Redis()
    size = 10_000
    start = time.time()
    for _ in range(size):
        c.get("foo")
    print("redis.get: %f", size / (time.time() - start))


def test_uuid():
    # 30万 QPS
    size = 10_000
    start = time.time()
    for _ in range(size):
        a = uuid.uuid4()
    print("uuid: %f", size / (time.time() - start))


test_add()
test_time()
test_redis()
test_uuid()
