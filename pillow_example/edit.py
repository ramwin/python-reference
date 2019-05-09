#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-11-07 14:17:42

from PIL import Image, ImageDraw
import random


blue = Image.open('blue.png', 'r')
yellow = Image.open('yellow.png', 'r')

def create_image(
    row=6, column=8,
    path="test.png", percent=0.55,
    background=0xffffff):
    """
    用原来的图片生成新的图片
    """
    image = Image.new('RGB', (800, 600), color=0xb68459)
    total = row*column  # 一共的圆
    yellow_total = int(row*column*percent)
    yellow_cnt = 0
    blue_total = total - yellow_total
    blue_cnt = 0
    rec_width = 100
    rec_row = 100
    for i in range(row): # 第i行
        for j in range(column):
            if random.randint(1, total - yellow_cnt - blue_cnt) <= \
                (yellow_total - yellow_cnt):
                circle_img = yellow
                yellow_cnt += 1
            else:
                color = "blue"
                circle_img = blue
                blue_cnt += 1

            image.paste(circle_img, box=(100*j,100*i, 100*(j+1), 100*(i+1)), mask=circle_img)
            image.save('test.png')
    print('blue')
    print(blue_cnt)
    print(yellow_cnt)


if __name__ == '__main__':
    create_image()
