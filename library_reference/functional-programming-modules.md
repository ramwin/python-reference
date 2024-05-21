## Functional Programming Modules
[官网](https://docs.python.org/3/library/functional.html)
```{toctree}
./itertools.md
./operator运算符.md
```
### functools
对于函数和可调用对象的执行操作

* cache
缓存函数结果
```
@functools.lru_cache(max_size=128)  # 一般用lru_cache自动释放缓存. cache的话更快,但是不会自动释放
def factorial(n):
    return n * factorial(n-1) if n else 1
```

* partial
把新增的参数放入原有参数来变成新的函数

原来的函数 `log_e(10)`, 默认用math.e当底数, 返回2.30.
但是我是程序员, 经常希望以2为底数
```python
import math
import functools

def log_e(n, base=math.e):
    return math.log(n, base)

log_2 = functools.partial(log_e, base=2)
print(log_2(4))  # 2.0
```

### 文件操作
* 基础
```python
    file = open(<filename>, 'w')
    file.write('text')
    file.close()
```
* 模式
    * w 写入模式
    * b 读取模式
    * a 添加模式, 无论seek到哪，write只能够添加数据
    * r+ 可读可写。write以后需要flush，不然之后read会导致指针位置改变，影响结果
* 方法
    * read(n)  # 读取n个字符或者字节
    * seek(offset, from_what)  # offset偏移数量，from_wath 0代表开始，1代表当前，2代表末尾

#### [Process Parameters](https://docs.python.org/3/library/os.html#process-parameters)

#### [File Descriptor Operations](https://docs.python.org/3/library/os.html#file-descriptor-operations)

#### [Process Management](https://docs.python.org/3/library/os.html#process-management)

### time
[官网](https://docs.python.org/3/library/time.html)

* localtime
* mktime
没啥用, 把时间变成时间戳, 不如直接用datetime
```python
>>> time.mktime((2022, 1, 2, 3, 4, 5, 6, 0, 0))
1641063845.0
>>> datetime.datetime(2022, 1, 2, 3, 4, 5).timestamp
1641063845.0
```
