#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-02-02 11:36:20

class A():
    def __init__(self, value):
        self.value = value
    def add(self):
        self.value += 1
    def get(self):
        return self.value
    def add_get(self):
        self.add()
        return self.get()
a = A(1)
a.add()
print(a.get())
print(a.add_get())
