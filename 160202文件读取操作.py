#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-02-02 15:13:47

path = '160202操作文件.txt'
def test1():
    '''w模式进行写入操作'''
    file = open(path,'w')
    file.write('1\n2\n3\n4\n')
    file.close()
test1()
