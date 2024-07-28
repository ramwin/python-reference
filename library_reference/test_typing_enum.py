#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


from enum import Enum

from hexbytes import HexBytes


class Hex(Enum):
    a = HexBytes("A")
    b = HexBytes("B")
    c = HexBytes("c")
    d = HexBytes("d")
    e = HexBytes("e")
    f = HexBytes("f")


def get() -> Hex:
    t = HexBytes("c")
    if t == Hex.c:
        print("=")
    return Hex.c
