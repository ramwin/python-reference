#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import redis
import pendulum
from redis import Redis
from redis.cluster import RedisCluster

from eth_utils.address import to_checksum_address

REDIS = Redis(decode_responses=True)
CLUSTER = RedisCluster.from_url('redis://localhost:7000', decode_responses=True)
