**Xiang Wang @ 2018-09-04 18:49:59**

# logging日志模块
## 参考
* [官网教程](https://docs.python.org/3/howto/logging.html)

## 基础
```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename='./log/test.log',
    filemode='a')
    
logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
 
log = logging.getLogger()
log.error('error')
```

## 保存到文件的同时，输入的终端
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

## 添加过滤器,只记录info,不记录warning
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
