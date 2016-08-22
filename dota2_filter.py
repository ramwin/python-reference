#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-08-07 04:59:02


def main():
    """
        有时候在dota2的聊天窗口里面想要屏蔽某个人，但是找不到他的ID，就运行这个
    """
    name = input("输入要屏蔽的用户名称(其实只要第一个汉字):")
    number = int(ord(name[0]))
    while True:
        name = input("输入当前你看到的用户名称(其实只要第一个汉字):")
        number2 = int(ord(name[0]))
        if number2 > number:
            print('用户在上面 %d行' % ((number2-number)/100))
        if number2 < number:
            print('用户在下面 %d行' % (-(number2-number)/100))


if __name__ == '__main__':
    main()
