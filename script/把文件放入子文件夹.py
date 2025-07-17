#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


from pathlib import Path


def handle_directory(sub_dir):
    """
    00
        00/00123.png => 00/00/123.png
    """
    files = list(sub_dir.iterdir())
    for file_path in files:
        assert file_path.is_file()
        target = sub_dir.joinpath(
            file_path.name[0:2],
            file_path.name[2:],
        )
        target.parent.mkdir(exist_ok=True)
        assert not target.exists()
        file_path.rename(target)


def main():
    for sub_dir in Path().iterdir():
        if sub_dir.is_file():
            continue
        handle_directory(sub_dir)


main()
