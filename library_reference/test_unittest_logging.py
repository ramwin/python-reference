#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import logging
import unittest


logging.basicConfig(filename="test_unittest_logging.log", level=logging.DEBUG)
logging.warning("测试")
file_handler = logging.FileHandler(filename="test_unittest_logging2.log")
file_handler.setLevel(logging.DEBUG)
logging.getLogger("unittest").warning("开始")
logging.getLogger("unittest").addHandler(file_handler)


class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(1, 0)


if __name__ == "__main__":
    unittest.main()
