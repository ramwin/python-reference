#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2020-03-21 19:04:28


import os
import time

print('Process (%s) start...' % os.getpid())

def f(x):
    if x <=1:
        return 1
    else:
        return f(x-1) + f(x-2)

origin = 36
origin += 1
pid = os.fork()
if pid == 0:
    print("我是子进程: {}, 我的父进程是{}".format(os.getpid(), os.getppid()))
    print("因为我是子进程，所以我fork")
    pid = os.fork()
    if pid == 0:
        print("我是子进程: {}, 我的父进程是{}".format(os.getpid(), os.getppid()))
    else:
        print("我是父进程: {}, 我的父进程是{}".format(os.getpid(), os.getppid()))
else:
    print("我是父进程: {}, 我的父进程是{}".format(os.getpid(), os.getppid()))

origin += 1
print("计算{}".format(origin))
f(origin)
print("我调用{}完毕了: {}".format(origin, os.getpid()))
