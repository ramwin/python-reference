#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-12-14 19:52:21


from multiprocessing import Process
import random
import time
import os


class A(object):
    def __init__(self, name):
        self.name = name

    def add(self):
        self.name += self.name

    def __str__(self):
        self.name += self.name
        return self.name


def f(name):
    sleep = random.random()*3
    sleep = 2
    time.sleep(sleep)
    print(f"id: {id(name)}")
    print("after %0.2f秒" % sleep)
    print("hello", name)
    name.add()
    print(name)
    print(f"id: {id(name)}")
    print("module name:", __name__)
    print("parent process:", os.getppid())
    print("process id:", os.getpid())


a = A('a')
if __name__ == '__main__':
    p = Process(target=f, args=(a, ))
    p.start()
    p1 = Process(target=f, args=(a, ))
    p1.start()
    # p.join()
    # p1.join()
