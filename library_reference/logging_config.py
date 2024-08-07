#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>

import logging

import colorlog


handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    "%(log_color)s%(levelname)s:%(name)s:%(message)s"
    ))
file_handler = logging.FileHandler("info.log")
logging.basicConfig(level=logging.INFO, handlers=[handler, file_handler])

logger = logging.getLogger(__name__)
logger.info("引入日志模块")
