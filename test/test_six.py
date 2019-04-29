#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-03-12 18:40:47


from __future__ import unicode_literals

import six
from six.moves import input as input_comp


if six.PY2:
    def input(prompt):
        raw = input_comp(prompt.encode("UTF-8"))
        return raw.decode("UTF-8")


name = input("输入您的名字")
print("您的名字是: {}".format(name))
