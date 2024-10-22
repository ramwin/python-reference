#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


from pathlib import Path
import hashfs
from hashfs.utils import shard


def main():
    """
    把 0xabcdef/
    移动到 ab/cd/ef
    """
    source = Path("./")
    for f in list(source.iterdir()):
        target_directory = Path(
            source,
            shard(f.name.lstrip("0x"), depth=3, width=2)
        )
        target_directory.parent.mkdir(exist_ok=True, parents=True)
        f.rename(target_directory)


if __name__ == "__main__":
    main()
