#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>

import pandas as pd

df = pd.DataFrame(
    {'年龄': [21,22,23,24]},
    index=pd.Series(
        ['a张三', 'b李四', 'c王二', 'd麻子'],
        name='姓名'
    ),
    columns=["年龄"]
)

df['出生年份'] = 2025 - df['年龄']

print(df)
