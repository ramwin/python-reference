#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
注意, cache.memoize 无法保留原来的typehint
"""


import logging
import time
from cacheout import Cache
import logging_config


cache = Cache(ttl=1)
LOGGER = logging.getLogger(__name__)


@cache.memoize()
def slow(x: int) -> str:
    LOGGER.info("调用: %d", x)
    return str(x)


def main() -> None:
    LOGGER.info("show(1): ")
    LOGGER.info(slow(1))
    time.sleep(0.3)
    LOGGER.info("show(2): ")
    LOGGER.info(slow(2))
    time.sleep(0.7)
    LOGGER.info("show(1): ")
    LOGGER.info(slow(1))
    LOGGER.info("show(2): ")
    LOGGER.info(slow('2'))


if __name__ == "__main__":
    main()
