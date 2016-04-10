#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @  ramwin@qq.com2016-04-05 11:15:56

import time

class A(object):
    def __init__(self, name):
        self.name = name
    def get(self):
        return self.name
class B(object):
    def __init__(self, name):
        self.name = name
    @staticmethod
    def get(object):
        return object.name
    def aget(self):
        return B.get(self)

start = time.time()
for i in range(1000000):
    a = B(i)
    B.get(a)
end = time.time()
print('使用静态方法耗时%0.2f秒'%(end-start))

start = time.time()
for i in range(1000000):
    a = A(i)
    a.get()
end = time.time()
print('使用非静态方法耗时%0.2f秒'%(end-start))
