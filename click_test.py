#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-08-28 14:57:18

import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(click.style('!'*100 + 'Hello %s!' % name, bg='blue', fg='red', bold=True, blink=True))

if __name__ == '__main__':
    hello()
