#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ ramwin@qq.com 2016-04-13 17:23:47

import datetime, clock, redis

@clock.log
def normal():
    r=redis.Redis()
    r.delete('test')
    for i in range(200000):
        r.incrby('test',i)
    print(r.get('test'))
@clock.log
def use_pipe():
    r = redis.Redis()
    r.delete('test')
    pipe = r.pipeline()
    for i in range(2000000):
        pipe.incrby('test',i)
    pipe.execute()
    print(r.get('test'))


if __name__=='__main__':
    # normal()
    use_pipe()
