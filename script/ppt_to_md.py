#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import click
from pptx import Presentation


@click.command()
@click.argument("source")
def main(source):
    for index, slide in enumerate(Presentation(source).slides, 1):
        print(f"## {index}")
        for shape in slide.shapes:
            if getattr(shape, "text", None):
                print(f"* {shape.text}")


if __name__ == "__main__":
    main()
