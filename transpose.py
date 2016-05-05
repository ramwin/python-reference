#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-05-04 15:20:10

import os
def transposition(origin):
    result = []
    first = True
    for iline, line in enumerate(origin):
        for jcolumn, column in enumerate(line):
            if first:
                result.append([])
            result[jcolumn].append(column)
        first = False
    return result


if __name__ == '__main__':
    list1 = [
        [1,2,3], 
        [4,5,6]
    ]
    list2 = transposition(list1)
    print(list2)
