#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from redis import Redis
from typing import Mapping, Union


client = Redis(decode_responses=True)
# client.set_response_callback("get", str)
a: str = client.get("foo")
print(a)
b: str = client.get("notexist")
print(b, type(b))
info: Mapping[Union[str, bytes], float] = {'pi': 3.14, b'ok': 4}
client.zadd('sortedset', info)
