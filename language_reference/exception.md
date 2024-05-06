# Exception知识
* [python.org官网教程](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)

* 常见错误
    * AssertionError: assert 1 > 2, "数据不对"
    * ZeroDivisionError: 1/0
    * ValueError: int('we')
    * KeyboardInterrupt: 用户 ctrl+C
    * OSError

* 异常处理
```
try:
    f = open('test.md', 'w')
    语句1
except OSError as e:  # 指定错误
    print("处理结果： 无法打开文件")
except (ValueError, AssertionError) as e:
    同时能处理两种错误
else:  # 如果不报错的处理方式
    f.close()
finally:  # 不管什么情况都会执行
    print("执行结束")
    # 如果try里面有异常，会继续抛出这个异常
```
