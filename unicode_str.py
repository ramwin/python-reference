#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-11-21 11:52:15


from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class A(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "name: {0}".format(self.name)


class B(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "B: name: {0}".format(self.name)


def f(a, b):
    s = "可以的{0}, {1}".format(a, b)
    print(s)


if __name__ == '__main__':
    a = A('桃子🍑')
    print(a)
    b = B('桃子🍑')
    f(a, b)
