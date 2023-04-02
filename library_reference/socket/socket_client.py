#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2020-03-18 15:02:44


"""
测试socket链接
"""


import time
import socket

import click


HOST = click.prompt("输入访问的IP", default="ramwin.com")
PORT = click.prompt("输入访问端口号", default=50008, type=int)
for i in range(100):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("链接上啦")
        print(s)
        for i in range(1):
            s.sendall(str(i).encode('utf-8'))
            data = s.recv(1024)
            print('Received', repr(data))
            time.sleep(0.1)
