#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-03-22 17:56:24


import unittest
from week import Week
import datetime


class TestWeekMethods(unittest.TestCase):

    def test_week(self):
        self.assertEqual(Week(2010, 10).get_year_week(), '201010')

    def test_create_from_date(self):
        self.assertEqual(Week(2017, 1),
                         Week.create_from_date(datetime.date(2017,1,2)))

    def test_startdate(self):
        self.assertEqual(Week(2017, 1).startdate,
                         datetime.date(2017, 1, 2))

    def test_startdatetime(self):
        self.assertEqual(Week(2017, 1).startdatetime,
                         datetime.datetime(2017, 1, 2))


if __name__ == '__main__':
    unittest.main()
