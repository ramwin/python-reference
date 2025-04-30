#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-08-30 14:29:31

import string
import datetime

for letter in string.ascii_letters:
    style = "%" + letter
    print(style + ":" + datetime.datetime.now().strftime(style))
