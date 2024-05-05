#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import functools
import time


@functools.cache
def f(x):
    print("调用f", x)
    time.sleep(x)
    return x + 1


print(f(1))
print(f(1.0))
print(f(0.5))
