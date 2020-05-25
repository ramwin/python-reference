#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2020-05-25 23:17:06

from PIL import Image, ImageDraw

blue = Image.new("RGB", (480, 320), 0xffffff00)
blue.save("origin.png")

red = Image.new("RGB", (150, 150), 0xff0000ff)
red.save("red.png")

# blue.paste(red, (100, 100))

mask = Image.new("RGBA", (150, 150), 0x00000000)
draw = ImageDraw.Draw(mask)
draw.chord(((0, 0), (150, 150)), 0, 360, 0xffffffff)
mask.save("mask.png")
# blue.save("before_paste.png")
blue.paste(red, (150, 150), mask=mask)
# blue.paste(red, (150, 150))
blue.save("paster_in_draw.png")
