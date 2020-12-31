#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2020-12-25 16:12:16


import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    start = time.time()
    print(f"started at {start}")
    task1 = asyncio.create_task(
        say_after(1, "hello"))
    task2 = asyncio.create_task(
        say_after(2, "world"))
    await task1
    print(f'task1 finished at {time.time() - start}')
    await task2
    print(f'task2 finished at {time.time() - start}')
    print(f"finished at {time.time()}")


asyncio.run(main())
