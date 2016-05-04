#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ ramwin@qq.com 2016-04-13 17:25:01

import datetime
import time
def log(f):
    def fin(*args, **kw):
        start=datetime.datetime.now()
        print('call'+f.__name__+'()...')
        f(*args,**kw)
        print('stop'+f.__name__+'()...')
        end=datetime.datetime.now()
        print('耗时 %d 秒'%(end-start).seconds)
    return fin

@log
def main():
    print(1)
    time.sleep(1)
    return 1

if __name__ == '__main__':
    main()
