#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
解压漫画的zip文件到当前文件夹. 
"""


import logging
from pathlib import Path

from zipfile import ZipFile


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


def main():
    """
    1. 把zip文件解压到当前文件夹.
    2. 并把里面的内容移动到最外面
    3. 把第x页抽取出来，直接变成0x页
    """
    for zip_file in sorted(Path().iterdir()):
        target_dir = Path(zip_file.stem.replace(" ", "-"))
        if target_dir.exists():
            continue
        LOGGER.info("解压: %s", zip_file)
        if zip_file.suffix == ".zip":
            with ZipFile(zip_file, "r") as myzip:
                myzip.extractall(target_dir)
        break


if __name__ == "__main__":
    main()
