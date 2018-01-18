#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ ramwin@qq.com 2016-04-22 17:36:02

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
    import shutil
    shutil.rmtree('<directory>')


# 文件操作
* 基础
    file = open(<filename>, 'w')
    file.write('text')
    file.close()
* 模式
    w 写入模式
    b 读取模式
    a 添加模式, 无论seek到哪，write只能够添加数据
    r+ 可读可写。write以后需要flush，不然之后read会导致指针位置改变，影响结果
* 方法
    read(n)  # 读取n个字符或者字节
    seek(offset, from_what)  # offset偏移数量，from_wath 0代表开始，1代表当前，2代表末尾
