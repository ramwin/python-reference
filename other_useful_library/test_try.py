#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from reretry import retry


def ignore(*args, **kwargs):
    print("ignore")


@retry(Exception, tries=1, delay=0, fail_callback=ignore)
def make_trouble():
    print('error')
    raise ValueError


make_trouble()
make_trouble()
