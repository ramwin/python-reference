#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-06-03 15:55:46

country = "中国"

class AmeStudent(object):
    __country = "美国"  # 使用__来避免被外部直接修改

    @classmethod
    def get_country(cls):
        return cls.__country

    def set_country(self, country):  # 即使修改了，也没有用
        self.__country = country
