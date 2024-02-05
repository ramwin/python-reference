#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""转化缓存的bilibili视频"""


import json
from pathlib import Path
import shutil
import subprocess

import click


@click.command()
@click.option("--source", prompt="输入需要转化的文件夹")
def main(source):
    """转化缓存的bilibili视频"""
    for directory in Path(source).iterdir():
        with open(directory / "entry.json", encoding="utf8") as f:
            info = json.load(f)
        page = int(info["page_data"]["page"])
        filename = Path(
                "转化",
                f'{page:02d}-{info["page_data"]["part"]}',
        ).with_suffix('.mp4')
        filename.parent.mkdir(exist_ok=True, parents=True)
        audio = directory / str(info["video_quality"]) / "audio.m4s"
        video = directory / str(info["video_quality"]) / "video.m4s"
        mp3 = audio.rename(directory / str(info["video_quality"]) / "audio.mp3")
        mp4 = video.rename(directory / str(info["video_quality"]) / "video.mp4")
        subprocess.run([
            "ffmpeg",
            "-i", mp4,
            "-i", mp3,
            "-c:v", "copy",
            "-c:a", "aac",
            filename,
        ], check=True)
        shutil.rmtree(directory)


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
