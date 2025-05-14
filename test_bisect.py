#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from portion import closed
from portion.interval import Interval


class BisectStrategy:

    def __init__(self, duration: Interval, step):
        self.duration = duration
        self.step = step

    def check(self, value) -> bool:
        return 

    def get_first_error(self):
        if self.check(self.duration.lower) is False:
            return self.duration.lower
        while True:
            middle = self.get_middle()
            middle_result = self.check(middle)
            if middle_result is False:
                self.duration = closed(self.duration.lower, middle)
            else:
                self.duration = closed(middle, self.duration.upper)
            if (self.duration.upper - self.duration.lower) <= self.step:
                return self.duration.upper

    def get_middle(self):
        return (self.duration.lower + self.duration.upper) // 2

    def check(self, value):
        if value < 5:
            return True
        return False


print(BisectStrategy(closed(3, 10), 1).get_first_error())
