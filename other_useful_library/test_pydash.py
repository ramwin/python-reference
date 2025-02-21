#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import itertools
import pydash
from pydash import py_


tasks = [
    { "user": "student", "task": "a" },
    { "user": "student", "task": "b" },
    { "user": "teacher", "task": "prea" },
    { "user": "teacher", "task": "posta" },
    { "user": "teacher", "task": "preb" },
    { "user": "teacher", "task": "postb" },
]

student_tasks = py_(tasks).filter({"user": "student"}).value()
teacher_task_group = py_(tasks)\
        .filter({"user": "teacher"})\
        .chunk(size=2)\
        .key_by(lambda x: x[0]["task"].lstrip("pre"))\
        .value()

print("student_tasks", student_tasks)
print("teacher_task_group", teacher_task_group)
# task_group = {
#         post["task"].lstrip('post'): (pre, post)
#         for (pre, post) in itertools.pairwise(teacher_tasks)
# }

for task in student_tasks:
    print(teacher_task_group[task["task"]])
