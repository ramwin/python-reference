#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


from typing import NewType


Age = NewType("Age", int)

type MY_INT = int  # 3.10里面不加type


def grow(age: Age) -> Age:
    # return age + 1  # 这样是报错的
    # return age + Age(1)  # 这样也不行
    return Age(age + 1)  # 这样才可以


def test_alias(age: MY_INT) -> MY_INT:
    return age + 3


def main():
    print(test_alias(3))


if __name__ == "__main__":
    main()
