#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
测试Pandas
"""


import logging
import pandas


logging.basicConfig(level=logging.INFO)
data_frame1 = pandas.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
    index=[0, 1, 2, 3]
)


data_frame4 = pandas.DataFrame(
    {
        "B": ["B2", "B3", "B6", "B7"],
        "D": ["D2", "D3", "D6", "D7"],
        "F": ["F2", "F3", "F6", "F7"],
    },
    index=[2, 3, 6, 7],
)


def test_merge():
    logging.info("data_frame1: \n%s", data_frame1)
    logging.info("data_frame4: \n%s", data_frame4)
    result = pandas.concat([data_frame1, data_frame4], axis=1, join="inner", on="B")
    logging.info("result: \n%s", result)


if __name__ == "__main__":
    test_merge()
