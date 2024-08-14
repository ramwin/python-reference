#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import logging
import traceback


class IndentFormatter(logging.Formatter):

    def __init__(self, indent=0, *args, **kwargs):
        self.indent = indent
        super().__init__(*args, **kwargs)

    def format(self, record: logging.LogRecord):
        stack_indent = len(traceback.format_stack())
        indent = self.indent
        if record.msg.startswith("group: "):
            self.indent += 1
        if record.msg.startswith("groupend: "):
            self.indent -= 1
            indent -= 1
        return "    " * max(indent + stack_indent, 0) + super().format(record)


handler = logging.StreamHandler()
handler.setFormatter(IndentFormatter(-10, "%(message)s"))
logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


def test():
    logger.info("test")

def main():
    logger.info("group: main")
    logger.info("main")
    test()
    logger.info("groupend: main")


if __name__ == "__main__":
    main()
