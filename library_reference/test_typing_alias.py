#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


from typing import NewType


Age = NewType("Age", int)


def grow(age: Age) -> Age:
    # return age + 1  # 这样是报错的
    # return age + Age(1)  # 这样也不行
    return Age(age + 1)  # 这样才可以
