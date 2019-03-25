#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-03-18 19:24:25

class A(object):
    pass

def runfast():
    print("I'm running fast")

setattr(A, 'run-fast', runfast)

a = A()
getattr(A, 'run-fast')()
