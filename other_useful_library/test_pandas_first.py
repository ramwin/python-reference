#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas


df = pandas.DataFrame({
    "name": ["alice", "bob", "chile"],
    "age": [18, 19, 20],
})


a = df[df.age>=19].iloc(0)[0:1]
print("a", a.empty)
b = df[df.age>=29].iloc(0)[0:1]
print("b", b.empty)
