#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-09-29 20:20:02


def echo(value=None):
    print("开始喊话")
    try:
        while True:
            try:
                value = (yield value)
            except Exception as e:
                print(e)
                value = e
    finally:
        print("Don't forget to clean up whe 'close()' is called")
generator = echo(1)
print(next(generator))  # 1
print(next(generator))  # None
print(generator.send(2))
print(next(generator))
generator.throw(TypeError, "spam")
generator.close()
