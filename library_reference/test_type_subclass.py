#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
如何指定新的类
"""


from dataclasses import dataclass
from typing import cast


class Model:
    id: int


class Student(Model):
    name: str


class Teacher(Model):
    id: int
    level: int


class Task:
    MODEL_CLASS = Model

    def __init__(self, instance: Model):
        self.instance = instance

    def go_to_classrooom(self) -> str:
        raise NotImplementedError


class StudentTask(Task):
    MODEL_CLASS = Student

    def go_to_classrooom(self) -> str:
        print(self.instance.id)  # 这个不会报错
        print(self.instance.name)  # 这个会报错
        assert isinstance(self.instance, self.MODEL_CLASS)
        print(self.instance.name)  # 这个不会报错


class StudentTask2(Task):
    MODEL_CLASS = Student

    def __init__(self, instance: Student):
        super().__init__(instance)

    def go_to_classrooom(self) -> str:
        print(self.instance.id)  # 这个不会报错
        print(self.instance.name)  # 这个会报错
        assert isinstance(self.instance, self.MODEL_CLASS)
        print(self.instance.name)  # 这个不会报错
        return self.instance.name
