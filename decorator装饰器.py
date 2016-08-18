#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-08-18 09:21:05

def log(f):
    print('log')
    print(f.__name__)
    def fin(*args, **kwargs):
        return f(*args, **kwargs)
    return fin

@log
def main():
    ''' main __docstring__ '''
    print(1)


main()
print(main.__doc__)
