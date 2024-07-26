#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import enum
from typing import Literal, NewType, TypeAlias


AGE = NewType("AGE", int)

YOUNG = AGE(18)

MIDDLE = AGE(38)

OLD = AGE(88)

# the next line will raise error Parameter 1 of Literal[...] is invalid

class Discount(enum.Enum):
    YOUNG = YOUNG
    OLD = OLD


def get_discount(age: Discount) -> float:
    if age == YOUNG:
        return 0.1
    elif age == OLD:
        return 0.9
    else:
        raise NotImplementedError


if __name__ == "__main__":
    print(get_discount(Discount.YOUNG))
    print(get_discount(MIDDLE))
