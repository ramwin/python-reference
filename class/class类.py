#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-04-26 18:12:33

class Person(object):
    def __init__(self, name):
        self._name = name
    def __str__(self):
        return self.name
class Student(Person):
    def __init__(self, name):
        super(Student,self).__init__(name)
        # self._name = name
        self.__score = 0
    def __str__(self):
        return "name: {0}, score: {1}".format(self._name,self.__score)
    def print_score(self):
        print('%s: %s'%(self._name, self.__score))

lucy = Student(name='lucy')
print(lucy)
print(lucy._name)
