#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-09-05 18:33:12


from pdf2image import convert_from_path
import os


files = os.listdir(path="行业报告")[0:1]
for source in files:
    print("转化文件: {}".format(source))
    target_directory = "行业报告_img/{}".format(source)
    if not os.path.isdir(target_directory):
        os.mkdir(target_directory)
    images = convert_from_path("行业报告/" + source)
    print("转化完毕, 保存到: {}".format(target_directory))
    for index, image in enumerate(images):
        target = "{}/{:02d}.jpeg".format(target_directory, index)
        image.save(target)
