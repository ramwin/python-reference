#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
测试typing literal
"""


from typing import Literal


def use_literal(a: Literal['r', 'w']):
    """
    测试typing literal
    """
    print(a)
    if a == 'e':
        print(a)
    return a


use_literal('c')
