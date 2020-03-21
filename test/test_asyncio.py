#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2020-03-21 21:56:42

import time

import asyncio
import os


url1 = "https://ramwin.com:8888"
url2 = "https://ramwin.com:3306"



async def main():
    print("开始执行")
    asyncio.create_task(
        write(path1)
    )
    asyncio.create_task(
        write(path2)
    )
    # await write(path1)
    # await write(path2)
    print("执行完毕")


print("开始")
start = time.time()
asyncio.run(main())
print("结束: {}".format(time.time() - start))

