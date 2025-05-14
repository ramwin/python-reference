#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import logging


def i_will_raise():
    raise ValueError('value报错')


def wrapper_level1():
    try:
        i_will_raise()
    except Exception as error:
        logging.error("wrapper: start")
        logging.exception(error)
        logging.error("wrapper: end")
        raise Exception(123)

def call_wrapper_level1():
    try:
        wrapper_level1()
    except Exception as error:
        logging.error("外部封装")
        logging.exception(error)

    
def i_will_ignore_ValueError():
    try:
        i_will_raise()
    except Exception as error:
        logging.error("=============== ignore的日志:start =================")
        logging.exception(error)
        logging.error("=============== ignore的日志:ended =================")
        raise error from error


def simple():
    """
    最简单的方式, 直接显示错误和traceback

    ERROR:root:=============== main的日志:start =================
    ERROR:root:value报错
    Traceback (most recent call last):
      File "/home/wangx/github/python-reference/test/test_exception.py", line 25, in simple
        i_will_raise()
      File "/home/wangx/github/python-reference/test/test_exception.py", line 10, in i_will_raise
        raise ValueError('value报错')
    ValueError: value报错
    ERROR:root:=============== main的日志:ended =================
    """
    try:
        i_will_raise()
    except Exception as error:
        logging.error("=============== main的日志:start =================")
        logging.exception(error)
        logging.error("=============== main的日志:ended =================")



simple()
print("封装一层")
call_wrapper_level1()
