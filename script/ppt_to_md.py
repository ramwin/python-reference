#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import click
from pathlib import Path
from pptx import Presentation


@click.command()
@click.argument("source", type=Path)
def main(source):
    print(f"# {source.stem}")
    for index, slide in enumerate(Presentation(source).slides, 1):
        print(f"## {index}")
        for shape in slide.shapes:
            if getattr(shape, "text", None):
                print(f"* {shape.text}")


if __name__ == "__main__":
    main()
