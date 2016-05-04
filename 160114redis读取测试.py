#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-01-14 13:48:25

import redis,time
def main():
    r = redis.StrictRedis(host='localhost',port=6379,db=0)
    i = 0
    while True:
        i = (i +1)%1000
        t = r.blpop('mylist',0)
        if i == 0 :
            print(t[1])
        time.sleep(0.001)
if __name__=='__main__':
    main()
