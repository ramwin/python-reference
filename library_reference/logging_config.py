#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>

import logging

import colorlog


handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    "%(log_color)s %(process)d %(levelname)s:%(name)s:%(message)s"
    ))
file_handler = logging.FileHandler("info.log", mode="w")
file_handler.setFormatter(logging.Formatter(
     '%(asctime)s [%(module)s:%(lineno)d] %(levelname)s %(message)s'
    ))
logging.basicConfig(level=logging.INFO, handlers=[handler, file_handler])

logger = logging.getLogger(__name__)
logger.info("引入日志模块")
