#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


from simple_pid import PID
from exponential_counter import LinearCounter


def test_time():
    print("默认情况下，时间是跟着系统时间走的，所以每次都是-200")
    value = -200
    pid = PID(1, 0.1, 0.05)
    for _ in range(3):
        delta = pid(value)
        value = value + delta
        print("增加%f 变成 => %f", delta, value)


def test_time2():
    print("我们提供一个自己的时间函数，每次加1")
    pid = PID(1, 0.1, 0.05, time_fn=LinearCounter())
    value = -200
    for _ in range(3):
        delta = pid(value)
        value = value + delta
        print("增加%f 变成 => %f", delta, value)


test_time()
test_time2()
