#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import redis
import pendulum
from redis import Redis, RedisCluster

from eth_utils.address import to_checksum_address
from hexbytes import HexBytes
from humanfriendly import *

REDIS = Redis(decode_responses=True)
try:
    CLUSTER = RedisCluster.from_url("redis://localhost:7000/", decode_responses=True)
except RedisClusterException as error:
    CLUSTER = None
