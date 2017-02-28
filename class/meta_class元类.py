#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-02-28 14:26:12


class MetaA(type):
    def __new__(cls, name, bases, attrs):
        name = attrs.get('name')
        class B(object):
            name1 = name

        class C(object):
            b = B()
            def print_name(self):
                print C.b.name1

        cls.B = B
        cls.C = C
        return super(MetaA, cls).__new__(cls, name, bases, attrs)

        

class A(object):
    name = 'test'
    __metaclass__ = MetaA

    def __init__(self):
        c = A.C()
        c.print_name()
