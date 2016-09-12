#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-09-11 23:38:03

import heapq
import time

def push_big(n):
    result = []
    for i in range(0, n):
        # result.insert(len(result), i) # 1.54秒
        heapq.heappush(result, i)   # 1.14秒


def push_small(n):
    result = []
    for i in range(n-1, -1, -1):
        # result.insert(0, i)  # 很久
        heapq.heappush(result, i)  # 3.54秒


def main(n):
    print("正在生成节点为 %d 的堆结构" % n)
    start = time.time()
    push_big(n)
    end = time.time()
    print("每次push大数字的时间需要 %0.2f 秒" % (end-start) )

    start = time.time()
    push_small(n)
    end = time.time()
    print("每次push小数字的时间需要 %0.2f 秒" % (end-start) )


main(10000000)
