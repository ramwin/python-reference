#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
当前文件夹启动ftp服务
"""


import logging

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


file_handler = logging.FileHandler("ftp.log", mode="a")

logging.basicConfig(
    level=logging.INFO,
    format=(
        '%(asctime)s %(pathname)s[line:%(lineno)d] %(levelname)s %(message)s'
    ),
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        file_handler,
    ],
)


def main():
    authorizer = DummyAuthorizer()

    authorizer.add_user('wangxiang', 'ftppass', '.', perm='elradfmwMT')

    handler = FTPHandler
    handler.authorizer = authorizer

    handler.banner = "pyftpdlib based ftpd ready."

    address = ('0.0.0.0', 21)
    server = FTPServer(address, handler)

    server.max_cons = 256
    server.max_cons_per_ip = 5

    server.serve_forever()

if __name__ == '__main__':
    main()
