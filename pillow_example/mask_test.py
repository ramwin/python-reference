#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-05-10 16:47:20


import io

from PIL import Image, ImageColor, ImageDraw, ImageFont
import requests


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


def circle_image(from_image):
    """把一张正方形图片变成圆圈图片"""
    x, y = image_size = from_image.size
    assert x == y, f"图片的长{x}, 宽{y}不一样"
    image = Image.new("RGBA", image_size, "#00000000")
    draw = ImageDraw.Draw(image)
    draw.chord(
        ((0,0), image_size),
        0, 360,
        outline="#FF0000",
        fill="#00FF00",
        width=3,)
    image.paste(from_image, (0,0), image)
    return image



def test1():
    image = Image.open("底图.png")
    res = requests.get(
        "https://publicstatic.duishang.net/avatar-2586-d188f5637c5f4"
        "ea6b3b5fb8a425ad9b6?imageView2/1/w/112"
        )
    image_avatar = Image.open(io.BytesIO(res.content))
    image_avatar = circle_image(image_avatar)
    image.paste(image_avatar, (465, 100), image_avatar)
    image.save("result.png")


def test2():
    green_img = Image.new("RGBA", (1000, 1000), 0xff00ff00)
    draw = ImageDraw.Draw(green_img)
    font = ImageFont.truetype("./font.ttf")

    green_solid_img = Image.new("RGBA", (100, 100), 0xff00ff00)
    red_solid_img = Image.new("RGBA", (100, 100), 0xff0000ff)
    red_half_img = Image.new("RGBA", (100, 100), 0x800000ff)
    solid_mask = Image.new("RGBA", (100, 100), 0xffffffff)
    half_mask = Image.new("RGBA", (100, 100), 0x80808080)
    trans_mask = Image.new("RGBA", (100, 100), 0x00000000)

    height = 10
    width = 10
    green_img.paste(red_solid_img, (width, height), red_solid_img)
    draw.text((width, height+100), "红色的实心圆\n(自己mask)", font=font, fill=ImageColor.getrgb("#0000ff"))

    width += 110
    green_img.paste(red_solid_img, (width, height), solid_mask)
    draw.text((width, height+100), "红色的实心圆\n(实心mask)", font=font, fill=ImageColor.getrgb("#0000ff"))

    width += 110
    green_img.paste(red_solid_img, (width, height), half_mask)  # 贴红色，但是用个半透明
    draw.text((width, height+100), "红色的实心圆\n(半透明mask)", font=font, fill=ImageColor.getrgb("#0000ff"))

    width += 100
    green_img.paste(red_solid_img, (width, height), trans_mask)
    draw.text((width, height+100), "红色的实心圆\n(透明mask)", font=font, fill=ImageColor.getrgb("#0000ff"))

    width = 10
    height += 130
    green_img.paste(red_half_img, (width, height), red_half_img)
    draw.text((width, height+100), "红色的半透明圆\n(自己mask)", font=font, fill=ImageColor.getrgb("#0000ff"))

    width += 110
    green_img.paste(red_half_img, (width, height), solid_mask)
    draw.text((width, height+100), "红色的半透明圆\n(实心mask)", font=font, fill=ImageColor.getrgb("#0000ff"))

    width += 110
    green_img.paste(red_half_img, (width, height), half_mask)
    draw.text((width, height+100), "红色的半透明圆\n(半透明mask)", font=font, fill=ImageColor.getrgb("#0000ff"))

    width += 100
    green_img.paste(red_half_img, (width, height), trans_mask)
    draw.text((width, height+100), "红色的半透明圆\n(透明mask)", font=font, fill=ImageColor.getrgb("#0000ff"))

    height += 130
    width = 10
    green_img.paste(solid_mask, (width, height), solid_mask)
    draw.text((width, height+100), "白色不透明圆\n(自己mask)", font=font, fill=ImageColor.getrgb("#0000ff"))

    width += 110
    green_img.paste(solid_mask, (width, height), solid_mask)
    draw.text((width, height+100), "白色不透明圆\n(实心mask)", font=font, fill=ImageColor.getrgb("#0000ff"))

    width += 110
    green_img.paste(solid_mask, (width, height), half_mask)
    draw.text((width, height+100), "白色不透明圆\n(半透明mask)", font=font, fill=ImageColor.getrgb("#0000ff"))

    width += 100
    green_img.paste(solid_mask, (width, height), trans_mask)
    draw.text((width, height+100), "白色不透明圆\n(透明mask)", font=font, fill=ImageColor.getrgb("#0000ff"))

    height += 130
    width = 10
    green_img.paste(half_mask, (width, height), half_mask)
    draw.text((width, height+100), "白色半透明圆\n(自己mask)", font=font, fill=ImageColor.getrgb("#0000ff"))

    width += 110
    green_img.paste(half_mask, (width, height), solid_mask)
    draw.text((width, height+100), "白色半透明圆\n(实心mask)", font=font, fill=ImageColor.getrgb("#0000ff"))

    width += 110
    green_img.paste(half_mask, (width, height), half_mask)
    draw.text((width, height+100), "白色半透明圆\n(半透明mask)", font=font, fill=ImageColor.getrgb("#0000ff"))

    width += 100
    green_img.paste(half_mask, (width, height), trans_mask)
    draw.text((width, height+100), "白色半透明圆\n(透明mask)", font=font, fill=ImageColor.getrgb("#0000ff"))

    green_img.save("result.png")


if __name__ == "__main__":
    test2()
