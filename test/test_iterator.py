#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2020-03-21 22:35:56


class Multi(object):

    def __init__(self):
        self.start = 2
        self.step = 2

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")
        self.start *= 2
        if self.start >= 1000:
            raise StopIteration
        return self.start


# __iter__和__next__都在一个函数里面
def test1():
    a = Multi()
    for i in iter(a):
        print(i)


class Multi(object):

    def __init__(self):
        self.start = 2
        self.step = 2

    def __next__(self):
        print("__next__")
        self.start *= 2
        if self.start >= 1000:
            raise StopIteration
        return self.start


class CreateIterator(object):

    def __iter__(self):
        print("__iter__")
        return Multi()


# __iter__和__next__不在一个object里面
def test2():
    a = CreateIterator()
    for i in a:
        print(i)


