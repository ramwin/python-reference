#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from typing import List, Union, Iterable


def show(keys: Iterable[str]) -> None:
    for i in keys:
        print(i)


def main() -> None:
    show(["1", "2"])
    show({
        "a": 123,
        }.keys())


if __name__ == "__main__":
    main()
