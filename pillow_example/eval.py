#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-05-14 16:34:36


from PIL import Image


def only_white_and_blck(x):
    if 20 < x < 235:
        return 0
    else:
        return x


img = Image.open("黑白原图.png")
img_excluded = Image.eval(img, only_white_and_blck)
img_excluded.save("黑白原图只保留极端颜色.png")
