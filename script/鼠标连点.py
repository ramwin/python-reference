#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import time
from PyWinMouse import Mouse


def main():
    m = Mouse()
    cnt = input("输入执行次数(50): ")
    if not cnt:
        cnt = 50
    else:
        cnt = int(cnt)
    for _ in range(cnt):
        time.sleep(0.2)
        m.left_click()


if __name__ == "__main__":
    main()
