#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time
from decimal import Decimal
from typing import Union, overload


def process(x: Union[int, float, Decimal]) -> Union[int, float, Decimal]:
    return x + 1


# def error() -> None:
#     a = Decimal(1)
#     b = process(a)
#     print(b.scaleb(10))  # 这里会报错, "int | float | Decimal" 没有scaleb属性


@overload
def overload_process(x: int) -> int:
    ...


@overload
def overload_process(x: float) -> float:
    ...


@overload
def overload_process(x: Decimal) -> Decimal:
    ...


def overload_process(x):
    return x + 1


def right() -> None:
    # a = Decimal(1)
    a = time.time()
    b = overload_process(a)
    print(b.scaleb(10))  # 这里会报错, "int | float | Decimal" 没有scaleb属性
