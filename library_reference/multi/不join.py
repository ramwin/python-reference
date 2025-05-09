#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


from multiprocessing import Process
import time


def f():
    time.sleep(12)


def start_back():
    p = Process(target=f)
    p.start()


def main():
    start_back()
    print("结束")


if __name__ == "__main__":
    main()
