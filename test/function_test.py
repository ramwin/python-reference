#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2020-03-21 18:08:13


def f(x):
    print("调用f")
    result = x+1
    print(result)
    return result


class M(type(f)):
    pass


