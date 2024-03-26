#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


from typing import Union, overload, Literal


@overload
def process(parsed: Literal[True]) -> dict:
    ...

@overload
def process(parsed: Literal[False]) -> str:
    ...

def process(parsed: bool) -> Union[dict, str]:
    if parsed:
        return {}
    return ''


print(process(False).keys())
print(process(True).endswith("er"))
