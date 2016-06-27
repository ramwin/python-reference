#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-06-27 14:43:40

class A(object):
    def __init__(self, number):
        self.x = number

    def __eq__(self, obj):
        return abs(self.x) == abs(obj.x)

    def __ne__(self, obj):
        return abs(self.x) != abs(obj.x)


a = A(-3)
b = A(2)
print(a!=b)
