#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-04-26 18:12:33

class Person(object):
    def __init__(self, name, age):
        self._name = name
        self.__age = age
    def __str__(self):
        return self.name
    def same(self, obj):
        return isinstance(obj, self.__class__)
    def test(self):
        return self.help("救救 %s"%self._name)
    def _one(self):
        print("我是person")
    def printname(self):
        self._one()
    @staticmethod
    def help(text="救救我"):
        print(text)
        return text
class Student(Person):

    class motto(object):
        """
            class 内部也可以定义 class
        """
        def __init__(self, text):
            self.text = text

    def __init__(self, name):
        super(Student,self).__init__(name)
        # self._name = name
        self.__score = 0
    def __str__(self):
        return "name: {0}, score: {1}".format(self._name,self.__score)
    def print_score(self):
        print('%s: %s'%(self._name, self.__score))


# a = Person(name='a', age=18)
# b = Person(name='b', age=19)
# print(a.same(b))

def main():
    Person.help('测试静态方法')
    a = Person(name='test', age=18)
    a.test()
    a.printname()
    a._one()
    print(a._name)


class A(object):
    def _say(self):
        print("calling _say")
    def __say(self):
        print("calling __say")
    def _say_(self):
        print("calling _say_")
    def __say__(self):
        print("calling __say__")
    def out(self):
        self.__say()

a = A()
a._say()
# a.__say()  # 有两个下划线是无法被调用的
a.out()
a._say_()
a.__say__()
