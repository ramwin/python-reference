#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import time


class TimeOut:

    def __init__(self, timeout: float):
        self.timeout = timeout
        self.end = self.start = time.time()

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, *args, **kwargs):
        self.end = time.time()
        if self.end > self.start + self.timeout:
            raise ValueError("函数超时了", self.end - self.start)


if __name__ == "__main__":
    with TimeOut(1):
        print(1)
    with TimeOut(2):
        time.sleep(2)
        print(2)
