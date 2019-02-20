#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2018-10-16 10:36:48

import traceback

def another_function():
    lumberstack()

def lumberstack():
    traceback.print_stack()
    print(repr(traceback.extract_stack()))
    print(repr(traceback.format_stack()))
    a = "".join(traceback.format_stack())
    print("\n\n得到的traceback: ========== ")
    print(a)

another_function()
