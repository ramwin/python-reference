#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import logging
import test_colorlog

from redis import Redis


LOGGER = logging.getLogger(__name__)


def main():
    pipe = Redis(decode_responses=True).pipeline()
    pipe.delete("dict")  # 1
    pipe.hset("dict", "k", "1.5")  # 1
    pipe.hset("dict", "k", "2")  # 0
    pipe.hset("dict", "k2", "3")  # 1
    pipe.hset("dict", "k1", "4")  # 1
    pipe.expire("dict", 3600)  # True
    pipe.hvals("dict")  #  ['2', '3', '4']
    LOGGER.info(pipe.execute())


if __name__ == "__main__":
    main()
