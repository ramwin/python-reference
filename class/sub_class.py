#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


class A:
    name = "A"
    double_name = "AA"

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.double_name = cls.name * 2


class B(A):
    name = "B"


print(B.double_name)
