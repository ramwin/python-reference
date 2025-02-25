#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
大概1秒7张.
"""


import time

from pyautogui import screenshot


def main():
    start = time.time()
    index = 0
    while time.time() - start <= 10:
        index += 1
        img = screenshot(region=(0,0, 2300, 1400))
        # img.save(f"tmp/{index}.png")
        print(f"截屏{index}次")


if __name__ == "__main__":
    main()
