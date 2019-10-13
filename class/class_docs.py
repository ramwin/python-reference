#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2019-10-10 02:21:44


def make_viewset(model, docstring):
    class A(object):
        def call(self):
            print("call")
    clsdict = {
        "test something": test_something,
        "  doc  ": docstring
    }
    return type("MyClass", (A, ), clsdict)


ViewSet = make_viewset("Ship", "我是文档")
print(ViewSet.__docs__)
