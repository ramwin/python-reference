#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import redis
from redis import Redis, RedisCluster

from eth_utils.address import to_checksum_address

REDIS = Redis(decode_responses=True)
REDIS_CLUSTER = RedisCluster(decode_responses=True, host="localhost", port=7000)
