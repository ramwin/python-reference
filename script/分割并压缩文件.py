#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import click
import gzip
import logging
import sys
from pathlib import Path


stdout = logging.StreamHandler(stream=sys.stdout)
stdout.setLevel(logging.INFO)
stdout.setFormatter(logging.Formatter(
     '%(asctime)s [%(module)s:%(lineno)d] %(levelname)s %(message)s'
    ))
logging.basicConfig(handlers=[stdout], level=logging.INFO)


class Spliter:

    def __init__(self, source: Path, target: Path, size: int, header_cnt: int):
        self.source = source
        self.target = target
        self.size = size
        self.header_cnt = header_cnt
        self.header = ""
        self.file_index = 0
        self.start_line = 0
        self.end_line = 0

    def prepare(self) -> None:
        assert self.target.exists()
        assert self.target.is_dir()
        assert not list(self.target.iterdir())
        self.open = open(self.source, "r")
        self.start_line = self.header_cnt
        self.end_line = self.start_line + self.size
        for i in range(self.header_cnt):
            self.header += self.open.readline()

    def get_writer(self) -> None:
        self.start_line = self.file_index * self.size + self.header_cnt
        self.end_line = self.start_line + self.size
        target_sub = Path(self.target,
                          (
                              f"{self.source.stem}_{self.file_index:03d}_"
                              f"{self.start_line}_{self.end_line}"
                              f"{self.source.suffix}.gz"
                          ))
        writer = gzip.open(target_sub, "xt", compresslevel=1)
        return writer

    def run(self):
        self.prepare()
        EOF = False
        while not EOF:
            writer = self.get_writer()
            writer.write(self.header)
            for _ in range(self.size):
                line = self.open.readline()
                writer.write(line)
                if not line:
                    EOF = True
                    break
            writer.close()
            self.file_index += 1
        self.final()

    def final(self):
        self.open.close()

@click.command()
@click.option("-s", "--source")
@click.option("-t", "--target")
@click.option("--size", default=10000)
@click.option("--header", default=0)
def main(source: Path, target: Path, size: int, header: int):
    """把source文件按照固定行数拆分到目标路径并压缩"""
    Spliter(Path(source), Path(target), size, header).run()


if __name__ == "__main__":
    main()
