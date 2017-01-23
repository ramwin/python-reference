#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-01-18 10:19:10


from celery import Celery
import time
app = Celery('tasks', broker='redis://@203.166.189.102:20379/9')


@app.task
def add(x, y):
    time.sleep(100)
    return x + y
