#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import logging
import random
import time

from multiprocessing import Pool

from redis import Redis


LOGGER = logging.getLogger(__name__)


class DelayBuyFastSet:
    """
    this class will read data from redis periodly and keep data in memory
    usage:

        WATCHING_USERS = DelayBuyFastSet(Redis(), key="WATCHING_USERS", timeout=5)
        "123" in WATCHING_USERS  # False
        WATCHING_USERS.add("123")
        "123" in WATCHING_USERS  # True

        WATCHING_USERS = DelayBuyFastSet(Redis(), key="WATCHING_USERS", timeout=5)
        "123" in WATCHING_USERS  # True
    """

    def __init__(self, redis_client, key, timeout):
        assert redis_client.get_encoder().decode_responses is True

        self.redis_client = redis_client
        self.value_key = f"{key}:value"
        self.version_key = f"{key}:version"

        self.timeout = timeout
        self.expire_at = time.perf_counter() + random.random() * timeout

        self._value = set()
        self.version = 0
        self.refresh()

    def __contains__(self, value):
        self.refresh_in_need()
        return str(value) in self._value

    def refresh_in_need(self):
        if time.perf_counter() < self.expire_at:
            return
        self.expire_at = time.perf_counter() + timeout
        if int(self.redis_client.get(self.version_key) or 0) == self.version:
            return
        self.refresh()

    def refresh(self):
        self._value = self.redis_client.smembers(self.value_key)
        self.version = self.redis_client.incr(self.version_key)

    def add(self, value: str):
        assert isinstance(value, str)
        self._value.add(value)
        added, version = self.redis_client.pipeline()\
                .sadd(self.value_key, value)\
                .incr(self.version_key)\
                .execute()


def test_performance(taskid: int):
    size = 10000
    Redis().delete("set_fastkey:value")
    Redis().delete("set_fastkey:version")
    Redis().delete("set_direct")
    a = DelayBuyFastSet(redis_client=Redis(decode_responses=True), key="set_fastkey", timeout=5)
    for i in range(0, size, 2):
        a.add(str(i))

    start = time.perf_counter()
    b = DelayBuyFastSet(redis_client=Redis(decode_responses=True), key="set_fastkey", timeout=5)
    cnt = 0
    for j in range(0, size, 3):
        if str(j) in b:
            cnt += 1
    end = time.perf_counter()
    LOGGER.info("任务 %d 的间接使用速度: %f, 结果: %d", taskid, end - start, cnt)

    client = Redis(decode_responses=True)
    for i in range(0, size, 2):
        client.sadd("set_direct", str(i))

    start = time.perf_counter()
    cnt = 0
    for j in range(0, size, 3):
        if client.sismember("set_direct", str(j)):
            cnt += 1
    end = time.perf_counter()
    LOGGER.info("任务 %d 直接使用速度: %f, 结果: %d", taskid, end - start, cnt)


if __name__ == "__main__":
    import logging_config
    task_cnt = 2
    with Pool(task_cnt) as p:
        p.map(test_performance, range(task_cnt))
