#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2020-04-22 13:19:25


from threading import Thread


class A(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        self.name += self.name
        return self.name


def call(obj):
    import time
    time.sleep(3)
    print(obj)


def main():
    print("main 启动")
    a = A(name='name')
    thread = Thread(target=call, args=(a, ))
    thread.start()
    thread = Thread(target=call, args=(a, ))
    thread.start()
    print("main 结束")


if __name__ == '__main__':
    main()
