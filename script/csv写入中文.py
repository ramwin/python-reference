#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2019-01-08 18:21:44


import csv
from collections import OrderedDict

fieldnames = OrderedDict([
    ("name", "姓名"),
    ("age", "年龄"),
])
rows = [
    {"name": "王祥", "age": 28},
    {"name": "测试", "age": 28},
]

with open("/tmp/test.csv", "w") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames.keys())
    writer.writeheader()
    writer.writerow(fieldnames)
    for row in rows:
        writer.writerow(row)
