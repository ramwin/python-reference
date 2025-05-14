#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time


def test_set_speed(step):
    a = set(range(step))
    b = list(range(step // 2, step * 3 // 2))
    start = time.time()
    c = [
            i
            for i in b
            if i in a
    ]
    end = time.time()
    print("set: QPS", step / (end - start))


def test_list_speed(step):
    a = list(range(step))
    b = list(range(step // 2, step * 3 // 2))
    start = time.time()
    c = [
            i
            for i in b
            if i in a
    ]
    end = time.time()
    print("list: QPS", step / (end - start))


def test_list_set():
    """
    结论, 5个以内无所谓, 5个以上用set
    step    set     list
    3       1.2M    2.5M
    4       2.7M    2.7M
    5       4.2M    4.2M
    10      6.0M    4.2M
    20      9.3M    5.5M
    30      13M     3M
    100     24M     2M
    1000    32M     238K
    10000   36M     23K
    """
    step = 4
    test_list_speed(step)
    test_set_speed(step)


test_list_set()
