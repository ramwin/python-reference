#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
定时截图, 方便后期找错题
"""


import datetime
from pathlib import Path
import time

from pyautogui import screenshot


DIRECTORY = Path("D:/定时截图")
TIMEOUT = 3600 * 2  # 截图时长
INTERVAL = 0.3  # 截屏频率一次
WINDOW_WIDTH = 2560
REGION = (0, 0, 1920, 1080)  # 截图范围


def main():
    """主函数"""
    starttime = time.time()
    pre_image = None
    while time.time() - starttime <= TIMEOUT:
        time.sleep(INTERVAL)
        current_image = screenshot(region=REGION)
        if current_image == pre_image:
            continue
        now = datetime.datetime.now()
        target = DIRECTORY.joinpath(
            now.strftime("%Y-%m-%d"),
            now.strftime("%H-%M-%S-%f")[:-4],
        ).with_suffix(".png")
        target.parent.mkdir(exist_ok=True, parents=True)
        with open(target, "wb") as fp:
            current_image.save(fp=fp, format="png")
        if pre_image is not None:
            pre_image.close()
        pre_image = current_image


if __name__ == "__main__":
    main()
