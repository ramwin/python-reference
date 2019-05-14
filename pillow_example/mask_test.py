#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-05-10 16:47:20


# 测试mask的功能

from PIL import Image, ImageColor


def only_middle(x):
    if 230 > x > 100:
        return 255
    return 0

image = Image.open("底图.png")

# 有颜色就张贴金色
img = Image.open("图片1.png")
img = img.resize((160,160))
img.save("小尺寸.png")
img = img.convert(mode="L")
img.save('灰度图.png')
img = Image.eval(img, only_middle)
# for column in range(img.size[0]):
#     for row in range(img.size[1]):
#         if pixels[column][row] == (255,255,255,255):
#             pixels[column][row] = (255,255,255,0)

yellow = Image.new("RGBA", (160, 160), ImageColor.getrgb("#ffae00ff"))
image.paste(yellow, box=(450, 850), mask=img)
image.save("test.png")

# 有白色就粘贴白色
