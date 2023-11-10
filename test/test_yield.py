#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2020-03-21 23:10:43


def gen():
    print("call gen")
    n = yield 1
    print("n: {}".format(n))
    print("call gen after 1")
    n = yield 2
    print("n: {}".format(n))
    print("call gen after 2")
    n = yield 3
    return 4, gen

def test1():
    a = gen()
    print("next: {}".format(next(a)))
    print("before send 1")
    result = a.send(1)
    print("result: {}".format(result))
    print("after send 1")
    print("next: {}".format(next(a)))
    print("end")
    print("return的值是通过StopIteration返回的")
    try:
        print("next: {}".format(next(a)))
    except StopIteration as error:
        print(error.args)
        print(next(error.args[0][1]()))

test1()
