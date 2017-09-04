#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-08-21 18:13:15



class Student(object):

    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        print("%s的年龄是%d" % (self.name, self._age))

    @age.setter
    def age(self, value):
        if value < 0:
            print("你的设置的年龄%d不正确" % value)
        else:
            self._age = value


student = Student("小明", 20)
student.age
student.age = -1
student.age
student.age = 21
student.age
