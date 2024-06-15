#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import time
from queue import Queue


def test():
    start = time.time()
    q = Queue()
    for i in range(1000):
        for i in range(1000):
            q.put(i)
        for i in range(1000):
            q.get()
    end = time.time()
    print("速度: 大约400K/s", 1000* 1000 / (end-start))


test()
