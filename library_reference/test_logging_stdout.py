#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import logging
import sys


def test1():
    logging.basicConfig(handlers=[logging.StreamHandler()], level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info("默认情况下, streamhandler是到stderr的 所以2>/dev/null就没有")


def test2():
    logging.basicConfig(handlers=[logging.StreamHandler()], level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info("通过指定streamhandler的stream可以把stderr变成stdout, 但是执行两次basicConfig, 只有第一次生效")
    logger.info("先执行test2, 那都是stdout, 先执行test1, 那都是stderr")
    logger.error("报错")


def test3():
    logging.basicConfig(handlers=[logging.StreamHandler(sys.stdout)], level=logging.INFO, format="%(message)s")
    logger = logging.getLogger(__name__)
    logger.info("如何能快速指导logger的是stdout还是stderr")


if __name__ == "__main__":
    # test1()
    test2()
    # test3()
