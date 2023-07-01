#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import unittest


def setUpModule():
    print("模块执行前调用")


class Test2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("class2 之前调用")

    @classmethod
    def tearDownClass(cls):
        print("class2 之前调用")

    def test2(self):
        print("Test2.test2")

    def test1(self):
        print("Test2.test1")


class Test1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Test1.class 之前调用")

    @classmethod
    def tearDownClass(cls):
        print("Test1.class 之前调用")

    def test2(self):
        print("Test1.test2")

    def test1(self):
        print("Test1.test1")


def tearDownModule():
    print("模块执行后调用")

