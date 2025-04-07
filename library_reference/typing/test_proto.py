#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


from typing import Protocol, ClassVar


class Person:
    type: ClassVar[str]

    def __init__(self, name: str):
        self.name = name

    def say(self) -> None:
        print(f"我是{self.type}, 我叫{self.name}")


class Student(Person):
    type = "学生"


class Teacher(Person):
    type = '老师'


if __name__ == "__main__":
    Student("alice").say()
