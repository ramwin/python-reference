#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-12-09 11:32:19

from ics import Calendar, Event

c = Calendar()
e = Event()
e.name = "My cool event"
e.begin = '20161212 00:00:00'
c.events.append(e)
print(str(c))
with open("test.ics", "w") as f:
    f.writelines(c)
