#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-06-08 17:23:24

import os
import time


if __name__ == '__main__':
    start = time.time()
    file_from = open(os.sys.argv[1], 'rb')
    file_to = open(os.sys.argv[2], 'wb')
    line = file_from.readline()
    index = 0
    while line:
        index += 1
        if index % 10000 == 0:
            print('已经转化了 %d 行，耗时 %d 秒' % (index, time.time() - start), end = '\r')
        file_to.write(line.rstrip(b'\n') + b'\r\n')
        line = file_from.readline()
    file_from.close()
    file_to.close()
    print('转化完成')
