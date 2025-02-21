#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


from typing import TypedDict, Optional
# NotRequired, 3.11才有


class Point2D(TypedDict):
    x: int
    y: int
    label: str


# a: Point2D = {'z': 1, 'label': 2}  # 这里会报错, x, y 缺少, z多了


class Student(TypedDict):
    student_id: NotRequired[int]
    name: str


alice: Student = {"name": "123"}
bob: Student = {"name": "123", "student_id": 3}
