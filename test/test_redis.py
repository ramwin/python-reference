#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-05-06 17:11:40


import redis
import time
import unittest


r = redis.StrictRedis(decode_responses=True)


class Cache(object):

    def sadd(sef):
        for i in range(97, 107):
            r.zadd("sorted_set", {chr(i): 100-i})

    def iterate(self):
        for i in r.zrange("sorted_set", 0, -1):
            yield i


class RedisTest(unittest.TestCase):

    def test_sorted_set(self):
        print("测试 sorted set 变化")
        cache = Cache()
        cache.sadd()
        for item in cache.iterate():
            r.zrem("sorted_set", "e")
            print(item)


class LockTest(unittest.TestCase):

    def test_lock(self):
        print("测试lock的变化")
        with r.lock("123") as lock:
            print("开始倒计时{}".format(lock))
            time.sleep(5)
            print("lock结束")


if __name__ == "__main__":
    unittest.main()
