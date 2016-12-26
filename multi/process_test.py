#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-12-14 19:52:21


from multiprocessing import Process
import random, time, os


def f(name):
    sleep = random.random()*3
    sleep = 2
    time.sleep(sleep)
    print("after %0.2f秒" % sleep)
    print("hello", name)
    print("module name:", __name__)
    print("parent process:", os.getppid())
    print("process id:", os.getpid())


if __name__ == '__main__':
    p = Process(target=f, args=('bob', ))
    p.start()
    p1 = Process(target=f, args=('bob1', ))
    p1.start()
    p.join()
    p1.join()
