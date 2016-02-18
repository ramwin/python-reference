#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-02-03 11:23:44

from kafka import SimpleProducer, SimpleClient
kafka_client = SimpleClient('192.168.1.191')
kafka_producer = SimpleProducer(kafka_client, async=False)
kafka_producer.send_messages('test',b'test')
