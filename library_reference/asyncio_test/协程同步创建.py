#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import time
import logging
import asyncio

import colorlog



handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    "%(asctime)s %(log_color)s%(levelname)s:%(name)s:%(message)s"
    ))
logging.basicConfig(level=logging.INFO, handlers=[handler])


LOGGER = logging.getLogger(__name__)


async def slow(task):
    await asyncio.sleep(0.01)
    LOGGER.info("处理任务: %s", task)
    LOGGER.info("等待0.1: %s", task)
    time.sleep(0.1)
    await asyncio.sleep(1)
    LOGGER.info("处理完毕: %s", task)

async def async_handle_single(task):
    return await slow(task)

async def use_task_group():
    tasks = list(range(20))
    LOGGER.info("开始处理")
    # TaskGroup会等待
    # async with asyncio.TaskGroup() as tg:
    #     LOGGER.info("创建了TaskGroup")
    #     for task in tasks:
    #         tg.create_task(async_handle_single(task))
    awaitables = [
        async_handle_single(task)
        for task in tasks
    ]
    LOGGER.info("创建完毕开始等待")
    time.sleep(1)
    for i in awaitables:
        await i
    LOGGER.info("处理完毕")


if __name__ == "__main__":
    asyncio.run(use_task_group())
