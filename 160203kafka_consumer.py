#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-02-03 11:23:44

from kafka import KafkaConsumer
consumer = KafkaConsumer('test',bootstrap_servers='192.168.1.191')
for msg in consumer:
    print(msg)

