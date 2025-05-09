#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
import time

import redis


client = redis.Redis(decode_responses=True)


def wait_and_execute(*args, **kwargs):
    key = json.dumps([
        args, kwargs
    ])
    client.hset("wait_and_execute", key, 1)
    time.sleep(1)
    if not client.hdel("wait_and_execute", key):
        return
    print("真的执行了", args, kwargs)


wait_and_execute()
