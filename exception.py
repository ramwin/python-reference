#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-08-19 11:00:43

try:
    1/0
except Exception as e:
    print(dir(e))
    print(e)
