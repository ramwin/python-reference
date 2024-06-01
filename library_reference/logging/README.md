# LOGGING
* [官网教程-基础](https://docs.python.org/3/howto/logging.html)
* [官网模块-进阶](https://docs.python.org/3/library/logging.html)

## example
* 基础  
默认配置, 保存到文件和终端

```python3
import logging

stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler("info.log", mode="a")

logging.captureWarnings(True)
logging.basicConfig(
    level=logging.INFO,
    format=(
        '%(asctime)s %(pathname)s[line:%(lineno)d] %(levelname)s %(message)s'
    ),
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        stream_handler,
        file_handler,
    ],
)
```

* 保存到文件的同时，输入的终端  
用2个handler

```
import logging
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

fh = logging.FileHandler(filename='log.log')
fh.setLevel(logging.WARNING)
f_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(f_formatter)

logger.addHandler(ch)
logger.addHandler(fh)

logger.info("info message")
logger.warn("warn message")
```


* 添加过滤器,只记录info,不记录warning
用在info的logger


```
import logging
logger = logging.getLogger('test_filter')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(
    logging.Formatter('%(user)s %(message)s')
)
class RamwinFilter(logging.Filter):
    def filter(self, record):
        record.user = 'ramwin'
        if record.levelname == 'WARNING':
            return False
        print(record.levelname)
        return True
f = RamwinFilter()
logger.addHandler(ch)
logger.addFilter(f)
logger.info("info")
logger.warning("warning")
```


## [Exceptions raised during logging][exceptions]
[测试](./test_unicode.py)

## logging.Logger
* propagate
设置这个值就能让不抛出LogRecord给父级

### [`debug(msg, stack_info, *args, **kwargs)`](https://docs.python.org/3/library/logging.html#logging.debug)
第二个参数 stack_info 如果是 `True`, 就会把日志的堆栈信息打印出来


* `log(lvl, msg, *args, **kwargs)`

lvl: 必须是整数
用指定的lvl等级去添加一个日志, 只要这个lvl大于等于20, 就会出发logging.INFO

## logging.handlers
[官网](https://docs.python.org/3/library/logging.handlers.html)

### [StreamHandler](https://docs.python.org/3/library/logging.handlers.html#streamhandler)
默认是sys.std, 建议改成sys.stdout
```python3
/usr/lib/python3.8/logging/__init__.py
class StreamHandler(Handler):

    def __init__(self, stream=None):
        if stream is None:
            stream = sys.stderr
```
所以StreamHandler的输出都是2>error哦

### [FileHandler](https://docs.python.org/3/library/logging.handlers.html#filehandler)
```
class logging.FileHandler(filename, mode='a', encoding=None, delay=False)
```

### RotatingFileHandler
```
from logging.handlers import RotatingFileHandler
import humanfriendly
RotatingFileHandler(
    "info.log", mode="a",
    maxBytes=humanfriendly.parse_size("10MiB"), backupCount=30,
)
```

### [MemoryHandler](https://docs.python.org/3/library/logging.handlers.html#memoryhandler)
[测试](./memory_handler.py)
MemoryHandler继承了BufferingHandler, 可以用来临时记录日志，一旦日志太多(超过了capacity),或者等级太高(达到了flushLevel), 就会记录到(target)
如果需要抛弃刚才的日志，可以调用`log.handelrs[0].close()`或者`log.removeHandler(memory_handler)`
```
class logging.handlers.MemoryHandler(capacity, flushLevel=ERROR, target=None)
```

### 其他
* [ ] NullHandler
* [ ] WatchedFileHadnler
* [ ] BaseRotatingHandler
* [ ] TimedRotatingFileHandler
* [ ] SocketHandler
* [ ] DatagramHandler
* [ ] SysLogHandler
* [ ] NTEventLogHandler
* [ ] SMTPHandler
* [ ] HTTPHandler
* [ ] QueueHandler
* [ ] QueueListener


## [LogRecord](https://docs.python.org/3/library/logging.html#logrecord-objects)

## LogRecord属性
* `%(asctime)s`: 时间
* `%(created)s`: 时间戳
* `%(filename)s`: 文件名
* `%(pathname)s`: 路径名
* `%(levelname)s`: INFO, ERROR等级信息
* `%(message)s`: 消息内容
* `%(module)s`: 模块名，文件名.stem
* `%(process)d`: 进程ID
* `%(processName)d`: 进程名


## 模块级函数
### basicConfig(**kwargs)
因为formatter的设置是在basicConfig里设置的, 所以basicConfig以后再给root添加logger就没有formatter的效果了(这样可以避免每个recorder都要判断formatter是否存在)  
basicConfig只能调用一次, 后续调用没效果.  
```python3
for h in root.handlers[:]:  # 清理旧的handler
    root.removeHandler(h)
    h.close()
for h in handlers:  # 设置新的handler
    if h.formatter is None:
        h.setFormatter(fmt)
```


### shutdown
* 系统退出时自动调用, 不要手动调用
* 调用时会让每个logger都调用flush后close

### warnings
```python3
logging.captureWarnings(True)
```

[exceptions]: https://docs.python.org/3/howto/logging.html#exceptions-raised-during-logging
