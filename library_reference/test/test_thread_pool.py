#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import random
import time
from multiprocessing.pool import ThreadPool


def f(x):
    print("开始执行", x)
    time.sleep(random.random())
    if x % 4 == 0:
        print("准备报错")
        raise ValueError("不吉利")
    print("执行完毕", x)
    return x + 1


def main():
    print("开始使用ThreadPool")
    print("不报错的情况下")
    tasks = range(1, 4)
    with ThreadPool() as p:
        results = p.map(f, tasks)
    print("可以拿到结果:", results)
    print("如果有报错的情况，就拿不到结果了")
    tasks = range(7)
    with ThreadPool() as p:
        results = p.map(f, tasks)
    print("结束")
    print(results)


main()
