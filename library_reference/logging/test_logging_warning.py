#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import warnings
import logging


logging.captureWarnings(True)
logging.basicConfig(
    filename="tmp.log"
)
warnings.warn("123")
