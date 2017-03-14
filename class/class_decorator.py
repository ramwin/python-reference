#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-03-14 13:49:42


from functools import update_wrapper
def decorator(f):
    def fin(*args, **kwargs):
        print("准备调用函数啦")
        return f(*args, **kwargs)
    return update_wrapper(fin, f)


@decorator
def function():
    print("调用了function函数")


def class_decorator(f):
    class fin(f):
        def function(self):
            print("准备调用函数啦")
            super(fin, self).function()

    return fin
    

@class_decorator
class A(object):
    def function(self):
        print("调用了A.function函数")
    def function2(self):
        print('调用了没被修改的A.function2函数')


if __name__ == '__main__':
    print("测试函数装饰器=====================")
    function()
    print("测试类装饰器=======================")
    a = A()
    a.function()
    a.function2()
