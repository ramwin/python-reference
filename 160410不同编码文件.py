#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ ramwin@qq.com 2016-04-10 19:35:18

import os, chardet
directory='./different_encoding_file'
for code in ['utf-8','gbk','utf-16']:
    file_utf8=os.path.join(directory,code+'.txt')
    print('文件头部的30个字节是')
    print(open(file_utf8,'rb').read(30))
    print(open(file_utf8,'r',encoding=code).read())
