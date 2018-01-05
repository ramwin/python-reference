** Xiang Wang @ 2016-05-26 15:30:51 **

# 导航
* TODO 有待完善
* [官网教程](https://docs.python.org/3/library/re.html#regular-expression-examples)
* [测试](https://regex101.com/#python)

# 基础知识
* 匹配规则
    * `\d`  *数字*
    * `\D`  *非数字*
    * `\s`  *空白字符*
    * `\S`  *非空白字符*
    * `\w`  *单词字符*
    * `\W`  *非单词字符*
    * `(a|bc|d)  *a或者bc或者c*
    * `[a-z]` * 小写字母

* 方法
    re.compile(r'(?P<id>\d+)we').match('123we').group('id')

# 例子
* 找到字符串里面符合规则的字符串
```
    a = re.compile(r'^数据更新时间：(?P<time>[0-9: -]*)').match('数据更新时间：2016-05-25 16:00:00')
    print(a.groupdict())
```

* 把字符串里面符合规则的字符进行替换
```
    re.splite(r'\.0*', text)
```


* 删除字符串里面符合规则的字符串
