#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from pathlib import Path


def main():
    p = Path("mode")
    for i in [0o777, 0o111, 0o444, 0o000, 0o222]:
        p.joinpath(oct(i)).mkdir(mode=i, exist_ok=True)


main()
