#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import click
import numpy
from PIL import Image


@click.command()
@click.option("--source")
@click.option("--target")
def main(source, target):
    image_a = numpy.array(Image.open(source).convert("L"))
    image_b = numpy.array(Image.open(target).convert("L"))
    height, width = image_a.shape
    diff = image_a - image_b
    diff_count = numpy.count_nonzero(diff)
    print(f"有 {diff_count} 个像素不一致, 百分比: {diff_count * 100/(height * width):02f}%")


if __name__ == "__main__":
    main()
