#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import logging


class MyHandler(logging.Handler):

    def handle(self, record):
        print("OK? " + record.msg[0:10])

    def flush(self):
        print("我flush了")

    def close(self):
        print("我close了")


logging.basicConfig(
    handlers=[MyHandler(), logging.StreamHandler()],
    level=logging.INFO
)

logging.error("OK" * 10)
logging.info("OK" * 10)
