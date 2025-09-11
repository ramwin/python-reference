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

def f2(x):
    print("处理", x)
    time.sleep(x / 10)
    print("处理完毕", x)
    return x

def test3():
    """
    imap是否固定顺序返回: 是的
    能否利用好多进程: 是的,返回数据处理慢了多进程也会继续执行下一个
    """

    with Pool(3) as p:
        for result in p.imap(f2, range(6)):
            print("  返回数据", result)
            time.sleep(0.4)
            print("  返回数据完毕", result)


def test2():
    """imap提前返回"""
    start = time.time()
    with Pool(8) as p:
        for i in p.imap_unordered(f, range(100)):
            if time.time() - start > 0.1:
                p.terminate()


test3()
