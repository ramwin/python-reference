#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-07-02 10:25:53


import time
import asyncio

async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')


async def say_after(delay, what):
    print(f"calling say_after {delay} {time.strftime('%X')}")
    await asyncio.sleep(delay)  # 执行到这一步就会卡住，直到外层调用await
    print(f"before sleep {delay} {time.strftime('%X')}")
    time.sleep(delay)
    print(f"after sleep {delay} {time.strftime('%X')}")
    print(what)
    print(f"finished calling say_after {delay} {time.strftime('%X')}")


async def main2():
    print(f"started at {time.strftime('%X')}")
    b = say_after(1, "hello")
    await b
    print(f"finished at {time.strftime('%X')}")


async def main3():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))
    task2 = asyncio.create_task(
        say_after(2, 'world'))
    print(f"started at {time.strftime('%X')}")
    await task2
    await task1
    print(f"finished at {time.strftime('%X')}")


def main4():
    """直接调用协程"""
    asyncio.run(say_after(1, 2))

def service():
    return say_after(1, 'service调用')

async def main5():
    """async函数调用普通函数调用async函数"""
    await service()
