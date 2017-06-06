#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-06-06 13:28:49


class Base(object):
    def get(self):
        print('Base')


class Upper(Base):
    pass


class Other(object):
    def get(self):
        print('Other')


class Me(Base, Other):
    pass


a = Me()
a.get()
