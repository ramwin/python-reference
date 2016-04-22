#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-01-03 21:10:49

def main():
    try:
        1/0
    except ZeroDivisionError:
        print('不能除以0')
    except Exception as err:
        print(err)
if __name__=='__main__':
    main()
