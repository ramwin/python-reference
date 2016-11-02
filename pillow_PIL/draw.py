#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-11-02 14:46:44


from PIL import Image, ImageDraw
import random


def create_image(width=1000, height=1000, row=10, column=10, path="test.png", percent=0.4, background=0xffffff):
    """
    生成一张有各种小球图片
    """
    total = row*column  # 一共的圆
    yellow_total = int(row*column*percent)
    yellow_cnt = 0
    blue_total = total - yellow_total
    blue_cnt = 0
    image = Image.new('RGB', (width, height), background)
    draw = ImageDraw.Draw(image)
    fill_color = 0x00ff00  # 填充颜色
    rec_width = width/row
    rec_row = width/column
    padding = 20  # 设置圆和边界之间的间隔
    for i in range(row):  # 第i行
        for j in range(column):  # 第j列
            if random.randint(1, total - yellow_cnt - blue_cnt) > (yellow_total - yellow_cnt):
                color = 'yellow'
            else:
                color = 'blue'
            draw.chord(
                ((rec_width*j+padding, rec_row*i+padding), (rec_width*(j+1)-padding, rec_row*(i+1)-padding)),
                0, 360, fill=color)
    image.save(path)


if __name__ == '__main__':
    create_image()
