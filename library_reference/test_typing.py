#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
"""

from typing import Tuple, Dict


def get() -> Dict[int, int]:
    return {
        1: '2'
    }

def main():
    a = get()
    print(a.keys())
    
    
main()