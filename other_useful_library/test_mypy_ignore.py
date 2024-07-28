#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
各种mypy的忽略方式
"""


def test() -> int:
    """
    测试
    """
    a: int = '3'  # type: ignore[assignment]
    b: int = '4' # type: ignore[assignment]  # 忽略
    return a + b
