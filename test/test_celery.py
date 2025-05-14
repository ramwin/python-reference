#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time

from celery import Celery


app = Celery('tasks', broker="redis://localhost/")
app.conf.result_backend = "redis://localhost/"


@app.task(name="school.tasks.add")
def add(x):
    print("调用add")
    time.sleep(x)
    return x + 1


if __name__ == "__main__":
    r = add.delay(1)
    print(r.get())
