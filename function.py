#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-03-25 11:57:17


def main(name, age, height=2.2, sex='F', *args,**kwargs):
    print("name: {}".format(name))
    print("age: {}".format(age))
    print("height: {}".format(height))
    print('args: {}'.format(args))
    print('kwargs: {}'.format(kwargs))

if __name__ == '__main__':
    main('name', 'age', '2.2', 2, 'china', 'ew', key='key')
