#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-07-29 08:17:10


import random
import os

ASCIIS = 'abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'


def main():
    """
        生成随机的密码
        可以指定密码长度(默认为6)
    """
    if len(os.sys.argv) >= 2:
        length = int(os.sys.argv[1])
    else:
        length = 6

    password = ''
    for i in range(length):
        password = password + random.choice(ASCIIS)
    print(password)


if __name__ == '__main__':
    main()
