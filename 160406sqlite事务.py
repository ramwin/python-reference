#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-04-06 11:29:08

import datetime
import sqlite3

file_path = './test.db'
def main():
    conn = sqlite3.connect(file_path)


if __name__ == '__main__':
    main()
