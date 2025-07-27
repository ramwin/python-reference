#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time

from pathlib import Path


def main():
    path = Path("test.log")
    start = time.time()
    with open(path, "w") as f:
        for i in range(10_000_000):
            f.write(str(i))
    end = time.time()
    speed = path.stat().st_size / 1024 / 1024 / (end - start)
    print("在", path.absolute(), "写的读写速度为", round(speed, 2))


if __name__ == "__main__":
    main()
