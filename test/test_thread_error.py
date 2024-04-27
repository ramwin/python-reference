#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import time
from threading import Thread


def f(x):
    if x == 1:
        raise ValueError


def main():
    Thread(None, f, args=[1]).start()
    Thread(None, f, args=[1]).start()
    time.sleep(1)
    print("结束")


main()
