#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-12-31 14:50:46


import time


def custom_time_decorator(timeout=1):
    def time_decorator(func):
        def fin(*args, **kwargs):
            starttime = time.time()
            result = func(*args, **kwargs)
            endtime = time.time()
            if endtime - starttime >= timeout:
                print("您超时了哦")
            return result
        return fin
    return time_decorator


@custom_time_decorator(1)
def fast():
    print("我跑得飞快")
    return 1


@custom_time_decorator(1)
def slow():
    time.sleep(1.1)
    print("我走得贼慢")
    return 2


@custom_time_decorator(timeout=2)
def slow2():
    time.sleep(1.1)
    print("虽然我走得贼慢，但是仍然快于2秒哦")
    return 2


@custom_time_decorator(timeout=2)
def slow3():
    time.sleep(2.1)
    print("我不行了，2s都不行")
    return 2


if __name__ == "__main__":
    fast()
    slow()
    slow2()
    slow3()
