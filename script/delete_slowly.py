#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import logging
import os
import time
from pathlib import Path

import click
import colorlog


handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    "%(log_color)s %(process)d %(levelname)s:%(name)s:%(message)s"
    ))
file_handler = logging.FileHandler("info.log", mode="w")
file_handler.setFormatter(logging.Formatter(
     '%(asctime)s [%(module)s:%(lineno)d] %(levelname)s %(message)s'
    ))
logging.basicConfig(level=logging.INFO, handlers=[handler, file_handler])

LOGGER = logging.getLogger(__name__)


@click.command()
@click.argument("source")
def main(source: Path):
    source = Path(source)
    LOGGER.info("清理文件夹: %s", source.absolute())
    for parent, dirs, files in os.walk(source, topdown=False):
        LOGGER.info("处理文件夹: %s", parent)
        for file in files:
            to_delete = Path(parent, file)
            LOGGER.info("删除: %s", to_delete)
            to_delete.unlink()
            time.sleep(0.01)
        for directory in dirs:
            to_delete = Path(parent, directory)
            to_delete.rmdir()
            time.sleep(0.01)
        LOGGER.info("删除文件夹: %s", parent)
        Path(parent).rmdir()
        time.sleep(0.1)


if __name__ == "__main__":
    main()
