#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time

from functools import partial
from threading import Timer


global_state = {}


def call(task_id, long):
    global_state.pop(task_id, None)
    print("真的执行了", long)
    time.sleep(long)
    print("真的执行完毕了", long)


def cal(task_id, *args, **kwargs):
    task = global_state.get(task_id, None)
    if task:
        task.cancel()
    global_state[task_id] = Timer(
        1, partial(call, task_id, *args, **kwargs)
    )
    global_state[task_id].start()


def main():
    cal("task1", 1)
    cal("task1", 2)
    cal("task2", 3)
    time.sleep(3)
    cal("task1", 2)
    cal("task1", 1)
    cal("task2", 3)


main()
