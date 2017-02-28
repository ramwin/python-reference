#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-02-09 17:30:07

class A(object):

    def __init__(self, number):
        self.number = '1' + '0'*number

    def __add__(self, integer):
        for i in range(integer):
            self.number += '0'
        return self

    def __gt__(self, a):
        return len(self.number) > len(a.number)

    def __str__(self):
        return self.number

    def __int__(self):
        return self.number.count('0')

    def __sub__(self, a):
        return int(self) - int(a)


class myrange(object):

    def __init__(self, a1, a2):
        self.count = A(int(a1))
        self.a1 = a1
        self.a2 = a2

    def __iter__(self):
        print(id(self.a1))
        yield self.count
        for i in range(self.a2-self.a1):
            yield self.count + 1


a = A(3)
b = A(10)
for i in myrange(a, b):
    print(i)
    print(id(i))
print(a)
