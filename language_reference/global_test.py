#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-12-28 15:41:56

global a
a = 0
b = 0
def add():
    print("add()")
    global a
    a += 1
    c = b
    print("b", b)
    c += 1
    print('a', a)
    print('c', c)

def add_without_global():
    print("add_without_global")
    print("a", a)
    a += 1 # 如果没有设置global，就只能用a而不能操作a
    print("a", a)

def show():
    print("show()")
    print('a', a)
    print('b', b)


def main():
    add()
    add()
    # add_without_global()
    show()


if __name__ == '__main__':
    main()
