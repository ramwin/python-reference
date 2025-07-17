#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
解压漫画的zip文件到当前文件夹. 
"""


import logging
import re

from pathlib import Path

from zipfile import ZipFile


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


def de_nest_directory(path: Path):
    """
    如果path只有一个文件夹，就把文件夹内的内容拿到外面来
    """
    while True:
        files = list(path.iterdir())
        if len(files) == 1 and files[0].is_dir():
            for content in files[0].iterdir():
                content.rename(
                        path.joinpath(content.name)
                )
            files[0].rmdir()
        else:
            break


def change_name(path):
    """
    把path里面的所有内容，改成纯数字
    第%d页.png => 0x.png
    """
    pattern = re.compile(r".*第(\d+)页")
    for file in list(path.iterdir()):
        match = pattern.match(file.name)
        assert match, file
        page = int(match.groups()[0])
        file.rename(file.parent.joinpath(
            f"{page:02d}" + file.suffix,
        ))


def main():
    """
    1. 把zip文件解压到当前文件夹.
    2. 并把里面的内容移动到最外面
    3. 把第x页抽取出来，直接变成0x页
    """
    for zip_file in sorted(Path().iterdir()):
        if zip_file.suffix != ".zip":
            continue
        target_dir = Path(zip_file.stem.replace(" ", "-"))
        if target_dir.exists():
            continue
        LOGGER.info("解压: %s", zip_file)
        if zip_file.suffix == ".zip":
            with ZipFile(zip_file, "r", metadata_encoding="gbk") as myzip:
                myzip.extractall(target_dir)
        de_nest_directory(target_dir)
        change_name(target_dir)


if __name__ == "__main__":
    main()
