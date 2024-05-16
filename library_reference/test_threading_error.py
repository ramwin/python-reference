#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import time
from multiprocessing.pool import ThreadPool

from logging_config import logging


LOGGER = logging.getLogger(__name__)


def f(x):
    if x == 2:
        raise ValueError("特殊的质数")
    time.sleep(0.1*x)
    LOGGER.info("%d 执行结束", x)
    return x**x


def test_block():
    LOGGER.info("测试ThreadPool, 他会报错，所以后面的日志(后面的日志)不会打印出来")
    LOGGER.info("但是不影响其他线程")
    tasks = range(1, 4)
    with ThreadPool() as p:
        p.map(f, tasks)

    LOGGER.info("后面的日志")


test_block()
