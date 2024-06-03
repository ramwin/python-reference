#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


def test(i):
    n = 0
    while n < i:
        # if n == 2:
        #     raise StopIteration  # 这个会报错
        if n == 3:
            return  # return 可以提前退出
        n += 1
        yield n * n
    print("结束")


print(list(test(10)))
