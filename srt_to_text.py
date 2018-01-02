#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-12-27 11:44:54

import click


@click.command()
@click.argument('path')
def transform(path, *args, **kwargs):
    """把
