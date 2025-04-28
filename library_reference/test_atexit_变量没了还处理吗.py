#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import atexit
import psutil


class A:

    def echo(self):
        return
        print("我是A")

    def __del__(self):
        atexit.unregister(self.echo)


def f():
    for i in range(100000):
        a = A()
        atexit.register(a.echo)
        atexit.unregister(a.echo)
    print("F end")


def main():
    process = psutil.Process()
    print("占用内存(GB):", process.memory_info().rss / 1024 ** 3)
    f()
    print("占用内存(GB):", process.memory_info().rss / 1024 ** 3)


if __name__ == "__main__":
    main()
