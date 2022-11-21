#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>

"""测试shift"""


import pandas


data_frame1 = pandas.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
    index=[0, 1, 2, 3]
)


print(data_frame1)
data_frame1["E"] = data_frame1["D"].shift(periods=2, axis="index", fill_value=0)
print(data_frame1)
