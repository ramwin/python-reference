#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import click


@click.command()
@click.option("--dry-run", "-n", is_flag=True)
def main(**kwargs):
    print(kwargs)


if __name__ == '__main__':
    main()
