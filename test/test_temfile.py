"""
测试tempfile
"""

import tempfile
import time

import psutil


def test1():
    """比较SpooledTemporaryFile和TemporaryFile的速度"""
    text = b"i" * 1024
    start = time.time()
    memory = psutil.virtual_memory().free
    with tempfile.SpooledTemporaryFile(max_size=1024 * 1024 * 1024) as spool:
        for _ in range(1024 * 1024):
            spool.write(text)
        print(f"Spooled写入1G: {time.time() - start}")
        print("使用内存")
        print((memory - psutil.virtual_memory().free) / 1024**3)

    start = time.time()
    memory = psutil.virtual_memory().free
    with tempfile.TemporaryFile() as temp:
        for _ in range(1024 * 1024):
            temp.write(text)
        print(f"temp写入1G: {time.time() - start}")
        print((memory - psutil.virtual_memory().free) / 1024**3)


test1()
