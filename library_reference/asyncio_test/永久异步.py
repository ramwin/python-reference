#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import logging
import random
import time

import colorlog
from redis import Redis


handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    "%(asctime)s %(log_color)s%(levelname)s:%(name)s:%(message)s"
    ))
logging.basicConfig(level=logging.INFO, handlers=[handler])


LOGGER = logging.getLogger(__name__)
background_tasks = set()


async def slow(duration):
    start = time.perf_counter()
    LOGGER.info("handler: %s", duration)
    await asyncio.sleep(duration)
    LOGGER.info("handle: %s done", duration)
    return time.perf_counter() - start


async def main():
    """
    create_task不wait不继续执行
    """
    LOGGER.info("main")
    for i in range(100):
        task = asyncio.create_task(slow(random.random()))
        background_tasks.add(task)
        task.add_done_callback(background_tasks.discard)


async def main2():
    """
    create_task不wait不继续执行
    """
    LOGGER.info("main")
    loop = asyncio.get_event_loop()
    for i in range(100):
        task = loop.create_task(slow(random.random()))
    loop.run_forever()


async def main3():
    """使用done"""
    client = Redis()
    tasks = []
    while True:
        LOGGER.info("循环开始")
        key_sleep = client.blpop('list', timeout=1)
        if key_sleep:
            starttime = time.perf_counter()
            task = asyncio.create_task(slow(float(key_sleep[1])))
            tasks.append((starttime, task))
            LOGGER.info("创建任务: %s", task)
        await asyncio.sleep(0.01)
        for starttime, task in tasks:
            if task.done():
                duration = await task
                tasks.remove((starttime, task))
                LOGGER.info("外部耗时: %f, 内部耗时: %f", time.perf_counter() - starttime, duration)



if __name__ == "__main__":
    asyncio.run(main3())
