#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-05-30 17:13:00

import time
index = 0
while index<100:
    print('%d' % index, end='\r')
    time.sleep(0.1)
    index += 1
