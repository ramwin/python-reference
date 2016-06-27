#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-05-27 10:58:54

class Positive(object):
    def __init__(self, n):
        self.data = 0
        self.end = n

    def __iter__(self):
        return self

    def __getitem__(self, n):
        return n

    def __next__(self):
        if self.data >= self.end:
            raise StopIteration
        else:
            self.data += 1
            return self.data


a = Positive(5)
for i in a:
    print(i)
print(a[2])

class Next(object):
    def __init__(self, n):
        self.data = [1,2,3,4]

    def __iter__(self):
        return self.data



a = Next(3)
print(iter(a))
