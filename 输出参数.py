#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试shell的输入和输出
"""

import sys


def main(*args, **kwargs):
    """
    输出shell的输入和输出
    """
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")


if __name__ == "__main__":
    main(*sys.argv)
