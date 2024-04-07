#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


from collections.abc import Callable


def call_int(x: str) -> str:
    return x + '1'


f: Callable[[float], float]

f = call_int
