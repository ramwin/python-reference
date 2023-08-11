#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import jmespath


def test1():
    data = {"foo": {"bar": {"name": "one"},
                    "baz": {"name": "two",
                            "key": "value",
                            }}}
    print(jmespath.search("*.*.key", data))


test1()
