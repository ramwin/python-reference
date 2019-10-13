#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-09-09 17:15:59


import re


def main1():
    def rep(x):
        print(type(x))
        print(x)
        print(x.groups())
        return "结果"

    a = re.sub(r'\w{3}(\w{4})', rep, '18812345678')
    print(a)


if __name__ == "__main__":
    main1()
