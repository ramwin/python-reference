#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import logging
import os

from pathlib import Path


LOGGER = logging.getLogger(__name__)


def main():
    for parent, dirs, files in os.walk("."):
        for dir in dirs:
            directory = Path(parent, dir)
            if not list(directory.iterdir()):
                LOGGER.warning("删除文件夹: %s", directory)
                directory.rmdir()


if __name__ == "__main__":
    main()
