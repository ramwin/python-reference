#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-08-18 09:21:05

# 基础用法
# def log(f):
#     print('log')
#     print(f.__name__)
#     def fin(*args, **kwargs):
#         return f(*args, **kwargs)
#     return fin
# 
# @log
# def main():
#     ''' main __docstring__ '''
#     print(1)


# main()
# print(main.__doc__)

from functools import update_wrapper
## 但是这样 docstring就变了
def log(f):
    print('log')
    print(f.__name__)
    def fin(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            return '出现错误, 但是我不告诉你错误是什么'
    return update_wrapper(fin, f)

@log
def main():
    """ main docstring """
    print(1)

main()
print(main.__doc__)
