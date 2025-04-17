#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import logging
import os
import time

from pathlib import Path

from multiprocessing import Process
import logging_config


LOGGER = logging.getLogger(__name__)


def clear():
    path = Path("/tmp/fifo")
    path.unlink(True)
    os.mkfifo(path)


def push():
    input_cnt = 10000
    LOGGER.info("开始输入")
    path = Path("/tmp/fifo")
    f = open(path, "w")
    # with open(path, "w") as f:
    if True:
        for i in range(input_cnt):
            f.write(str(i) + "\n")
            f.flush()
            LOGGER.info("输入: %d", i)
            time.sleep(0.0001)
    f.close()
    LOGGER.info("输入结束")


def pull():
    """测试分2次读取应该中间缺少了python一次读1024字节的缓存"""
    LOGGER.info("开始输出")
    path = Path("/tmp/fifo")
    pre = 0
    with open(path) as f:
        for index, line in enumerate(f):
            LOGGER.info("读到了: %s", line)
            if int(line) - pre > 2:
                LOGGER.error("上次读 %d 这次直接变成 %s了", pre, line)
            pre = int(line)
    LOGGER.info("第一次输出结束")


def test_multi_pull():
    pull1 = Process(target=pull)
    pull2 = Process(target=pull)
    pull1.start()
    pull2.start()
    pull1.join()
    pull2.join()


if __name__ == "__main__":
    clear()
    push_process = Process(target=push)
    pull_process = Process(target=test_multi_pull)
    push_process.start()
    pull_process.start()
    push_process.join()
    pull_process.join()
