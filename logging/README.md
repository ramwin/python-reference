**Xiang Wang @ 2018-09-04 18:49:59**

* [官网教程-基础](https://docs.python.org/3/howto/logging.html)
* [官网模块-进阶](https://docs.python.org/3/library/logging.html)

### example
* 基础  
默认配置, 保存到文件和终端

```python3
import logging

stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler("info.log", mode="a")

logging.basicConfig(
    level=logging.INFO,
    format=(
        '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
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


* 添加过滤器,只记录info,不记录warning
用在info的logger


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


### [Exceptions raised during logging][exceptions]
[测试](./test_unicode.py)

### logging.Logger
* `debug(msg, *args, **kwargs)`
* `log(lvl, msg, *args, **kwargs)`
lvl: 必须是整数
用指定的lvl等级去添加一个日志, 只要这个lvl大于等于20, 就会出发logging.INFO

### logging.handlers
[官网](https://docs.python.org/3/library/logging.handlers.html)

#### [StreamHandler](https://docs.python.org/3/library/logging.handlers.html#streamhandler)
#### [FileHandler](https://docs.python.org/3/library/logging.handlers.html#filehandler)
```
class logging.FileHandler(filename, mode='a', encoding=None, delay=False)
```

#### [MemoryHandler](https://docs.python.org/3/library/logging.handlers.html#memoryhandler)
[测试](./memory_handler.py)
MemoryHandler继承了BufferingHandler, 可以用来临时记录日志，一旦日志太多(超过了capacity),或者等级太高(达到了flushLevel), 就会记录到(target)
如果需要抛弃刚才的日志，可以调用`log.handelrs[0].close()`或者`log.removeHandler(memory_handler)`
```
class logging.handlers.MemoryHandler(capacity, flushLevel=ERROR, target=None)
```

#### 其他
* [ ] NullHandler
* [ ] WatchedFileHadnler
* [ ] BaseRotatingHandler
* [ ] RotatingFileHandler
* [ ] TimedRotatingFileHandler
* [ ] SocketHandler
* [ ] DatagramHandler
* [ ] SysLogHandler
* [ ] NTEventLogHandler
* [ ] SMTPHandler
* [ ] HTTPHandler
* [ ] QueueHandler
* [ ] QueueListener


[exceptions]: https://docs.python.org/3/howto/logging.html#exceptions-raised-during-logging
