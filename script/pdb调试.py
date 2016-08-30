#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-08-30 11:40:36

import pdb


def main():
    sum = 0
    for i in range(100):
        if i==50:
            pdb.set_trace()
        sum += i
        print(i)


if __name__ == '__main__':
    main()
