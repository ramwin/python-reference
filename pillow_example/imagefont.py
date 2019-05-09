#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-05-09 14:31:05


from PIL import ImageFont, ImageDraw, Image, ImageColor


image = Image.new(
    "RGBA", (480, 320),
    ImageColor.getrgb("#f00")
)
draw = ImageDraw.Draw(image)

# font = ImageFont.truetype("VeraMono.ttf", 15)
# font = ImageFont.truetype("VeraMono", 15)
# font = ImageFont.load_default()
font = ImageFont.truetype("/usr/share/fonts/TTF/DroidSansFallbackFull.ttf", 32)

draw.text((10, 10), "您好", fill=ImageColor.getrgb("#fff"), font=font)
size1 = draw.textsize("您好", font=font)
size2 = font.getsize("您好")


image.save("test.png")
