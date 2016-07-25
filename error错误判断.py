#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-01-03 21:10:49


# 输出错误的行数
try:
    1/0
except:
    traceback.print_exc()
def main():
    '''错误判断的方法'''
    try:
        1/0
    except ZeroDivisionError:
        print('不能除以0')
    except Exception as err:
        print(err)
# def main2():
#     '''python2 的用法'''
#     try:
#         1/0
#     except Exception,e:
#         print e.message
def main3():
    '''python3 的用法, 最新版本的2也支持。'''
    try:
        1/0
    except Exception as err:
        print(err)

# 自定义错误
class TestError(Exception):
    def __init__(self, name):
        self.name = name
        pass
    def str(self):
        return '自定义的错误 %s'%(self.name)
raise TestError('error')
