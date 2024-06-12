# 其他
* socket.gethostname()    # 获取当前主机的主机名
* uuid.getnote()    # 获取本机的MAC地址  
mac=uuid.UUID(int = node).hex[-12:]
* [ ] `readme_renderer`

## 进程
通过fork可以创建一个子线程。子线程可以完整地运行并且每个子线程可以充分地利用一个cpu.当一个线程崩溃后，不会影响其他线程
## 线程
python的解释器在执行代码的时候，有个GIL锁，保证同一时间只有一个线程执行。所以不能充分利用CPU。但是这不代表不会出现几个线程打乱数据的问题，因为线程的切换是按照python字节码来处理的。`test/test_thread.py` 不会应为有多核CPU而变快。但是`test/test_fork.py`会因为多核而变快
用kill杀出一个子线程后，会导致进程崩溃

## 性能

1. time.time 来判断是否刷新缓存，1秒能执行753万次
```python
if time.time() > start :
    refresh()
```


2. random.random 来判断， 1秒能执行977万次


```python
if random.random() > 0.0000001:
    refresh()
```

3. 多进程的queue: 50K/s
```{literalinclude} ./library_reference/test_multiprocessing_queue.py
```

3. redis.get  
本地测试key长度为3和长度为720都差不多
`0.05ms, 20K/s`

4. 数据库的get  
`0.3ms, 2K/s`
