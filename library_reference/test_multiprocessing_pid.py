#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
from contextvars import ContextVar
from multiprocessing import Pool, parent_process


pid = ContextVar("pid", default=0)
pid.set(os.getpid())


def f(i):
    if os.getpid() != pid.get():
        print("是子进程")
        print(parent_process().name)
    else:
        print("不是子进程")


def main():
    print(parent_process())
    f(12)
    with Pool() as p:
        p.map(f, range(20))


main()
