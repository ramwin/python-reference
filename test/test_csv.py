#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Xiang Wang @ 2018-11-20 11:00:50
from __future__ import unicode_literals
import csv
from collections import OrderedDict
import time

def f():
    fieldnames = OrderedDict((
        ("name", "姓名"),
        ("company", "公司名称"),
        ("gb_classfication1", "国标一级分类"),
        ("gb_classfication2", "国标二级分类"),
        ("gb_classfication3", "国标三级分类"),
        ("sw_classfication1", "国标一级分类"),
        ("sw_classfication2", "国标二级分类"),
        ("sw_classfication3", "国标三级分类"),
        ("keywords", "关键词"),
        ("introduction", "简介"),
    ))
    filename = "{name} {time}.csv".format(
        name="圈子名称",
        time=time.strftime("%Y-%m-%d %H:%M:%S"),
    )
    with open("/tmp/tmp2", "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames.keys())
        writer.writerow(fieldnames)


if __name__ == '__main__':
    f()
