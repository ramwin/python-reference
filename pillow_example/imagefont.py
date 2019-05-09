#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-05-09 14:31:05


from PIL import ImageFont, ImageDraw, Image


image = Image.new("RGB", (480, 320), 0xffffff)
draw = ImageDraw.Draw(image)

# font = ImageFont.truetype("VeraMono.ttf", 15)
# font = ImageFont.truetype("VeraMono", 15)
# font = ImageFont.load_default()
font = ImageFont.truetype("/usr/share/fonts/TTF/DroidSansFallbackFull.ttf")

draw.text((10, 10), "您好", fill=0x0000ff, font=font)

image.save("test.png")
