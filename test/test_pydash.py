#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import pydash


def test1():
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


test1()
