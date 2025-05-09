#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2020-03-21 19:44:03


import os
import threading


def f(x):
    if x <=1:
        return 1
    else:
        return f(x-1) + f(x-2)


def cal(x):
    print("计算{}的费波那契数列, pid: {}".format(x, os.getpid()))
    result = f(x)
    print("结果是: {}".format(result))


for i in range(2):
    threading.Thread(target=cal, args=(37, )).start()
print("结束")
