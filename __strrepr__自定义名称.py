#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-05-27 11:07:17

class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        ''' 这个会在 print 的时候调用 '''
        return 'Student: %s' % (self.name)

    def __repr__(self):
        ''' 这个是直接敲打变量的shell里面调用 '''
        return 'Student Object: {"name": %s}' % (self.name)


a = Student('Amy')
print(a)
