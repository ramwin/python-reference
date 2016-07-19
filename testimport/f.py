#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-07-15 16:04:12


class A(object):
    def __init__(self, name):
        self.b = B(name)
        


class B(object):
    def __init__(self, name):
        self.name = name
