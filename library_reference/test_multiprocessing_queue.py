#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import time

from multiprocessing import Process, Queue
from multiprocessing.queues import Empty


N = 100_000

def product(q):
    for i in range(N):
        q.put([i, None, "Hello"])


def consumer(qs):
    n = 0
    while True:
        try:
            a = qs.get(timeout=0.1)
            n += 1
        except Empty:
            print("没有数据了", n)
            return


def main():
    start = time.time()
    q = Queue()
    p1 = Process(target=product, args=[q])
    p1.start()
    p2 = Process(target=consumer, args=[q])
    p2.start()
    p1.join()
    p2.join()
    end = time.time()
    print("多进程的queue速度:", N // (end - start))


if __name__ == "__main__":
    main()
