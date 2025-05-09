#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-12-14 19:43:27

from multiprocessing import Pool
import time, os, random


def f(x):
    print(x)
    time.sleep(x)
    print(os.getpid())
    return x*x


def main1():
    with Pool() as p:  # 这个数字代表最多开几个线程
        p.map(f, [6,5,3,4,2,1])  # 这样并不会要n倍时间才能执行, 单倍即可


def main2():
    print(list(map(f, [1,2,3])))  # 这样就要6秒


if __name__ == '__main__':
    start = time.time()
    main1()
    end = time.time()
    print("执行了%0.2f秒" % (end-start))
