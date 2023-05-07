#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


from pathlib import Path

import chardet
import click


@click.command
@click.option("--source")
def main(source):
    files = list(Path(source).iterdir())
    for path in files:
        print(f"开始转化 {path=}")
        with open(path, 'rb') as f:
            content = f.read()
        encoding = chardet.detect(content)["encoding"]
        text = content.decode(encoding, errors="ignore")
        with open(path, "w") as f:
            f.write(text)


if __name__ == "__main__":
    main()
