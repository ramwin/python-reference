#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import logging
import traceback
from contextvars import ContextVar


logger_groups = ContextVar("groups", default=[])


class MyFormatter(logging.Formatter):

    def format(self, record: logging.LogRecord):
        stack_len = len(traceback.format_stack()) - 9
        indent_cnt = len(logger_groups.get()) + stack_len
        if isinstance(record.msg, str):
            if record.msg.startswith("group:"):
                logger_groups.get().append(record.msg.lstrip("group:").strip())
            if record.msg.startswith("endgroup"):
                indent_cnt -= 1
        return "    " * indent_cnt + super().format(record)


handler = logging.StreamHandler()
handler.setFormatter(MyFormatter("%(name)s %(message)s"))
logging.basicConfig(
        level=logging.INFO,
        format="%(name)s %(message)s",
        handlers=[handler],
)
logger: logging.Logger = logging.getLogger(__name__)


def main():
    logger.info("开始执行main")
    logger.info("group: main")
    logger.info("123")
    logger.info("456")
    logger.info("endgroup")


def test_stack():
    logger.info(123)
    main()


if __name__ == "__main__":
    logger.info("开始")
    test_stack()
