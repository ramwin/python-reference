#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
测试typing
"""


from typing import List


def add(number: int) -> int:
    """
    数据加1返回
    """
    number = number + 1
    return "123"


def adds(numbers: List[int]) -> List[int]:
    for i in numbers:
        add(i)
