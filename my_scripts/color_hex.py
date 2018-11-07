#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-11-17 18:14:40

import click


@click.command()
@click.argument("color")
def get(color):
    color = int(color)
    hexs = hex(color).lstrip('0x').zfill(2)
    click.echo(hexs)


if __name__ == "__main__":
    get()
