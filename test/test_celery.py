#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time

from celery import Celery


app = Celery('tasks', broker="redis://localhost")


@app.task
def add(x, y):
    time.sleep(4)
    if x == y:
        raise Exception(x, y)
    print("调用add", x, y)
    return x + y
