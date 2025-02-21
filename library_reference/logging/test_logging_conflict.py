#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import time
from logging.handlers import TimedRotatingFileHandler

from multiprocessing import Pool
import click


file_handler = TimedRotatingFileHandler(
        filename="conflict_log/info.log",
        when="S",
        backupCount=10,
)
file_handler.setFormatter(logging.Formatter(
    '[%(levelname)5s] %(asctime)s %(process)d %(name)s '
    '%(funcName)s (line: %(lineno)d)'
    '    %(message)s'
))
logging.basicConfig(level=logging.INFO, handlers=[file_handler])
LOGGER = logging.getLogger(__name__)


def write_log(process_id, **kwargs):
    for i in range(10000):
        LOGGER.info("进程 %d 的日志: %d", process_id, i)


@click.command()
@click.option("--jobs", default=1)
def main(jobs):
    now = time.time()
    time.sleep( 10 - now % 10)
    # print("开始")
    # for i in range(100):
    #     write_log(i)
    # return
    with Pool(jobs) as p:
        p.map(write_log, range(100))


if __name__ == "__main__":
    main()
