#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-08-19 11:00:43

import json
def testexcept():
    try:
        1/0
    except Exception as e:
        print("zero")


    try:
        json.loads("ew")
    except ZeroDivisionError:  # 遇到指定错误处理
        print("zero")
    except:  # 处理所有的错误
        print("except")
    finally:  # 无论是否有错误，都触发
        print("done")

    try:
        1+1
    except NameError:
        print("nameerror")
    else:  # 如果没有报错就进行else
        print(1)


import traceback
def testexcept():
    try:
        1/0
    except Exception as e:
        a = e
