#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-07-03 16:25:03


import click


@click.command()
@click.argument("path")
def transform(path):
    """把一个文件的中文换行符变成英文换行符"""
    text = open(path, "rb").read()
    text1 = text.replace(b'\r\n', b'\n')
    with open(path, "wb") as f:
        f.write(text1)
    print("转化完成")


if __name__ == '__main__':
    transform()
