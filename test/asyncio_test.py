#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-07-02 09:54:30

import time
import asyncio


@asyncio.coroutine
def slow_function(x):
    print("调用慢函数")
    # time.sleep(1)
    yield from asyncio.sleep(1)
    print("慢函数执行完毕")

async def slow_function2(x):
    print("调用慢函数2")
    r = await asyncio.sleep(1)
    print("慢函数2执行完毕")


async def main():
    print("Hello World")
    await asyncio.sleep(1)
    print("... World!")

if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # tasks = [slow_function2(1), slow_function2(2)]
    # loop.run_until_complete(asyncio.wait(tasks))
    # loop.close()
    task1 = main()
    task2 = main()
    asyncio.run(main())
    asyncio.run(main())
