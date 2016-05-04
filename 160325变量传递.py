#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-03-25 11:57:17

def main(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)
def alllist(*args):
    for i in args:
        print(i)
def main1(name='默认不穿参数'):
    print(name)
if __name__ == '__main__':
    print('直接把变量的数值传进去')
    main('string','index0','index1',key='value')
    print('把list和dict对象传进去')
    string = 'string'
    list0 = ['index0','index1']
    dict0 = {'key':'value'}
    main(string,  *list0, **dict0)
    alllist(1,2,3)
    main1()
    main1('传递了参数')
