#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-02-20 11:21:16

class B(object):
    pass
class C(object):
    def print_name(self):
        print(C.b.name1)

class A(object):
    name = 'test'

def createA():
    classa = A
    classb = B
    classb.name1 = classa.name
    classa.B = classb
    classa.C = C
    classa.C.b = classa.B
    return classa
classa = createA()
c = classa.C()
c.print_name()
