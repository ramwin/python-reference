#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import traceback

import logging


class IndentFormat(logging.Formatter):
    DEFAULT_INDENT = 10

    def format(self, *args, **kwargs):
        return "    " * max(
                len(traceback.extract_stack()) - self.DEFAULT_INDENT,
                0,
        ) + super().format(*args, **kwargs)


stream_handler = logging.StreamHandler()
stream_handler.setFormatter(IndentFormat())
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)
LOGGER.addHandler(stream_handler)


def f():
    LOGGER.info("执行f")


def main():
    LOGGER.info("执行Main")
    f()
    LOGGER.info("执行结束")


main()
