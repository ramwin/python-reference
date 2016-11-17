#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-11-09 19:54:05

def A(object):
    def __init__(self, number):
        self.number = number

    def __gt__(self, b):
        return self.number > b.number


import heapq
a = []
heapq.heappush(a, A(1))
heapq.heappush(a, A(2))
