#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-04-26 17:39:59
import time

# 类方法
class Date(object):
    day, month, year = 0, 0, 0
    def __init__(self, day=0, month=0, year=0):
        self.day, self.month, self.year = day, month, year
    # 这如果我要把字符串变成时间，我就要
    # day, month, year = map(int, string_data.split('-'))
    # date1 = Date(day, month, year)
    # 这样的话就很难看，而且函数在class外面了。
    @classmethod
    def from_string(cls, date_as_string):
        # 一: 代码可以复用
        # 二: 函数封装得好，不要放在外面
        # 三: 继承了Date的子类也可以用这个方法
        day, month, year = map(int, date_as_string.split('-'))
        return cls(day, month, year)

a = Date(1,1,2000)
print(a.year)

a = Date.from_string('1-1-2001')
print(a.year)

# 静态方法
class A(object):
    def __init__(self, name):
        self.name = name
    def get(self):
        return self.name
class B(object):
    def __init__(self, name):
        self.name = name
    @staticmethod
    def get(object):
        return object.name
    def aget(self):
        return B.get(self)

start = time.time()
for i in range(1):
    a = B(i)
    B.get(a)
end = time.time()
print('使用静态方法耗时%0.2f秒'%(end-start))

start = time.time()
for i in range(1):
    a = A(i)
    a.get()
end = time.time()
print('使用非静态方法耗时%0.2f秒'%(end-start))

# 类方法
class Color(object):
    _color = (0,0,0)

    @classmethod
    def value(cls):
        if cls.__name__ == 'Red':
            cls._color = (255,0,0)

        elif cls.__name__ == 'Green':
            cls._color = (0,255,0)

        return cls._color

class Red(Color):
    pass

class Green(Color):
    pass

class UnknownColor(Color):
    pass

red = Red()
print(red.value())
green = Green()
xcolor = UnknownColor()


import time
class A(object):
    def test():
        return 23
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    a = test()
