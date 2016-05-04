#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-01-14 13:46:54

import redis,time
def main():
    r = redis.StrictRedis(host='localhost',port=6379,db=0)
    i=0
    while True:
        i+=1
        r.rpush('mylist',i)
        time.sleep(0.01)
if __name__=='__main__':
    main()
