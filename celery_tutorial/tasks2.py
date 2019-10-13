#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-01-18 10:19:10


from celery import Celery
import time
app = Celery(
    'tasks2',
    )

app.config_from_object('celeryconfig')

# a = list(range(100000)) celery运行时，里面的a是共享的．不会额外占用４倍内存
# b = list(range(100000))
# c = list(range(100000))
# d = list(range(100000))


@app.task
def add(x, y):
    time.sleep(x+y)
    return x + y


