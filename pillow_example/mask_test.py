#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-05-10 16:47:20


# 测试mask的功能

from PIL import Image, ImageColor


# 写个脚本只保留中间颜色，排除黑白两色, 把其他颜色都变成自定义色调


def exclude_black_and_white(x):  # 这样两边的黑色背景和白色背景就都没有了, 只保留文字（文字不是全黑或者全白的)
    if 30 < x < 230:
        return 255
    return 0


def convert_image(from_image, to_image, background, frontcolor):
    img = Image.open(from_image)
    image_size = img.size
    img = img.resize(image_size)
    img = img.convert(mode="L")
    img = Image.eval(img, exclude_black_and_white)
    result = Image.new("RGBA", image_size, background)
    yellow = Image.new("RGBA", image_size, frontcolor)
    result.paste(yellow, (0, 0), mask=img)
    result.save(to_image)


if __name__ == "__main__":
    convert_image(
        "黑白原图.png",
        "result.png",
        background="purple",
        frontcolor="gold",
        # ImageColor.getrgb("#00000000"),
        # ImageColor.getrgb("#ffae00ff"),
    )
