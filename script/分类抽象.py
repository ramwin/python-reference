#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-12-19 15:44:29

import pprint
import csv
import json
from collections import OrderedDict


file_name = 'type.csv'


class Industry(object):
    """代表了行业的类"""
    def __init__(self, name, code, pattern=None, parent=None):
        self.name = name.strip()
        self.code = code
        self.parent = parent
        self.pattern = pattern  # 这个值你可以暂时不管
        self.children = []

    def has_child(self, industry):
        """self的children里面是存在code和industry的code一致的元素"""
        for i in self.children:
            if i == industry:
                return True
        else:
            return False

    def has_generation(self, industry):
        """self的children， children的children里面是否存在和industry的code一致的元素"""
        pass

    def contains(self, industry):
        """判断一个industry是否属于self"""
        if self.parent is None:
            return industry.ancestor == self
        else:
            return industry.code.startswith(self.code)

    def contains_directly(self, industry):
        """判断一个industry是不是直接隶属于self"""
        if not self.contains(industry):
            return False
        if self.parent is None:
            if len(industry.code) == 2:
                return True
            else:
                return False
        else:
            return len(industry.code)-1 == len(self.code)

    def get_next_level(self, industry):
        """返回self的children里面是industry的组辈的那个元素"""
        for i in self.children:
            if i.contains(industry):
                return i
        return None

    def get_next_level_of_industry(self, industry):
        """返回industry的父辈们，哪个应该是直接隶属于self的"""
        assert self.contains(industry)
        while True:
            if industry.parent == self:
                return industry
            else:
                return self.get_next_level_of_industry(industry.parent)

    def insert(self, industry):
        """把industry加入到self的children或者children的children里面"""
        print("把%s加入%s" % (industry, self))
        assert self.contains(industry)
        if self.contains_directly(industry):
            if self.has_child(industry):
                pass
            else:
                print("把%s加入%s的children"%(industry, self))
                industry.parent = self  # 有待商榷，内存泄露
                self.children.append(industry)
        else:
            next_level = self.get_next_level(industry)
            if next_level:
                next_level.insert(industry)
            else:
                self.children.append(self.get_next_level_of_industry(industry))

    @property
    def ancestor(self):
        if self.parent:
            return self.parent.ancestor
        else:
            return self

    def to_dict(self):
        """返回dict格式"""
        return {}

    def __str__(self):
        return self.name

    def __eq__(self, industry):
        return self.code == industry.code

    def to_dict(self):
        return {
            'code': self.code,
            'name': self.name,
            'pattern': self.pattern,
            'children': list(map(lambda x: x.to_dict(), self.children))
        }


def main():
    """把文件里面的excel格式转变成嵌套的json格式"""
    result = []
    reader = csv.DictReader(open(file_name))
    for index, row in enumerate(reader):
        industry = Industry(
            name=row['小类名称'], code=row['小类'], pattern=row['小类'],
            parent=Industry(
                name=row['中类名称'], code=row['中类'],
                pattern=row['中类']+'*',
                parent=Industry(
                    name=row['大类名称'], code=row['大类'],
                    pattern=row['大类'] + '*',
                    parent=Industry(
                        name=row['门类名称'], code=row['门类'])
                )
            )
        )
        for i in result:
            if industry.ancestor == i:
                i.insert(industry)
                break
        else:
            industry.ancestor.insert(industry)
            result.append(industry.ancestor)
    return result


if __name__ == '__main__':
    print("====starts=====")
    for index, i in enumerate(main()):
        print('index')
        pprint.pprint(i.to_dict(), indent=4)
    data = []
    for i in main():
        data.append(i.to_dict())
    with open('result.json', 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("===end===")
