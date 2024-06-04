# Concurrent Execution
```{toctree}
./multiprocessing.md
```

## 线程 [Threading](https://docs.python.org/3/library/threading.html)

### Thread
```
new_thread = threading.Thread(target=<function>, args=[], kwargs={})
new_thread.start()
new_thread.join()
new_thread.run()  # run的话就不起线程了，和直接调用f是一个效果
```

如果线程报错了, 不会影响后续执行, 想要抓住这个exception, 就用[ThreadPool](./multiprocessing.md)吧
```python
from threading import Thread
s1 = Thread(None, function, args=[], kwargs={})
s2 = Thread(None, function2, args=[], kwargs={})
s1.start()
s2.start()
```

* `threading.get_native_id()`
获取当前线程的id  

* Thread-Local Data:  
使用`treading.local()`可以获取本线程的变量。 这个变量在几个线程内不相通  
[测试2个thread的变量](./test/test_thread_local.py)

* Lock
线程锁, 一个线程只能拿到一个

* RLock
线程锁. 同一个线程内可以多次获取

## [multiprocessing — Process-based parallelism](./multiprocessing.md)

### Process
* [如果不join,直接关闭](./multi/不join.py)
直到主进程都要退出的时候，会等待子进程的结束


### 获取进程数据
[示例](./multi/获取输出.py)

## [ ] concurrent.futures

## [subprocess][subprocess]
基础用法

```
import subprocess
try:
    res = subprocess.run(["ls", "-l"], capture_output=True, check=True)
    print(res.stdout.decode("utf-8"))
except subprocess.TimeoutExpired as e:
    logger.exception(e)
    logger.exception("超时了")
except subprocess.CalledProcessError as e:
    logger.exception(e)
    logger.error(f"执行任务失败")
```

* 输入输出
[测试代码](./test/subprocess_input.py)

```
proc = subprocess.Popen(["sh", "input.sh"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
outs, errs = proc.communicate(
    input="1\n2\nexit\n".encode("utf-8"), timeout=1)
print(outs.decode('utf-8'))
```

* [异步执行 Popen](https://docs.python.org/3/library/subprocess.html#popen-constructor)

```
from subprocess import Popen
thread = Popen(["python", "-m", "pyftpdlib"])
time.sleep(10)
thread.kill()
```


## [ ] sched

