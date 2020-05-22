#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2020-04-13 13:50:29


class Animal(object):
<<<<<<< HEAD
    class_attr = 'animal'
=======
    class_attr = 'class_attr'
>>>>>>> 745286e788c3e44108ec9944b26bad26314f3fa2
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
# d.say()
d.class_attr = 'new attr'  # 如果没有这个赋值，那么d的class_attr会被下面这句覆盖
Animal.class_attr = 'new attr2'
print(d.class_attr)
c = Some("cat")
# c.say()
print(c.class_attr)
