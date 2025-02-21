#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from typing import NewType, List, cast

from pydash import py_


def main(l: List[int]) -> int:
    return sum(l)


tasks = [1, 2, 3, 4, '5']

tasks2 = cast(List[int], py_(tasks).filter(lambda x: isinstance(x, int)).value())

print(main(tasks2))
