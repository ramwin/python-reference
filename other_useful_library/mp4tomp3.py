#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2019-03-02 15:12:40


import math
import os
import sys
from pydub import AudioSegment


abspath = sys.argv[1]
directory, filename = os.path.split(abspath)
name, suffix = os.path.splitext(filename)


song = AudioSegment.from_file(abspath, "mp4")
song.export(os.path.join(directory, name + ".mp3"), format="mp3")
step = 3 * 60 * 1000
for i in range(math.ceil(len(song)/step)):
    destination = os.path.join(
        directory,
        "{}_{:02d}.mp3".format(name, i)
    )
    song[step*i: (i+1)*step].export(destination, format="mp3")
