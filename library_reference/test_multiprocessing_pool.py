#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


from multiprocessing import Pool
import time


def f(x):
    print("处理", x)
    time.sleep((100 - x) / 100)
    print("处理完成", x)

def test1():
    """imap_unordered必须被用了才执行"""
    with Pool() as p:
        for i in p.imap_unordered(f, range(100)):
            print(i)


def test2():
    """imap提前返回"""
    start = time.time()
    with Pool(8) as p:
        for i in p.imap_unordered(f, range(100)):
            if time.time() - start > 0.1:
                p.terminate()


test2()
