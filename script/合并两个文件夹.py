#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import logging
from pathlib import Path
import shutil

import click


LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    filemode="a",
    format="%(asctime)s %(pathname)s[line:%(lineno)d] %(levelname)s %(message)s",
    filename="info.log",
)
LOGGER.addHandler(logging.StreamHandler())


def copy(source, target):
    paths = list(source.iterdir())
    files = [
        path
        for path in paths
        if path.is_file()
    ]
    directories = [
        path
        for path in paths
        if path.is_dir()
    ]
    for source_file_path in files:
        target_file_path = target.joinpath(source_file_path.relative_to(source))
        target_file_path.parent.mkdir(exist_ok=True, parents=True)
        if not target_file_path.exists():
            LOGGER.info("move %s => %s", source_file_path, target_file_path)
            shutil.move(source_file_path, target_file_path)
        else:
            if target_file_path.stat().st_size >= source_file_path.stat().st_size:
                LOGGER.info("unlink: %s", source_file_path)
                source_file_path.unlink()
            else:
                target_file_path.unlink()
                shutil.move(source_file_path, target_file_path)
                LOGGER.info("move %s => %s", source_file_path, target_file_path)
    for source_directory in directories:
        target_directory = target.joinpath(source_directory.relative_to(source))
        copy(source_directory, target_directory)
    LOGGER.info("clear dir: %s", source)
    source.rmdir()


@click.command()
@click.option("--source")
@click.option("--target")
def main(source, target):
    """把source的文件都复制到target"""
    copy(Path(source), Path(target))


if __name__ == "__main__":
    main()
