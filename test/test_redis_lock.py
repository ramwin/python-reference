#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
测试lock的时候，其他进程lock了怎么办
"""


import time
from multiprocessing import Process

from redis import Redis
from redis.exceptions import LockError


REDIS = Redis("localhost")


def process1():
    print("进程1开始")
    with REDIS.lock("lock"):
        print("进程1拿到了锁")
        time.sleep(5)
        print("进程1结束")


def process2():
    print("进程2开始")
    try:
        with REDIS.lock("lock", blocking=False):
            print("进程2拿到了锁")
            time.sleep(5)
            print("进程2结束")
    except LockError as error:
        print("进程2拿不到锁")


if __name__ == "__main__":
    p1 = Process(target=process1)
    p2 = Process(target=process2)
    p1.start()
    p2.start()
