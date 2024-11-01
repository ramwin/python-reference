# [多进程multiprocessing](https://docs.python.org/3/library/multiprocessing.html)
* parent_process():
如果不是None, 说明是生成的子进程

## [Pool][pool]
* Pool.map只支持一个参数。 所以如果你是多个参数， 要用Pool.starmap
* Pool的进程是根据初始化来的，后续不会生成新的进程. 处理完任务后进程会从列表继续获取任务执行
```
from multiprocessing import Pool
with Pool() as pool:
    pool.map(function, taskslist)
    pool.imap_unordered(function, tasklist[, chunksize])  # chunksize可以让一个进程一次性多获取几个任务
    pool.starmap(function, [(arg1, arg2), (arg1, arg2)])
```

[测试](../multi/poll_test.py)
* Introduction
p.map返回一个列表. 执行的顺序是一定按照顺序来的
```
from multiprocessing import Pool
def f(x):
    return x * x
with Pool(5) as p:
    print(p.map(f, [1,2,3]))
```

### [imap_unordered](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.imap_unordered)
```{note}
imap_unordered返回的是迭代器，必须for一下才能一个个执行
```

```{note}
对iterable里面的每个元素执行func. chunksize代表每个进程执行的迭代次数。这样一个进程可以执行多次
```

[测试](./pool_chunksize.py)

```
with Pool() as p:
    for result in p.imap_unordered(func, iterable, chunksize):
        print(result)
```

## ThreadPool
[../test/test_thread_pool.py](../test/test_thread_pool.py)
```python
from multiprocessing.pool import ThreadPool

tasks = range(1, 4)
with ThreadPool() as p:
    results = p.map(f, tasks)  # [2, 3, 4]

print("如果有报错的情况，就拿不到结果了")
tasks = range(7)
with ThreadPool() as p:
    results = p.map(f, tasks)  # results不存在
print("结束")  # 这里不会执行
```

[pool]: https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing.pool
