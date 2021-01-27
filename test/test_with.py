#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2021-01-27 15:55:25


class A():

    def __enter__(self):
        print('enter')

    def __exit__(self, exc_type, exc_value, traceback):
        print(f'exc_type: {exc_type}')
        print(f'exc_value: {exc_value}')
        print(f'traceback: {traceback}')
        print('exist')


with A():
    print('start')
    raise Exception('value')
