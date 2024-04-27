# Library Reference 内置库参考

[官网][library-reference]

## typing

```{toctree}
:maxdepth: 2
./typing.md
./os.md
```

## [Built-in Functions](./built_in_functions内置函数.md)

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


7. statistics — Mathematical statistics functions 数学分析
    * [statistics.mean](https://docs.python.org/3/library/statistics.html#statistics.mean)
    * [statistics.stdev](https://docs.python.org/3/library/statistics.html#statistics.stdev)
    * statistics.StatisticsError

## Functional Programming Modules
* [itertools 迭代器](./library_reference/itertools.md)
* [functools](./library_reference/README.md#functools)
包含cache lru_cache等功能
* [operator 运算符](./library_reference/operator运算符.md)

## File and Directory Access
[官网](https://docs.python.org/3/library/filesys.html)
```{toctree}
./os.md
./tempfile.md
./pathlib.md
```

### pathlib
操作目录,路径的功能


### filecmp 文件、文件夹比较
[官网](https://docs.python.org/3/library/filecmp.html)
推荐使用 [deep-dircmp](https://github.com/mitar/python-deep-dircmp)

```python
from deep_dircmp import DeepDirCmp
DeepDirCmp(source, target).get_left_only_recursive()  # 注意，如果一个文件夹额外存在，只会返回文件夹路径，不会再迭代文件夹内部文件
```


### [shutil](https://docs.python.org/3/library/shutil.html)
* rmtree  
删除文件夹

```python
shutil.rmtree(Path)
```

* 复制文件夹
    * `dirs_exist_ok=False`

    ```python
    shutil.copytree(src, dst)
    ```

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
[https://docs.python.org/3/library/allos.html](https://docs.python.org/3/library/allos.html)

```{toctree}
./os.md
```

### getpass
```
from getpass import getpass
getpass(prompt="输入密码:")
```

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

### [multiprocessing — Process-based parallelism](./multiprocessing.md)

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

## Internet Protocols and Support

* ftplib
```python3
with FTP() as ftp:
    ftp.connect(host='localhost', port=2121)
    ftp.login()
    ftp.dir()
    with open("source.md", "rb") as f:  # 保存文件
        ftp.storbinary("STOR target.md", f)
```

* [ ] poplib
* imaplib
* [ ] nntplib
* [ ] smtplib
* [ ] telnetlib
* [ ] socketserver

### urllib
*处理url*
```{toctree}
./urllib.md
```

### uuid
* uuid.uuid1
根据序列号，时间，电脑的mac地址生成一个uuid
返回一个uuid,但是后面是固定的node,可以手工提供或者直接获取电脑的mac地址
* uuid.uuid4
生成随机的uuid

## Development Tools

### [unittest — Unit testing framework 测试框架](./unittest.md)

## [Python Runtime Services](./runtime_services.md)

* sys
* traceback
* [dataclass](./runtime_services.md#dataclass)
* [contextlib](./runtime_services.md#contextlib)



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


## 未分类

```{toctree}
../pdb调试.md
../runtime_services.md
../string.md
./argparse.md
./asyncio.md
./built_in_functions内置函数.md
./built_in_types内置数据类型.md
./csv.md
./datetime时间.md
./heapq.md
./itertools.md
./json.md
./multiprocessing.md
./operator运算符.md
./os.md
./pathlib.md
./re.md
./tempfile.md
./unittest.md
./urllib.md
./zip.md
```

## socket
```{toctree}
:maxdepth: 1
./socket.md
```

## Data Types


### [Enum](https://docs.python.org/3/library/enum.html)
```

from enum import Enum

class Type(Enum):
    A = 1
    B = '2'

Type['A'] == Type.A
Type.A.value >> 1
Type.A.name >> 'A'
list(Type) >>
[<Type.A: 1>, <Type.B: '2'>]
```

## Numeric and Mathematical Modules

### [math](https://docs.python.org/3/library/math.html)
```
math.ceil(x) 大于等于x的最小的整数, 使用 __ceil__ 方法，可以让一个对象支持这个函数
math.floor(x) 小于等于x的最大的整数, 使用 __floor__ 方法，可以让一个对象支持这个函数
```

* [isclose](https://docs.python.org/3/library/math.html#math.isclose)
相当于 `abs(a-b) <= max{abs_tol, rel_tol*max[abs(a), abs(b)]}`, 起不到校验超过`abs_tol`或者`rel_tol`的功能哦

### [decimal](https://docs.python.org/3/library/decimal.html)
```python
a = Decimal(3)
a / 3  # Decimal("0.33333333333333333")
b = Decimal("0.050")
b.scaleb(-3)  # Decimal("0.0000050")
b.scaleb(3)  # Decimal("50")
```

### [fractions](
https://docs.python.org/3.8/library/fractions.html#fractions.Fraction)
```
    from fractions import Fraction
    f = Fraction(1,3)
    print("1/3 = %d/%d" % (f.numerator, f.denominator))
```

### [random](https://docs.python.org/3.8/library/random.html)
Generate pseudo-random numbers

```python
random.choice(list)  # choose one value from list
random.choices(list, k=20)  # 随机选择20次, 可能重复选到
random.randrange(stop)
random.randrange(start, stop[, step])  
turn value from start(included) to stop(excluded)
random.randint(start, stop)  
turn value from start(included) to stop(included)
random.sample(list, k)  # choose k's value from list, 每个item只被选一次，所以k要小于len(list)
```

## [Functional Programming Modules](https://docs.python.org/3/library/functional.html)

### [itertools](./itertools.md)

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

### [operator](./operator运算符.md)


### 文件操作
* 基础
    file = open(<filename>, 'w')
    file.write('text')
    file.close()
* 模式
    w 写入模式
    b 读取模式
    a 添加模式, 无论seek到哪，write只能够添加数据
    r+ 可读可写。write以后需要flush，不然之后read会导致指针位置改变，影响结果
* 方法
    read(n)  # 读取n个字符或者字节
    seek(offset, from_what)  # offset偏移数量，from_wath 0代表开始，1代表当前，2代表末尾

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

### [Platform](https://docs.python.org/3/library/platform.html)
* system  
最实用,返回Linux, Windows, Java, Darwin

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


7. statistics — Mathematical statistics functions 数学分析
    * [statistics.mean](https://docs.python.org/3/library/statistics.html#statistics.mean)
    * [statistics.stdev](https://docs.python.org/3/library/statistics.html#statistics.stdev)
    * statistics.StatisticsError

## Functional Programming Modules
* [itertools 迭代器](./library_reference/itertools.md)
* [functools](./library_reference/README.md#functools)
包含cache lru_cache等功能
* [operator 运算符](./library_reference/operator运算符.md)

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

```{toctree}

../config.md
```

### [csv](./library_reference/csv.md)
 * [source code](https://github.com/python/cpython/blob/3.6/Lib/csv.py)

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

### logging日志处理

```{toctree}
../logging/README.md
```

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



## [Python Runtime Services](./runtime_services.md)

* sys
* traceback
* [dataclass](./runtime_services.md#dataclass)
* [contextlib](./runtime_services.md#contextlib)
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

[base64]: https://docs.python.org/3/library/base64.html
[subprocess]: https://docs.python.org/3/library/subprocess.html
[bz2]: https://docs.python.org/3/library/bz2.html#examples-of-usage
[library-reference]: https://docs.python.org/3/library/index.html
