**Xiang Wang @ 2019-07-02 10:04:45**

### asyncio
[官网](https://docs.python.org/3/library/asyncio.html)
[测试代码](../test/asyncio_test.py)
#### Hello World!
```
async def main():
    print("Hello World")
    await asyncio.sleep(1)
    print("... World!")
```

#### [Coroutines and Tasks][Coroutines and Tasks]
[测试代码](./asyncio_test/coroutine_test.py)
* 官网文档

```
>>> import asyncio

>>> async def main():
...     print('hello')
...     await asyncio.sleep(1)
...     print('world')

>>> asyncio.run(main())
hello
world
```
注意，如果仅仅调用`main()`, 只会返回一个coroutine object, 而不会被执行. 执行协程的方式有三种
1. 使用`asyncio.run()`直接调用协程
2. await一个coroutine. 这样coroutine就会执行(同步). await必须用在async函数里面
```
async def say_after(delay, what):
    await asyncio.sleep(delay)
async def main():
    await say_after(1, "hello")  # 先花1秒执行完
    await say_after(2, "world")  # 再花2秒执行完，一共耗时3秒
```
3. 使用`asyncio.create_task()` 来同时执行多个协程
```
async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")
```

#### Awaitables
如果await可以用于某个Object,那么这个object就是awaitable的. 主要的有三种， Coroutines, Tasks, Futures
* Coroutines
这里coroutine代表
    1. 一个coroutine function: async def function
    2. 一个coroutine object: 调用cotoutine function返回的对象
* Tasks
可以同时执行的coroutines, 通过`asyncio.ccreate_task()`来调用，并且会立刻执行
* [ ] Futures

#### Running an asyncio Program
直接运行一个asyncio程序
```
asyncio.run(coro, *, debug=False)
```

[Coroutines and Tasks]: https://docs.python.org/3/library/asyncio-task.html
