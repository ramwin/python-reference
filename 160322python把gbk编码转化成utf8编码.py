#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-03-22 14:46:20

import os
def main(local, target):
    local_file = open(local,'rb')
    target_file = open(target,'w')
    error_file = open(local+'.error','ab')
    print('正在把原始文件 %s (gbk) 转化成 %s (utf-8)'%(local,target))
    print('未能转化的数据保存在 %s'%(local+'.error'))
    line = True
    while line:
        line = local_file.readline()
        try:
            tmp = line.decode('gbk')
            target_file.write(tmp)
        except:
            error_file.write(line)
    local_file.close()
    target_file.close()
    error_file.close()
    print('转化完成')

if __name__ == '__main__':
    local = os.sys.argv[1]
    target = os.sys.argv[2]
    main(local, target)
