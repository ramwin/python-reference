#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import logging


logging.basicConfig(level=logging.INFO)


def main():
    logging.info("123", stack_info=True,
                 extra={'foo': 'bar'})


main()
