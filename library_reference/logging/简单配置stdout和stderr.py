#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import logging
import sys


stdout = logging.StreamHandler(stream=sys.stdout)
stdout.setLevel(logging.INFO)
stderr = logging.StreamHandler(stream=sys.stderr)
stderr.setLevel(logging.ERROR)
stdout.setFormatter(logging.Formatter(
     '%(asctime)s [%(module)s:%(lineno)d] %(levelname)s %(message)s'
    ))
stderr.setFormatter(logging.Formatter(
     '%(asctime)s [%(module)s:%(lineno)d] %(levelname)s %(message)s'
    ))
logging.basicConfig(
        level=logging.INFO,
        handlers=[stdout, stderr],
)


LOGGER = logging.getLogger(__name__)


def main():
    LOGGER.info("info")
    LOGGER.warning("warning")
    LOGGER.error("error")
    raise ValueError(123)


if __name__ == "__main__":
    main()
