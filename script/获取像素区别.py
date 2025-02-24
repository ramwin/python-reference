#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


from pathlib import Path

import click
import numpy
import numpy as np
from PIL import Image


@click.group()
def cli():
    pass


def open_path(path: Path) -> numpy.array:
    return numpy.array(Image.open(path).convert("L"), dtype=np.int16)


def is_diff(a, b):
    return np.count_nonzero(np.maximum(
        np.zeros(a.shape, dtype=np.int16),
        np.abs(a - b) - 50
    )) > 3000


@cli.command()
@click.option("--source")
@click.option("--target")
def compare(source, target):
    image_a = numpy.array(Image.open(source).convert("L"), dtype=np.int16)
    image_b = numpy.array(Image.open(target).convert("L"), dtype=np.int16)
    height, width = image_a.shape
    diff = numpy.maximum(
        numpy.zeros(image_a.shape, dtype=np.int16),
        numpy.abs(image_a - image_b) - 50
    )
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
    files.sort()
    duplicate_dir = source.joinpath("重复图片")
    duplicate_dir.mkdir(exist_ok=True)

    previous = None
    previous_index = -1
    for index in range(len(files) - 1):
        if previous is None:
            previous = open_path(files[index])
            previous_index = index
            continue
        current = open_path(files[index])
        if is_diff(previous, current):
            previous = current
            previous_index = index
            continue
        print(f"重复: {files[previous_index]}")
        files[previous_index].rename(
            duplicate_dir.joinpath(files[previous_index].name)
        )
        previous = current
        previous_index = index


if __name__ == "__main__":
    cli()
