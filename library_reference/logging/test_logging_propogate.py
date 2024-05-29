#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import logging


logging.basicConfig(handlers=[logging.StreamHandler()])

def main():
    """server 的日志只有一个，因为propagate为False"""
    client_logger = logging.getLogger("web3.client")
    client_logger.addHandler(logging.StreamHandler())
    client_logger.warning("client warning")

    server_logger = logging.getLogger("web3.server")
    server_logger.propagate = False
    server_logger.warning("server warning")


if __name__ == "__main__":
    main()

