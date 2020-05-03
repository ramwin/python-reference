#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2020-04-13 13:50:29


class Animal(object):
    def __init__(self, *args, **kwargs):
        print("chushihua")
        pass


class Dog(Animal):

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

    def say(self):
        print("i'm dog")


class Cat(Animal):
    def say(self):
        print("I'm cat")


class Some(object):

    def __new__(self, type, *args, **kwargs):
        import ipdb
        ipdb.set_trace()
        if type == 'dog':
            return Dog(*args, **kwargs)
        return Cat(*args, **kwargs)


d = Some("dog")
d.say()
c = Some("cat")
c.say()
