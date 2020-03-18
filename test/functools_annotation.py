#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2020-03-18 13:12:43


def f(a: int, b: str = 'default') -> int:
    print("调用f")
    print(type(a))
    if b == 'default':
        return a* a
    else:
        return '123'


print(f(2))
print(f("2", 'nothing'))
