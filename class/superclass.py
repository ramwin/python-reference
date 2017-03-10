#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-03-06 11:22:30


class Log(object):
    def get(self):
        print('log\'s get')
        return super(Log, self).get()


class Api(object):
    def get(self):
        print('api\'s get')


class NewApi(Api):
    def get(self):
        print('New Api s get')
        return super(NewApi, self).get()


class Oapi(Api):
    pass

class My(Log, NewApi):
    pass

class You(Log, Api):
    pass

my = My()
my.get()
print(my.__class__.__mro__)
print(Log.__mro__)


o = You()
o.get()
