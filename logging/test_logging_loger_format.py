#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import logging

stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler("info.log", mode="a")

logging.captureWarnings(True)
logging.basicConfig(
    level=logging.INFO,
    format=(
        '[%(levelname)s] %(asctime)s [%(pathname)s:%(lineno)d] %(message)s'
    ),
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        stream_handler,
        file_handler,
    ],
)

logging.root.addHandler(
    logging.StreamHandler(
    ),
)
logging.info("后来添加的handler没有formatter")
