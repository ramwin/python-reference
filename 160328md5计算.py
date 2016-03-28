#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-03-28 15:48:38

import os
import hashlib

def md5file(fileobject):
    md5sum = hashlib.md5()
    read = True
    filebuf = fileobject.read(4*1024*1024)
    while filebuf:
        md5sum.update(filebuf)
        filebuf = fileobject.read(4*1024*1024)
    return md5sum.hexdigest()
        
if __name__ == '__main__':
    if len(os.sys.argv) == 2:
        filename = os.sys.argv[1]
        fileo = open(filename,'rb')
        print('正在计算文件: %s 的md5码'%(filename))
        md5sum = md5file(fileo)
        print('文件名: %s'%(filename),end=' ')
        print('md5码: %s'%(md5sum))
    else:
        print('输入参数文件名')
