# 基础
* 编辑 `settings.py`
```
    LOG_FILE = './log/log.log'
    LOG_ENABLED = True
    LOG_ENCODING = 'utf8'
    LOG_LEVEL = 'INFO'
    LOG_FORMAT = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
```
* 使用
    import logging
    logging.warning('')
