#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-09-29 16:04:37

"""
"""
import random

class Item(object):
    def __init__(self):
        self.level = 0
        self.cost = 0
        self.probability = {
            0: 0.8,
            1: 0.7,
            2: 0.6,
            3: 0.5,
            4: 0.4,
        }
    def upgrade(self):
        self.cost += 1
        success = random.random() < self.probability[self.level]
        if success:
            self.level += 1
        else:
            self.level -= 2
            if self.level < 0:
                self.level = 0

total = 0
for i in range(1000000):
    i = Item()
    while i.level != 5:
        i.upgrade()
    total += i.cost
print(total/1000000)
