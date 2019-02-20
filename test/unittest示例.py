#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-02-20 16:35:39


import unittest


class MyTest(unittest.TestCase):

    def test_divide_zero(self):
        with self.assertRaises(ZeroDivisionError):
            1/0
            pass


if __name__ == "__main__":
    unittest.main()
