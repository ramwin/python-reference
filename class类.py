#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-04-26 18:12:33

class Student(object):
    def __init__(self, name, score):
        self._name = name
        self.__score = score
    def __str__(self):
        return "name: {0}, score: {1}".format(self._name,self.__score)
    def print_score(self):
        print('%s: %s'%(self._name, self.__score))

lucy = Student(name='lucy', score=18)
print(lucy)
print(lucy._name)
print(lucy.__score)
