#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import logging
import time

from pathlib import Path
from threading import Thread


LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)
LOGGER.addHandler(logging.FileHandler("写日志时重命名文件.log"))
LOGGER.addHandler(logging.StreamHandler())


def task1():
    for i in range(100):
        LOGGER.info(i)
        time.sleep(0.02)


def task2():
    time.sleep(1)
    LOGGER.info("开始重命名")
    Path("写日志时重命名文件.log").rename("写日志时重命名文件.log.1")
    LOGGER.info("重命名了")


def main():
    thread1 = Thread(group=None, target=task1)
    thread2 = Thread(group=None, target=task2)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()
