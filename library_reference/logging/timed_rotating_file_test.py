#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-04-29 11:10:12

import logging
import datetime
from logging.handlers import TimedRotatingFileHandler
import time


logging.basicConfig(
    format="%(asctime)s %(message)s",
    datefmt="%H:%M:%S"
)
file_handler1 = TimedRotatingFileHandler(
    filename="timelogger.log",
    interval=1,
    backupCount=5,
    when="midnight",
    atTime=datetime.time(0, 0, 0),
)
file_handler1.setFormatter(logging.Formatter(fmt="%(asctime)s %(message)s"))

log = logging.getLogger()
log.addHandler(file_handler1)


if __name__ == '__main__':
    for i in range(80):
        time.sleep(1)
        log.warning("warning")
