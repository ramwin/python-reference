#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
比较各个算法的时间. 同样的 2.33G 文件

blake3: 9.4秒
md5: 10秒
sha245: 12.8秒

但是如果使用命令行
md5sum 4.9秒
b3sum 0.745秒
sha256sum 13.011秒
"""


import logging
from pathlib import Path
import time

from hashlib import md5, sha256
from blake3 import blake3

import logging_config  # pylint: disable=unused-import


FILE = Path("/mnt/s/tmp/极品老妈1080p/Mom.S01E01.Pilot.1080p.AMZN.WEB-DL.DDP5.1.H.264-NTb.mkv")


class NoHash:

    def update(self, data):
        return

    def hexdigest(self):
        return "no hash"


def gettime(f):

    def g(hash_algorithm):
        logging.info("开始运行: %s", hash_algorithm)
        start = time.time()
        f(hash_algorithm)
        duration = time.time() - start
        logging.info("结束运行: %s, 耗时: %f", f, duration)

    return g


@gettime
def test(hash_algorithm):
    hasher = hash_algorithm()
    with open(FILE, "rb") as f:
        for data in f:
            hasher.update(data)
        logging.info("结果: %s", hasher.hexdigest())


def blake3_4_core():
    """
    4核更慢, 需要53秒
    """
    return blake3(max_threads=4)


def main():
    logging.info("第一遍无缓存")
    for hash_algorithm in [
        NoHash, sha256, blake3, md5,
    ]:
        test(hash_algorithm)


main()
