#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-09-18 11:36:43

import datetime
from datetime import date


class Week(object):
    """
        默认设置每年的第一个周一开始为的第一周
        默认设置每周从周一开始，周日结束
    """
    def __init__(self, year, week):
        """
            year: 年份
            week: 第几周
        """
        assert 1970 < year < 9999
        assert 1 <= week <= 53
        self.year = year
        self.week = week

    @classmethod
    def create_from_date(cls, date_obj):
        """
            date: datetime.date
            example: week = Week.create_from_date(date(2016, 9, 18))
        """
        year = date_obj.year
        week = int(date_obj.strftime('%W'))
        if week == 0:
            date_obj=date(year-1,12,31)
            return cls.create_from_date(date_obj=date_obj)
        week_obj = cls(year=date_obj.year, week=week)
        return week_obj

    @property
    def startdate(self):
        new_years_day = date(year=self.year, month=1, day=1)
        startdate = new_years_day + \
                    datetime.timedelta(days=(7-new_years_day.weekday()) % 7) + \
                    datetime.timedelta(days=(self.week-1)*7)
        return startdate

    @property
    def enddate(self):
        enddate = self.startdate + datetime.timedelta(days=6)
        return enddate

    def __str__(self):
        return "%d年第%d周: %s~%s" % (self.year, self.week, self.startdate.strftime("%m月%d日"), self.enddate.strftime("%m月%d日"))


def main():
    a = Week(2016,1)
    print(a)
    b = Week.create_from_date(date(2016,9,18))
    print(b)
    c = Week.create_from_date(date(2016,1,1))
    print(c)


if __name__ == "__main__":
    main()
