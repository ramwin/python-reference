#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import logging
from pathlib import Path
import shutil

import click

import logging_config


def copy(source, target):
    logging.info("复制文件夹 %s => %s", source, target)
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
            logging.info("move %s => %s", source_file_path, target_file_path)
            shutil.move(source_file_path, target_file_path)
        else:
            if target_file_path.stat().st_size >= source_file_path.stat().st_size:
                logging.info("unlink: %s", source_file_path)
                source_file_path.unlink()
            else:
                target_file_path.unlink()
                logging.info("move %s => %s", source_file_path, target_file_path)
                shutil.move(source_file_path, target_file_path)
    for source_directory in directories:
        target_directory = target.joinpath(source_directory.relative_to(source))
        copy(source_directory, target_directory)
    logging.info("clear dir: %s", source)
    source.rmdir()


@click.command()
@click.option("--source")
@click.option("--target")
def main(source, target):
    """把source的文件都复制到target"""
    copy(Path(source), Path(target))


if __name__ == "__main__":
    main()
