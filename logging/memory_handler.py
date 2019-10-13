#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-07-03 10:38:10


import six
import logging
from logging import handlers


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - line: %(lineno)s %(message)s')
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - line: %(lineno)s %(message)s',
)

def basic():  # 基础用法
    log = logging.getLogger(__name__)
    stream_handler = logging.StreamHandler()

    # 写入5个后才会记录。并且close的时候会记录
    memory_handler1 = handlers.MemoryHandler(5, target=stream_handler)
    memory_handler1.setLevel(logging.INFO)

    log.addHandler(memory_handler1)

    for i in range(13):
        log.info(i)


def noflush():  # close的时候不记录
    log = logging.getLogger(__name__)
    stream_handler = logging.StreamHandler()

    # 写入5个后才会记录。并且close的时候会记录
    if six.PY3:
        memory_handler1 = handlers.MemoryHandler(100,
            target=stream_handler,
            flushOnClose=False)
    else:
        memory_handler1 = handlers.MemoryHandler(100,
            target=stream_handler)
    memory_handler1.setLevel(logging.INFO)

    log.addHandler(memory_handler1)

    for i in range(13):
        log.info(i)
    # log.handlers[0].close()  # 调用close直接关闭可以避免记录最后的数据
    # log.removeHandler(memory_handler1)  # 直接remove，会导致没有flush
    if i == 13:  # 如果最后一个数字是13, 恭喜，请求处理完毕，什么日志都不用记录
        log.removeHandler(memory_handler1)
    else:
        pass


if __name__ == '__main__':
    noflush()
