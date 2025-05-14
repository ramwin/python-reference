#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click


@click.group()
@click.pass_context
@click.option("--source")
@click.option("--target")
def cli(ctx, source, target):
    ctx.ensure_object(dict)
    ctx.obj["source"] = source
    ctx.obj["target"] = target


@cli.command()
@click.pass_context
def function1(ctx):
    print(ctx.obj)


if __name__ == "__main__":
    cli()
