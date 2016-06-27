#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-06-27 10:09:08

class A(object):
    def __init__(self, x):
        self.x = x
    def __cmp__(self, obj):
        ''' 已经被弃用了 '''
        if abs(self.x) > abs(obj.x):
            return 1
        elif abs(self.x) == abs(obj.x):
            return 0
        else:
            return -1


a = A(-2)
b = A(3)
print(a >= b)
