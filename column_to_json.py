#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-12-19 15:44:29

import pprint


file_name = 'type.csv'


class Industry(object):
    """代表了行业的类"""
    def __init__(self, name, code, pattern, parent=None):
        self.name = name
        self.code = code
        self.parent = parent
        self.pattern = pattern  # 这个值你可以暂时不管
        self.children = []

    def has_child(self, industry):
        """self的children里面是存在code和industry的code一致的元素"""
        pass

    def has_generation(self, industry):
        """self的children， children的children里面是否存在和industry的code一致的元素"""
        pass

    def insert(self, industry):
        """把industry加入到self的children里面"""

    ...其他函数自己想，需要什么叫什么...

def main():
    """把文件里面的excel格式转变成嵌套的json格式"""
    result = []
    ...自己处理啦...
    return result


if __name__ == '__main__':
    pprint.pprint(main(), indent=4, depth=4)
