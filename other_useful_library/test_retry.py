#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import logging
import time
from retry import retry


start = time.time()


@retry(delay=0.1, logger=logging.getLogger(__name__))
def run():
    if time.time() - start >= 0.1:
        print("OK")
        return True
    print("FAIL")
    raise ValueError("请等等")


run()
