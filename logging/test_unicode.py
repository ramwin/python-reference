#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-07-22 15:42:09


import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="./test.log",
    filemode="a",
)


logging.info('123')
logging.info({u'姓名', u'王祥'})
