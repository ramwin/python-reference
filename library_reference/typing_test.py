#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
测试typing
"""


from typing import List, Union


def add(number: int) -> int:
    """
    数据加1返回
    """
    number = number + 1
    return "123"


def adds(numbers: List[int]) -> List[int]:
    """每个数据+1"""
    for i in numbers:
        add(i)


class User:
    """用户"""

    def __init__(self, _id):
        self._id = _id


def get_user(userid: int) -> Union[User, None]:
    """根据id返回用户或者None"""
    if userid <= 0:
        return None

    return User(userid)
