#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>

from multiprocessing import Pool
import time
import random
import os


a = list(range(10))


def f(x):
    time.sleep(random.random() / 100)
    print(f"{x}的pid = {os.getpid()}")
    return [x, x ** 2]


def main():
    results = []
    with Pool() as p:
        for x in p.imap_unordered(f, a, 3):
            results.append(x)
    print(results)


main()
