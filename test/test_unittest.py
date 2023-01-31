#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>



import unittest


class MyTest(unittest.TestCase):

    def after(self, *args, **kwargs):
        print(args)
        print("after")

    def test_raise(self):
        self.addCleanup(self.after, 1, 2)
        with self.assertRaises(ZeroDivisionError):
            1/2
        print("测试完毕")

    def test_divide_zero(self):
        self.addCleanup(self.after, 1, 2)
        with self.assertRaises(ZeroDivisionError):
            1/0
        print("测试完毕")


if __name__ == "__main__":
    unittest.main()
