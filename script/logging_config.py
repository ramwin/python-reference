#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(pathname)s[line:%(lineno)d] %(levelname)s %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("info.log"),
    ]
)
