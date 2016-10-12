#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-10-13 01:09:54

import click
import random

@click.command()
@click.option('-r', is_flag=True, default=False)
@click.option('-s', is
@click.argument('filename')
def create(r, filename):
    if r is True:  # 生成随机文档
    print(r)
    print(filename)


if __name__ == '__main__':
    create()
