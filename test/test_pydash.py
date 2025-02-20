#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import time
import pydash
import atexit


def test_get():
    """
    测试有key但是为None
    """
    print(__doc__)

    class A:
        pass

    a = A
    a.foo = {"key": {}, "bar": None}
    print("空字典: ", pydash.get(a, "foo.key", 1))
    print("不存在: ", pydash.get(a, "foo.nokey", 1))
    print("None: ", pydash.get(a, "foo.bar", 1))


def wait(x):
    print("call wait")
    print(x)
    print("wait end")


def test_debounse():
    new_wait = pydash.functions.debounce(wait, wait=1000)
    atexit.register(wait, 1)
    print("第1遍")
    new_wait(0)
    print("第2遍")
    new_wait(1)
    print("第3遍")
    new_wait(2)
    print("第4遍")
    new_wait(3)


test_debounse()
