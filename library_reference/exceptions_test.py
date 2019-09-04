#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-09-03 18:12:47


import warnings


def test_warning():
    warnings.warn("deprecated", DeprecationWarning)
    # with warnings.catch_warnings(record=True) as w:
    #     raise DeprecationWarning("这个函数不能被调用哦")


if __name__ == "__main__":
    test_warning()
    print("执行完毕")
