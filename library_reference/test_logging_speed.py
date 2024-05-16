#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
INFO:logging_config:引入日志模块
INFO:__main__:开始运行: test_format_logging
INFO:__main__:结束运行: test_format_logging
INFO:__main__:总耗时: 0.000000, 2014934
INFO:__main__:开始运行: test_logging_with_parameter
INFO:__main__:结束运行: test_logging_with_parameter
INFO:__main__:总耗时: 0.000000, 3206824
"""


import logging
import time

from functools import update_wrapper

import logging_config


LOGGER = logging.getLogger(__name__)


def monitor(f):
    def fin(*args, **kwargs):
        LOGGER.info("开始运行: %s", f.__name__)
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        LOGGER.info("结束运行: %s", f.__name__)
        LOGGER.info("总耗时: %f, %d", round(end - start, 2), int(result / (end - start)))
        return result
    return update_wrapper(fin, f)


@monitor
def test_format_logging():
    for i in range(10000):
        LOGGER.debug(f"一般的日志大概都会有十几个到二十个字: {i}")
    return i


@monitor
def test_logging_with_parameter():
    for i in range(10000):
        LOGGER.debug("一般的日志大概都会有十几个到二十个字: %d", i)
    return i


if __name__ == "__main__":
    test_format_logging()
    test_logging_with_parameter()
