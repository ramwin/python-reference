# Language Reference

[官网](https://docs.python.org/3/reference/index.html)

```{toctree}
:heading-offset: 1
./exception.md
```

[官网](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)

## 6. Expressions
### [magic method魔法方法](./magic_methods/README.md)
* [slice](https://docs.python.org/3/reference/expressions.html#expression-lists)


    class A:

        def __getitem__(self, sli):
            sli.start, sli.stop, sli.step  # A()[start:stop:step]


### Evaluation order 执行顺序
[官网](https://docs.python.org/3/reference/expressions.html#evaluation-order)

    ()  # 括号内
    **  # 指数
    +x, -x  # 负数
    in, not in, is, is not, <, <=, >, >=, !=  # 比较
    not x  #
    and  #
    or  # and 和 or不是同样的哦。

## Simple statements 简单语句
11. [import机制](http://www.jianshu.com/p/b963782f59e9)
[import文档](https://docs.python.org/3/reference/simple_stmts.html#the-import-statement)  
如果使用了相对引用, 必须保证最外层不能抵达当前目录

12. [global](language_reference/global_test.py)

## Compound statements 复合语句

### [with语句 the with statement](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement)
[测试](./test/test_with.py)
成功执行时, exit的三个参数都为None, 否则为对应数据
```
class A():
    def __enter__(self):
        print('enter')
    def __exit__(self, exc_type, exc_value, traceback):
        print(f'exc_type: {exc_type}')
        print(f'exc_value: {exc_value}')
        print(f'traceback: {traceback}')
        print('exist')
with A():
    print('start')
    raise Exception('value')
```

### [for 语句](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement)
* 通过内置变量counter来记录执行的位置，所以remove会导致少执行，insert会导致重复执行

    ```
    for i in a:
        if i == 3: a.remove(i)  # 少执行
        if i == 3: a.insert(0, 3)  # 多执行
    ```

### [函数 function](./language_reference/function.md)
* [docstring](./language_reference/function.md#docstring)

[官网](https://docs.python.org/3/reference/compound_stmts.html#function-definitions)
* [decorator装饰器](http://www.cnblogs.com/huxi/archive/2011/03/01/1967600.html)
* [decorator.py](decorator装饰器.py)

### [class](./class/README.md)
[官网文档 TODO](http://ramwin.com:8000/tutorial/classes.html)
* 属性
    * `__new__`: 创建class类的时候调用  

[示例](./class/class_new.py). 通过`__new__`的时候`，返回不同的class  

    ```python
    class GuessAnimal(object):
        def __name__(self, type, *args, **kwargs):
            if type == 'dog':
                return Dog(*args, **kwargs)
            return Cat(*args, **kwargs)
    d = Some("dog")
    d.say()
    c = Some("cat")
    ```

    * `__module__` : class的模块
    * `__name__` : class的name

* [property](./library_reference/built_in_functions内置函数.md#property)

# [Library Reference 内置库参考](./library_reference/README.md)
[官网][library-reference]

1. [x] Introduction
## [Built-in Functions](./library_reference/built_in_functions内置函数.md)

* all
* any
* divmod
* enumerate

```
enumerate(['a','b','c'], start=1)  // [(0, 'a'), (1, 'b'), (2, 'c')]  但是不是list， 而是一个enumerate对象, 默认从0开始
```

* [ ] locals
* ### [map(function, iterable)](https://docs.python.org/3/library/functions.html#map)
* [ ] max
* open  
打开一个文件 buffering=0代表不需要缓存(不缓存,mode必须是b), buffering=1代表每一行保存,buffering>1代表多少字节保存
* ### [property](./library_reference/built_in_functions内置函数.md#property)
* zip: 迭代2个迭代器, 按照最短的来计算
3. Built-in Constants
4. Built-in Types
* [Set集合](./set.md)
* ### [Mapping Types -- dict 字典参考](./library_reference/built_in_types内置数据类型.md)
5. ## [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
### Warnings
* DeprecationWarning

## [Text Processing Services](https://docs.python.org/3/library/text.html)

### [2. re -- Regular expression operations 正则表达式 regex](./library_reference/re.md)
[test regrex 在线测试](https://regex101.com/#python)

### textwrap.dedent
注意, 前面和后面的换行符不会消失

```python
from textwrap import dedent
def function():
    LONG_CONTENT = dedent("""\
        A,   # 空格数量无所谓, 只要一致就行
        B,
        C\
    """)

```

7. [ ] Binary Data Services

## Data Types
[官网](https://docs.python.org/3/library/datatypes.html)

### [datetime](./library_reference/datetime时间.md)
### [ ] [calendar](https://docs.python.org/3/library/calendar.html)

```{toctree}
./collections.md
```

### [heapq](./library_reference/heapq.md)

### [bisect](https://docs.python.org/3/library/bisect.html)
通过二分法来查找list或者插入数据
```
bisect.insort(list, item)  # 把x插入list并保持顺序
bisect.bisect(list, item)  # 找到可以插入item的位置(最右侧)
# 查看是否存在
def index(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError
```

### copy  

* copy.copy(x): return a shallow copy of x
* copy.deepcopy(x): return a deepcopy
copy.copy只会copy一层, 里面的可变对象不会copy  
copy.deepcopy会copy recursively  
在shallow copy里, 对于dict, 使用的是 dict.copy(), 对于list使用的是copied_list = original_list[:]  
如果要实现自己的copye, 可以重写 `__copy__()` 和 `__deepcopy__()`  

* [ ] pprint

### [enum](./library_reference/README.md#enum)

## Numeric and Mathematical Modules
2. [math](https://docs.python.org/3/library/math.html)
```
math.ceil(x) 大于等于x的最小的整数, 使用 __ceil__ 方法，可以让一个对象支持这个函数
math.floor(x) 小于等于x的最大的整数, 使用 __floor__ 方法，可以让一个对象支持这个函数
```

* [isclose](https://docs.python.org/3/library/math.html#math.isclose)
相当于 `abs(a-b) <= max{abs_tol, rel_tol*max[abs(a), abs(b)]}`, 起不到校验超过`abs_tol`或者`rel_tol`的功能哦

4. [decimal](https://docs.python.org/3/library/decimal.html)
```python
a = Decimal(3)
a / 3  # Decimal("0.33333333333333333")
b = Decimal("0.050")
b.scaleb(-3)  # Decimal("0.0000050")
b.scaleb(3)  # Decimal("50")
```

5. [fractions](
https://docs.python.org/3.8/library/fractions.html#fractions.Fraction)
```
    from fractions import Fraction
    f = Fraction(1,3)
    print("1/3 = %d/%d" % (f.numerator, f.denominator))
```

### [random](./library_reference/README.md#random)

7. statistics — Mathematical statistics functions 数学分析
    * [statistics.mean](https://docs.python.org/3/library/statistics.html#statistics.mean)
    * [statistics.stdev](https://docs.python.org/3/library/statistics.html#statistics.stdev)
    * statistics.StatisticsError

## Functional Programming Modules
* [itertools 迭代器](./library_reference/itertools.md)
* [functools](./library_reference/README.md#functools)
包含cache lru_cache等功能
* [operator 运算符](./library_reference/operator运算符.md)

## [File and Directory Access](https://docs.python.org/3/library/filesys.html)

### [pathlib](./library_reference/pathlib.md)
操作目录,路径的功能

2. [os.path](library_reference/README.md#os)
#### [tempfile](library_reference/tempfile.md)
临时文件，临时文件夹

### [filecmp 文件、文件夹比较](https://docs.python.org/3/library/filecmp.html)
推荐使用 [deep-dircmp](https://github.com/mitar/python-deep-dircmp)

    from deep_dircmp import DeepDirCmp

    DeepDirCmp(source, target).get_left_only_recursive()  # 注意，如果一个文件夹额外存在，只会返回文件夹路径，不会再迭代文件夹内部文件


### [shutil](https://docs.python.org/3/library/shutil.html)
* rmtree  
删除文件夹


    shutil.rmtree(Path)

* 复制文件夹
    * `dirs_exist_ok=False`


    shutil.copytree(src, dst)


## Data Persistence

### [pickle](https://docs.python.org/3/library/pickle.html) *把python的对象序列化成字符串*

## Data Compression and Archiving
* [bz2][bz2]
使用方法
```
import bz2
bz2.compress(b'11111' * 1000)
>>> b'BZh91....'
bz2.decompress(b'BZh91...')
>>> b'11111...'
f = bz2.open("myfiles.bz2", "bb")
f.read()
f = bz2.open("myfiles.bz2", "wb")
f.write(data)
```


* [gzip](https://docs.python.org/3/library/gzip.html)
```
import gzip
f = gzip.open("~/test.csv.gz", compresslevel=3)
f.write("hedaer\n")
f.write("123\n")
f.close()
```


* [zipfile](./library_reference/zip.md) *处理zip压缩包*

## File Formats
[官网](https://docs.python.org/3/library/fileformats.html)
### [csv](./library_reference/csv.md)
 * [source code](https://github.com/python/cpython/blob/3.6/Lib/csv.py)
### [configparser](./config.md) 配置文件

* [ ] netrc
* [ ] xdrlib
* [ ] plistlib

## Cryptographic Services
### [hashlib](https://docs.python.org/3/library/hashlib.html)

    import hashlib
    a = hashlib.md5()
    a.update('string'.encode('utf8'))
    a.hexdigest()
    >>> 'b45cffe084dd3d20d928bee85e7b0f21'

### [ ] hmac
### [ ] secrets

## Generic Operating System Services
[官网](https://docs.python.org/3/library/allos.html)

### [os](./library_reference/README.md#os)
[ ] io

### [time](./library_reference/README.md#time)

### [argparse](./library_reference/argparse.md)
这个用来解析python的命令

5. [ ] getopt

### [logging日志处理](./logging/README.md)
### [platform](./library_reference/README.md#platform)
平台相关

## Concurrent Execution

### 线程 [Threading](https://docs.python.org/3/library/threading.html)


    from threading import Thread
    s1 = Thread(None, function, args=[], kwargs={})
    s2 = Thread(None, function2, args=[], kwargs={})
    s1.start()
    s2.start()

* `threading.get_native_id()`
获取当前线程的id  


* Thread-Local Data:  
使用`treading.local()`可以获取本线程的变量。 这个变量在几个线程内不相通  
[测试2个thread的变量](./test/test_thread_local.py)

* Lock
线程锁, 一个线程只能拿到一个

* RLock
线程锁. 同一个线程内可以多次获取

### [multiprocessing — Process-based parallelism](./library_reference/multiprocessing.md)

#### Process
* [如果不join,直接关闭](./multi/不join.py)
直到主进程都要退出的时候，会等待子进程的结束


#### 获取进程数据
[示例](./multi/获取输出.py)

#### Poll
* [imap_unordered](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.imap_unordered)
对iterable里面的每个元素执行func. chunksize代表每个进程执行的迭代次数。这样一个进程可以执行多次
[测试](./library_reference/pool_chunksize.py)
```
with Pool() as p:
    for result in p.imap_unordered(func, iterable, chunksize):
        print(result)
```

### [ ] concurrent.futures

### [subprocess][subprocess]
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


### [ ] sched

## contextvars — Context Variables
## Networking and Interprocess Communication 网络和进程间通信

### [asyncio](./library_reference/asyncio.md) *用来处理协程*
### [signal](https://docs.python.org/zh-cn/3/library/signal.html)
* 使用触发信号，处理ctrl+c的时候，保证循环执行完毕
```
stop = False

def handler(signalnum, handler):
    global stop
    stop = True

def main():
    signal.signal(signal.SIGINT, handler)
    global stop
    while not stop:
        time.sleep(0.1)
    print("stop拉")
```

## Internet Data Handling

### [JSON](./library_reference/json.md)

### [base64][base64]
原理, [RFC 3548](https://tools.ietf.org/html/rfc3548.html#section-3)

    '  '  b'00100000 00100000'
    按照6个比特来分割 001000 000010 0000[补充00]
                      I      C      A=
    对比 0-25 A-Z 26-51 a-z 52-61 0-9
    然后每76个字符加一个换行，最后加一个换行
    base64.encodebytes(b'  ') == b'ICA=\n'


    b = base64.encodebytes('我'.encode('utf8')) # 只有二进制才能encode,结果还是bytes
    b = base64.encodestring('我'.encode('utf8')) # 查了源码，果然这个是为了兼容python2的语法。以后避免使用这个方法
    b = base64.encodestring('我')   # python2里面的str就是二进制,结果是str(仍然是二进制)

7. [ ] binhex
8. [binascii](https://docs.python.org/3/library/binascii.html)
    * unhexlify(a) 把十六进制的字符串变成二进制数据
    ```
    a = 'b4447f6670a'
    binascii.unhexlify(a)
    >>> b'\xb4G\xf6g\n'
    ```

* [ ] to be continued
21. [ ] Structed Markup Processing Tools
22. ## Internet Protocols and Support
    * [ ] poplib
    * imaplib
    * [ ] nntplib
    * [ ] smtplib
    * ### [urllib](./library_reference/urllib.md) *处理url*
    * [ ] telnetlib
    * ### uuid
        * uuid.uuid1
        根据序列号，时间，电脑的mac地址生成一个uuid
        返回一个uuid,但是后面是固定的node,可以手工提供或者直接获取电脑的mac地址
        * uuid.uuid4
        生成随机的uuid
    * [ ] socketserver

## Development Tools

### [unittest — Unit testing framework 测试框架](./library_reference/unittest.md)

## [Python Runtime Services](./runtime_services.md)

* sys
* traceback
* [dataclass](./runtime_services.md#dataclass)
* [contextlib](./runtime_services.md#contextlib)

## Internet Protocols and Support

* ftplib
```python
with FTP() as ftp:
    ftp.connect(host='localhost', port=2121)
    ftp.login()
    ftp.dir()
    with open("source.md", "rb") as f:  # 保存文件
        ftp.storbinary("STOR target.md", f)
```


## [ ] Custom Python Interpreters

33. ## Python Language Services
    2. ast
    `ast.literal_eval`: "savely evalute an expression node or a string containing a Python literal or container display."
    3. [ ] to be continued

## Unix Specific Services
### [fcntl](https://docs.python.org/3/library/fcntl.html)
不过更加建议的是使用[flockcontext](./other_useful_library/README.md)
* fcntl.flock
```
f = open("name", "w")
fcntl.flock(f, fcntl.LOCK_EX)  # 只有一个线程可以获取执行, 其他的会等待, 并且如果f变量失效了，也会释放锁
fcntl.flock(f, fcntl.LOCK_UN)  # 执行完毕后记得unlock
fcntl.flock(f, fcntl.LOCK_SH)  # 可以共享
```

