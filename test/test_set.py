#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""测试set"""


import random


class A:
    """测试自定义类的set"""

    def __hash__(self):
        """hash是用来给set定位的, 知道保存数组的位置"""
        # return 1
        # 所以如果你的hash返回的不一致, 一定都保存. 如果hash返回的一致, 根据 __eq__ 判断
        result = random.randrange(1, 3)
        print(f"调用A.hash = {result}")
        return result

    def __eq__(self, other):
        """eq是用来直接判断是否是同一个数组的"""
        return True


a = {A(), A()}

print(a)
