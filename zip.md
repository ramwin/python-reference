#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-09-28 16:56:34


[官方教程](https://docs.python.org/3/library/zipfile.html)


## 基础用法
    from zipfile import ZipFile

    # 把文件压缩到指定文件
    with ZipFile(<filename.zip>, 'w') as myzip:
        myzip.write('filename', arcname='new_filename')  # 如果没有arcname，就会用filename来保存
