#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-08-28 14:57:18

import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', required=True, default="ew", prompt="Your Name",
              help='The person to greet.')
@click.argument('target')
def hello(count, name, target):
    """Simple program that greets NAME for a total of COUNT times."""
    if click.confirm('继续吗'):
        print("你输入的最后参数是: %s" % target)
        for x in range(count):
            click.echo(click.style('!'*100 + 'Hello %s!' % name, bg='blue', fg='red', bold=True, blink=True, underline=True))

if __name__ == '__main__':
    hello()
