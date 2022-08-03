#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import csv
from csv import Dialect, QUOTE_ALL


class MyDialect(Dialect):
    delimiter = ";"
    quotechar = "%"
    quoting = QUOTE_ALL
    lineterminator = "end\r\n"


with open("test_dialect.csv", "w") as csvfile:
    fieldnames = ["name", "age"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect=MyDialect)
    writer.writeheader()
    writer.writerow({"name": "张三", "age": 18})
