#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-11-02 14:46:44


from PIL import Image, ImageDraw
import random


def create_image(
        width=2000, height=1500,
        row=6, column=8,
        path="test.png", percent=0.48,
        background=0xffffff):
    """
    生成一张有各种小球图片
    """
    total = row*column  # 一共的圆
    yellow_total = int(row*column*percent)
    print(yellow_total)
    yellow_cnt = 0
    blue_total = total - yellow_total
    print(blue_total)
    blue_cnt = 0
    image = Image.new('RGB', (width, height), background)
    draw = ImageDraw.Draw(image)
    fill_color = 0x00ff00  # 填充颜色
    rec_width = width/column
    rec_row = height/row
    padding = 4  # 设置圆和边界之间的间隔
    for i in range(row):  # 第i行
        for j in range(column):  # 第j列
            if random.randint(1, total - yellow_cnt - blue_cnt) <= \
               (yellow_total - yellow_cnt):
                color = 'yellow'
                yellow_cnt += 1
            else:
                color = 'blue'
                blue_cnt += 1
            draw.chord(
                ((rec_width*j+padding, rec_row*i+padding), (rec_width*(j+1)-padding, rec_row*(i+1)-padding)),
                0, 360, fill=color)
    print(blue_cnt)
    image.save(path)


def paste_an_circle_to_image():
    image = Image.open("底图.png")
    draw = ImageDraw.Draw(image)
    draw.ellipse(
        ((0,0), (100, 100)),
        fill="#ff0000ff",
        outline="#00FF0000",
        width=10)
    image.save("画了一个圆圈的图.png")

if __name__ == '__main__':
    # for i in range(1):
    #     create_image()
    paste_an_circle_to_image()
