#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-10-13 01:09:54

import click
import random

@click.command()
@click.option('-r', is_flag=True, default=False)
@click.option('-f', is_flag=True, default=False)
@click.argument('filename')
def create(r, f, filename):
    if os.path.exists(filename):
        if not f:
            print("文件已存在")
            return False
    file_obj = open(filename, 'wb')
    if r is not True:  # 生成随机文档
        file_obj.write('0')


if __name__ == '__main__':
    create()
