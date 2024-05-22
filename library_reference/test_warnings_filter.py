#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import warnings


warnings.filterwarnings("error", category=DeprecationWarning)


def f():
    warnings.warn(DeprecationWarning("不要用我了"))


if __name__ == "__main__":
    print("普通调用时只有一个warning")
    print("严格调用时直接raise")
    f()
    print("调用结束")
