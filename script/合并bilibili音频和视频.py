#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import json
from pathlib import Path
import subprocess


def main():
    for directory in Path("17649289").iterdir():
        with open(directory / "entry.json", encoding="utf8") as f:
            info = json.load(f)
        page = int(info["page_data"]["page"])
        filename = f"转化/{page:02d}-" + \
            info["page_data"]["part"] + ".mp4"
        audio = directory / "64/audio.m4s"
        video = directory / "64/video.m4s"
        mp3 = audio.rename(directory / "64/audio.mp3")
        mp4 = video.rename(directory / "64/video.mp4")
        subprocess.run([
            "ffmpeg",
            "-i", mp4,
            "-i", mp3,
            "-c:v", "copy",
            "-c:a", "aac",
            filename,
        ], check=True)


if __name__ == "__main__":
    main()
