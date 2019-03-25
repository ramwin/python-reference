#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2019-03-02 15:12:40


import math
import os
import sys
from pydub import AudioSegment


abspath = sys.argv[1]
directory, filename = os.path.split(abspath)
print("当前目录", directory)
print("文件名", filename)
name, suffix = os.path.splitext(filename)


song = AudioSegment.from_file(abspath, "mp4")
export_path = os.path.join(directory, name + ".mp3")
print("导出路径", export_path)
song.export(export_path, format="mp3")
step = 3 * 60 * 1000
for i in range(math.ceil(len(song)/step)):
    destination = os.path.join(
        directory,
        "{}_{:02d}.mp3".format(name, i)
    )
    song[step*i: (i+1)*step].export(destination, format="mp3")
