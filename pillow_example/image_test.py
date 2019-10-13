#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-07-19 18:34:55


from PIL import Image


def test():
    green_image = Image.new("RGBA", (100, 100), 0xff00ff00)
    red_image = Image.new("RGBA", (100, 100), 0xff0000ff)
    half_red_image = Image.new("RGBA", (100, 100), 0x800000ff)
    bg = Image.new("RGBA", (1000, 1000), 0xffffffff)

    width = 10
    height = 10
    
    img1 = Image.alpha_composite(green_image, red_image)
    bg.paste(img1, (width, height), img1)  # 绿色加红色，变成红色

    width += 110
    img2 = Image.alpha_composite(green_image, half_red_image)  # 绿色，半透明红色，变成了黯淡的黄色
    bg.paste(img2, (width, height), img2)

    width += 110
    img3 = Image.composite(green_image, red_image, red_image)
    bg.paste(img2, (width, height), img3)

    bg.save("image_test.png")


if __name__ == '__main__':
    test()
