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

def test1():
    a = gen()
    print("next: {}".format(next(a)))
    print("before send 1")
    result = a.send(1)
    print("result: {}".format(result))
    print("after send 1")
    print("next: {}".format(next(a)))
    print("end")

test1()
