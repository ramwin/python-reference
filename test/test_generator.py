#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2020-03-21 22:55:27


def f():
    for i in range(100):
        yield i


for a in f():
    print(a)
