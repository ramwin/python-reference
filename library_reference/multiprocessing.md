### [多进程multiprocessing](https://docs.python.org/3/library/multiprocessing.html)


#### [Pool](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing.pool)
Pool.map只支持一个参数。 所以如果你是多个参数， 要用Pool.starmap
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
