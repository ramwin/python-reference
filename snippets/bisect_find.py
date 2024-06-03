#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


from portion import closed, Interval


class BisectBlame:
    """用二分法找到一个错误的东西"""

    def __init__(self, duration: Interval, step):
        self.duration = duration
        self.step = step
        if not self.has_error(duration):
            raise ValueError("不存在错误")

    def has_error(self, duration) -> bool:
        """判断某个范围是否有错误"""
        raise NotImplementedError

    def find_first_error(self, duration=None) -> Interval:
        """找到第一个报错的范围"""
        if duration is None:
            duration = self.duration
        if (duration.upper - duration.start) <= self.step:
            return duration
        middle_value = self.get_middle(duration)
        if self.has_error(closed(duration.lower, middle_value)):
            return self.find_first_error(closed(duration.lower, middle_value))
        return self.find_first_error(closed(middle_value, duration.upper))

    def get_middle(self, duration):
        """返回中间的数字"""
        return (duration.lower + duration.upper) // 2
