#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-05-04 11:18:05

import os

def main(filename):
    file = open(filename,'r')
    line = ''
    index = 0
    for i in  file.readlines():
        index += 1
        if len(i) > len(line):
            line = i
    print('文件 %s : 第%d行最长'%(filename,index))
    print(line,end=',')
if __name__ == '__main__':
    for filename in os.sys.argv[1:]:
        main(filename)
