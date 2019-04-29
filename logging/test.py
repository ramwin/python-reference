#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-04-29 11:10:12

import logging
from logging.handlers import TimedRotatingFileHandler
import time


logging.basicConfig(
    format="%(asctime)s %(message)s",
    datefmt="%H:%M:%S"
)
file_handler1 = TimedRotatingFileHandler(
    filename="logger.log",
    backupCount=5,
    when="M",
)
file_handler1.setFormatter(logging.Formatter(fmt="%(asctime)s %(message)s"))

log = logging.getLogger()
log.addHandler(file_handler1)


for i in range(80):
    time.sleep(1)
    log.warning("warning")
