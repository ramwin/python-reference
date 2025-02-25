#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import logging
import re
import signal
import time

import click
from git import Repo


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(filename)s:%(lineno)d]: %(message)s",
    handlers=[
        logging.FileHandler("info.log"),
        logging.StreamHandler()
    ]
)
stop = False


def compare_commit(left, right):
    """
    return ("mergecommit", "usercommit")
    """
    pattern = re.compile(r"(m|M)erge .* into .*\n")
    if pattern.match(left.message) and not pattern.match(right.message):
        return left, right
    if not pattern.match(left.message) and pattern.match(right.message):
        return right, left
    raise Exception("请手动处理")


def handler(signalnum, handler):
    logging.info("ctrlc了")
    global stop
    stop = True


@click.command()
@click.option("--max", type=int, default=1, help="最多rebase多少次")
@click.argument("path", default="./")
def main(max, path):

    logging.info("开始rebase")
    start = time.time()
    signal.signal(signal.SIGINT, handler)

    repo = Repo(path)
    logging.info("rebase %s 的所有分支", repo)
    rebase_times = 0

    while rebase_times < max and not stop:
        if rebase_times >= 1:
            duration = time.time() - start
            remain = (max - rebase_times) / rebase_times * duration
            logging.info("rebase %d 次, 耗时 %f 秒, 预计剩余 %f 秒",
                         rebase_times, duration, remain)
        for index, commit in enumerate(repo.iter_commits()):
            if index == 0:
                logging.info("当前最新节点是: %s", commit)
            if len(commit.parents) >= 2:
                logging.info("%s 有2个父节点, 需要rebase", commit)
                merge_commit, _ = compare_commit(*commit.parents)
                repo.git().rebase(merge_commit)
                rebase_times += 1
                break
        else:
            logging.info("所有节点处理完毕, 不存在合并节点")
            return


if __name__ == "__main__":
    try:
        main()  # pylint: disable=no-value-for-parameter
    except Exception as e:
        logging.error(e)
        logging.exception(e)
