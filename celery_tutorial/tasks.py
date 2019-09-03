#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-01-18 10:19:10


from celery import Celery
import time
app = Celery(
    'tasks',
    )

app.config_from_object('celeryconfig')


@app.task
def add(x, y):
    time.sleep(x+y)
    return x + y


