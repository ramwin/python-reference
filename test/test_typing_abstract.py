#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from abc import abstractmethod
from typing import Protocol, ClassVar


class A(Protocol):
    info: ClassVar[dict]


class B(A):
    pass


class C(A):
    info = []
