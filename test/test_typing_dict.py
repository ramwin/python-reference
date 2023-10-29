#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


from typing import TypedDict


class Point2D(TypedDict):
    x: int
    y: int
    label: str


a: Point2D = {'z': 1, 'label': 2}
