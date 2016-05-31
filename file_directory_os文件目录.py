#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ ramwin@qq.com 2016-04-22 17:36:02

import os, shutild
# 目录操作
## 获取当前目录  
    os.getcwd()
    os.path.abspath('.')

## 是否是目录
    os.path.isdir("<path>")

## 切换目录
    os.chdir('Pictures')

## 遍历文件
    os.listdir()

## 删除目录
    shutil.rmtree('<directory>')
