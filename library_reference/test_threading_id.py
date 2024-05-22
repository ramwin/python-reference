#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import threading


def f():
    print(threading.get_native_id())


def test():
    """测试线程ID"""
    f()
    new_thread = threading.Thread(target=f).start()


test()
