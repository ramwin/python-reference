#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import multiprocessing
import os
import time

from contextvars import ContextVar


var = ContextVar("var", default=False)


def f(x):
    time.sleep(x * 0.01)
    if var.get() is False:
        var.set(True)
        print("第一次遇到进程", os.getpid())
    print(os.getpid(), "处理", x)


def main():
    with multiprocessing.Pool(4) as p:
        p.map(f, range(10))


if __name__ == "__main__":
    main()
