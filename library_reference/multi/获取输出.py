#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import queue
from multiprocessing import Process, Queue
import time


def f(conn, arg):
    time.sleep(1)
    conn.put(arg**2)
    return


def main():
    q = Queue()
    p = Process(target=f, args=(q, 45))
    p.start()
    try:
        print(q.get(timeout=0.1))
    except queue.Empty:
        print("没有数据")
    print(q.get(timeout=1))


if __name__ == "__main__":
    main()
