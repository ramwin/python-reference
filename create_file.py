#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-10-13 01:09:54

import click
import random
import os

@click.command()
@click.option('-r', is_flag=True, default=False, help="生成随机文档")
@click.option('-f', is_flag=True, default=False, help="强制覆盖原有的文件")
@click.option('-s', default=1000, help="生成文件的尺寸(字节)")
@click.option('--width', default=79, help="每行的字符")
@click.argument('filename')
def create(r, f, s, width, filename):
    if os.path.exists(filename):
        if not f:
            print("文件已存在")
            return False
    file_obj = open(filename, 'w')
    if not r:  # 生成不随机文档
        for i in range(1, s+1):
            if i%width == 0:
                file_obj.write('\n')
                continue
            file_obj.write('0')
    if r:
        for i in range(1, s+1):
            if i%width == 0:
                file_obj.write('\n')
                continue
            file_obj.write(chr(random.randint(32,126)))


if __name__ == '__main__':
    create()
