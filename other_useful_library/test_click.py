#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


from pathlib import Path
import click


@click.command()
@click.argument("path", nargs=2, type=click.Path(exists=True, path_type=Path))
def main(path):
    print(path)


main()
