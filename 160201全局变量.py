#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-02-01 16:14:57

import redis
# 如果没有这个和下面的global, main函数执行完毕后，r又变成了localhost
# global r 
r = redis.StrictRedis(host='localhost',port=6379,db=0)
print(r.get('info'))
def main():
    global r
    r = redis.StrictRedis(host='192.168.1.188',port=6379,db=0)
    print(r.get('info'))
class A():
    def __init__(self):
        # global r 无效
        pass
    def get(self):
        print(r.get('info'))
    def change(self):
        global r # 有效
        r = redis.StrictRedis(host='192.168.1.188',port=6379,db=0)
    def delete(self):
        r = 0
# main()
# print(r.get('info'))
a = A()
a.get()
a.change()
a.get()
print(r.get('info'))
a.delete()
print(r)
