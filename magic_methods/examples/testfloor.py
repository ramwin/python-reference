#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-06-27 15:27:40

class A(object):
    def __init__(self, number):
        self.x = number

    def __truediv__(self, obj):
        return self.x / obj.x

    def __floordiv__(self, obj):
        return self.x // obj.x


print(A(3)//A(2))
