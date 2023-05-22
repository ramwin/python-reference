#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


from pathlib import Path

import click
import numpy
from PIL import Image


@click.group()
def cli():
    pass


def open_path(path: Path) -> numpy.array:
    return numpy.array(Image.open(path).convert("L"))


def is_diff(a, b):
    return numpy.count_nonzero(a - b) > 3000


@cli.command()
@click.option("--source")
@click.option("--target")
def compare(source, target):
    image_a = numpy.array(Image.open(source).convert("L"))
    image_b = numpy.array(Image.open(target).convert("L"))
    height, width = image_a.shape
    diff = image_a - image_b
    diff_count = numpy.count_nonzero(diff)
    print(f"有 {diff_count} 个像素不一致, 百分比: {diff_count * 100/(height * width):02f}%")


@cli.command()
@click.option("--source")
def handle(source):
    source = Path(source)
    files = [
        image_path
        for image_path in source.iterdir()
        if image_path.suffix == ".png"
    ]
    duplicate_dir = source.joinpath("重复图片")
    duplicate_dir.mkdir(exist_ok=True)

    previous = None
    for index in range(len(files) - 1):
        if previous is None:
            previous = open_path(files[index])
            continue
        current = open_path(files[index])
        if is_diff(previous, current):
            previous = current
            continue
        print(f"重复: {files[index]}")
        files[index].rename(
            duplicate_dir.joinpath(files[index].name)
        )


if __name__ == "__main__":
    cli()
