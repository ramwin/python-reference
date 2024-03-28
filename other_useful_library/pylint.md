# 忽略以前的代码, 只看自己的错误
```python
# pylint: disable=C,E,W,R
其他人的代码
# pylint: enable=C,E,W,R
自己的代码
```

# 忽略某行错误
```
# pylint: disbale=missing-module-docstring
```

# 忽略某个class的错误
```python
class Foo:
    # pylint: disable=no-member
    ...
```

# 配置
```
# ignore-path来忽略2个文件
ignore-paths=test.py,
    test1.py
# disable来关闭某些类型
disable=missing-function-docstring,
    ...,
```

