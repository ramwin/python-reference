#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import subprocess

from pathlib import Path


def main():
    if not Path(".git").exists():
        return
    res = subprocess.run(["git", "branch", "--show-current"], capture_output=True)
    print("[" + res.stdout.decode('utf8').strip() + "]")


if __name__ == "__main__":
    main()
