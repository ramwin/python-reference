#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
对于一个文件, 如果是一个字节一个字节的复制, 速度
如果直接copy, 66M/s
"""


import random
import shutil
import time
from pathlib import Path


root = Path("/mnt/f/电视剧/三体")
target = Path("/mnt/e/大文件")
files = list(root.iterdir())


def test1():
    """
    对文件对象进行for循环, 其实是528字节一个迭代
    """
    path = random.choice(files)
    print("开始读取文件")
    start = time.time()
    with open(target, "wb") as out:
        with open(path, "rb") as f:
            for data in f:
                out.write(data)

    duration = time.time() - start
    size = path.stat().st_size
    print(f"按照每个字节读取 {size=} 个字节, 耗时: {duration}, 速度: {size / duration / 1024 / 1024} M/s")


def test2():
    path = random.choice(files)
    start = time.time()
    shutil.copyfile(path, target)
    duration = time.time() - start
    size = path.stat().st_size
    print(f"复制 {size=} 个字节, 耗时: {duration}, 速度: {size / duration / 1024 / 1024} M/s")


test1()
test2()
