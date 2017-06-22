#### Xiang Wang @ 2017-05-03 18:00:06

# 基础
* [官网教程](https://docs.python.org/3.5/library/configparser.html)
```
    config = configparser.ConfigParser()
    config.read("config.cfg")
    config.getint("common", "port")
    config.getboolean("common", "debug")
```

* getboolean:
    "1", "yes", "true", "on" 会当作 True  # 不区分大小写
    "0", "no", "false", "off" 会当作 False
