#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import time
from PyWinMouse import PyMouse


def main():
    m = PyMouse()
    for i in range(200):
        time.sleep(0.2)
        m.left_click()


if __name__ == "__main__":
    main()
