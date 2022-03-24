# 目录
* [Language Reference 语法](#language-reference)
* [Library Reference 内置包参考](#library-reference-内置库参考)
* [Other Useful Library 其他有用的包](#other-useful-library)
* [official documents 官网文档](https://docs.python.org/3/)
* [python tips 小技巧](http://book.pythontips.com/en/latest/index.html)
* [github链接](https://github.com/ramwin/python-reference/)

# tutorial
[官网](https://docs.python.org/3/tutorial/index.html)
## Data Structures 基础类型
其实这个是Library Reference的内容
* ### [列表list](list.md)
    * [自定义可迭代](./for.md)
* ### [string](./string.md)
    * [unicode table](https://unicode-table.com/cn/#samaritan)
    * #### [format](./string.md#format)
5. [x] Dictionaries  
使用**del**可以删除一个key  
list(d)可以把Dictionaries的keys按照插入的顺序输出 *python3.7新特性. 使用时注意版本是否支持*
```python3
    a_dict = {'foo': 'bar', 'my': 'a-only'}
    b_dict = {'foo': 'b', 'you': 'b-only'}
    a_dict.update(b_dict)
    >>> a_dict
    {'foo': 'b', 'my': 'a-only', 'you': 'b-only'}
```
* [集合set](set.md)

## Classes
* 9.8 [Iterators](https://docs.python.org/3/tutorial/classes.html#iterators)
定义一个iter会返回一个class(拥有__next__方法). 如果这个iterator自己有__next__方法，他可以返回self  
for的功能就是调用object的`__iter__`函数
* 9.9 [Generators](https://docs.python.org/3/tutorial/classes.html#generators)
在函数里添加yield来使得这个函数变成iterators
    1. 自动创建`__iter__, __next__`函数
    2. 每次执行next时自动更新，免去手动设置`self.data, self.index`
    3. 不返回时，自动`raise StopIteration`


# [Language Reference](https://docs.python.org/3/reference/index.html)
## Exceution model
* [Exception报错](./exception.md)
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
11. [import机制](http://www.jianshu.com/p/b963782f59e9) [import文档](https://docs.python.org/3/reference/simple_stmts.html#the-import-statement)
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

### [函数 function](function.md)
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

# [Library Reference 内置库参考][library-reference]
1. [x] Introduction
2. ## [Built-in Functions](./library_reference/built_in_functions内置函数.md)
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

### [2. re -- Regular expression operations 正则表达式 regex](./re.md)
[test regrex 在线测试](https://regex101.com/#python)

7. [ ] Binary Data Services

## [Data Types](https://docs.python.org/3/library/datatypes.html)

### [datetime](./datetime时间.md)
### [ ] [calendar](https://docs.python.org/3/library/calendar.html)

### [collections](./collections.md)

### [collections.abc](./collections.md#collections.abc)
### [ ] heapq: *heap queque algorithm*

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

* [ ] ...
10. copy  
copy.copy(x): return a shallow copy of x
copy.deepcopy(x): return a deepcopy
copy.copy只会copy一层, 里面的可变对象不会copy  
copy.deepcopy会copy recursively  
在shallow copy里, 对于dict, 使用的是 dict.copy(), 对于list使用的是copied_list = original_list[:]  
如果要实现自己的copye, 可以重写 `__copy__()` 和 `__deepcopy__()`  
11. [ ] pprint
12. [ ] ...

### Numeric and Mathematical Modules
2. [math](https://docs.python.org/3/library/math.html)
```
math.ceil(x) 大于等于x的最小的整数, 使用 __ceil__ 方法，可以让一个对象支持这个函数
math.floor(x) 小于等于x的最大的整数, 使用 __floor__ 方法，可以让一个对象支持这个函数
```

* [isclose](https://docs.python.org/3/library/math.html#math.isclose)
相当于 `abs(a-b) <= max{abs_tol, rel_tol*max[abs(a), abs(b)]}`, 起不到校验超过`abs_tol`或者`rel_tol`的功能哦

4. [decimal](https://docs.python.org/3/library/decimal.html)
```
```

5. [fractions](
https://docs.python.org/3.8/library/fractions.html#fractions.Fraction)
```
    from fractions import Fraction
    f = Fraction(1,3)
    print("1/3 = %d/%d" % (f.numerator, f.denominator))
```
6. [random](https://docs.python.org/3.8/library/random.html)
Generate pseudo-random numbers
    * random.choice(list)  # choose one value from list
    * random.choices(list, k=20)  # 随机选择20次, 可能重复宣导
    * random.randrange(stop)
    * random.randrange(start, stop[, step])  
    return value from start(included) to stop(excluded)
    * random.randint(start, stop)  
    return value from start(included) to stop(included)
    * random.sample(list, k)  # choose k's value from list, 每个item只被选一次，所以k要小于len(list)
7. statistics — Mathematical statistics functions 数学分析
    * [statistics.mean](https://docs.python.org/3/library/statistics.html#statistics.mean)
    * [statistics.stdev](https://docs.python.org/3/library/statistics.html#statistics.stdev)
    * statistics.StatisticsError

10. ## [Functional Programming Modules](https://docs.python.org/3/library/functional.html)
### [itertools](https://docs.python.org/3/library/itertools.html)

* count(start, [step])  
从某个数字开始一直循环


    from itertools import count
    loop = count(10)
    next(loop) // 10
    next(loop) // 11
    next(loop) // 12
    ...

### functools: 对于函数和可调用对象的执行操作

### [operator](./operator运算符.md)

## [File and Directory Access](https://docs.python.org/3/library/filesys.html)

### [pathlib](./library_reference/pathlib.md)
操作目录,路径的功能

2. [os.path](library_reference/os.md)
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


    import gzip
    f = gzip.open("~/test.csv.gz", compresslevel=3)
    f.write("hedaer\n")
    f.write("123\n")
    f.close()


* [zipfile](./zip.md) *处理zip压缩包*

14. File Formats
[官网](https://docs.python.org/3/library/fileformats.html)
    1. ### [csv](./csv.md)
        * [source code](https://github.com/python/cpython/blob/3.6/Lib/csv.py)
    2. ### [configparser](./config.md) 配置文件
    3. [ ] netrc
    4. [ ] xdrlib
    5. [ ] plistlib

## Cryptographic Services
### [hashlib](https://docs.python.org/3/library/hashlib.html)

    import hashlib
    a = hashlib.md5()
    a.update('string'.encode('utf8'))
    a.hexdigest()
    >>> 'b45cffe084dd3d20d928bee85e7b0f21'

### [ ] hmac
### [ ] secrets

## [Generic Operating System Services](https://docs.python.org/3/library/allos.html)
1. ### [os](./os.md)
2. [ ] io
3. [ ] time
4. [argparse](./library_reference/argparse.md)
这个用来解析python的命令
5. [ ] getopt

### [logging日志处理](./logging/README.md)
9. [ ] to be continued

## Concurrent Execution

### 线程 [Threading](https://docs.python.org/3/library/threading.html)


    from threading import Thread
    s1 = Thread(None, function, args=[], kwargs={})
    s2 = Thread(None, function2, args=[], kwargs={})
    s1.start()
    s2.start()

* `threading.get_native_id()`
获取当前线程的id  


* Trhead-Local Data:  
使用`treading.local()`可以获取本线程的变量。 这个变量在几个线程内不想通  
[测试2个thread的变量](./test/test_thread_local.py)


### multiprocessing — Process-based parallelism
[测试](./multi/poll_test.py)
* Introduction
p.map返回一个列表

```
from multiprocessing import Pool
def f(x):
    return x * x
with Pool(5) as p:
    print(p.map(f, [1,2,3]))
```

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
[socket](./library_reference/socket.md) *低级的网络接口*
### [signal](https://docs.python.org/zh-cn/3/library/signal.html)
* 使用触发信号，处理ctrl+c的时候，保证循环执行完毕

    
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
27. Development Tools
    4. ### [unittest — Unit testing framework 测试框架](./library_reference/unittest.md)

30. ## [Python Runtime Services 和编译器,环境有关的服务](https://docs.python.org/3/library/python.html)

### [Sys](https://docs.python.org/3/library/sys.html)
* stdin
```
print(sys.stdin)  # 用于python处理pipe数据
```

### traceback -- Print or retrieve a stack traceback
[官网](https://docs.python.org/3/library/traceback.html)
```
traceback.print_stack()  # 直接print出stack
log = traceback.format_exc()  # 记录报错的stack
stack = traceback.format_stack()  # 记录当前的stack
```

## Internet Protocols and Support

* ftplib

    ```
    with FTP() as ftp:
        ftp.connect(host='localhost', port=2121)
        ftp.login()
        ftp.dir()
    ```


## [ ] Custom Python Interpreters

33. ## Python Language Services
    2. ast
    `ast.literal_eval`: "savely evalute an expression node or a string containing a Python literal or container display."
    3. [ ] to be continued

## Unix Specific Services
### [fcntl](https://docs.python.org/3/library/fcntl.html)
* fcntl.flock
```
f = open("name", "w")
fcntl.flock(f, fcntl.LOCK_EX)  # 只有一个线程可以获取执行, 其他的会等待, 并且如果f变量失效了，也会释放锁
fcntl.flock(f, fcntl.LOCK_UN)  # 执行完毕后记得unlock
fcntl.flock(f, fcntl.LOCK_SH)  # 可以共享
```

# 其他有用的包 Other Useful Library
## 7z

[官网](https://github.com/miurahr/py7zr)


    import py7zr
    archive = py7zr.SevenZipFile('sample.7z', mode='r')
    archive.extractall(path='/tmp')


## beautifulsoup4 *用来解析html文件*
[官网](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#id5)
    * 安装: `pip3 install beautifulsoup4`
    * [文档整理](./other_useful_library/beautifulsoup.md)
* [captcha](./other_useful_library/captcha_test.py) *生成验证码*
* ## celery *用来执行异步脚本*
这个软件在linux-reference里面  
    * [官网](http://docs.celeryproject.org/en/latest/index.html)
    * [github在线链接](https://github.com/ramwin/linux-reference#celery)
    * [本地linux-reference链接](../linux-reference/README.md#celery)

## [click](./other_useful_library/click.md) *用python写shell命令command*

## [diff-match-patch](https://github.com/google/diff-match-patch)
用来比较文字的不同
* 用法
    ```
    >>> from diff_match_patch import diff_match_patch
    >>> dmp = diff_match_patch()
    >>> dmp.diff_main('123', '22')
    [(-1, '1'), (1, '2'), (0, '2'), (-1, '3')]
    >>> dmp.diff_prettyHtml(dmp.diff_main('123', '223'))
    '<del style="background:#ffe6e6;">1</del><ins style="background:#e6ffe6;">2</ins><span>23</span>'
    ```
* 效果  
<del style="background:#ffe6e6;">1</del><ins style="background:#e6ffe6;">2</ins><span>23</span>

## [filelock](https://github.com/benediktschmitt/py-filelock)


    from filelock import Timeout, FileLock
    lock = FileLock(path)
    try:
        lock.acquire(timeout=0)
    except Timeout:
        pass


## [git](https://gitpython.readthedocs.io/en/stable/tutorial.html)
处理git用
* 克隆代码

```
from git import Repo
Repo.clone_from(url, to_path)
git.Repo.clone_from(url, to_path, recurse_submodule=True)
```

* 基础代码

```
sudo pip3 install gitpython
from git import Repo
repo = Repo()
for tag in repo.tags:
    print(tag.name, tag.commit)

for commit in repo.iter_commits(max_count=10):
    print(commit.hexsha, commit.message, commit.author.name, )
```

* 运行git命令

```
import git
repo.git.rebase
cmd = git.cmd.Git()
cmd.execute('git lfs ls-files -l')
try:
    repo.git.merge(<ref>)  # 合并分支
except git.GitCommandError:
    raise
```


## [imapclient](https://github.com/mjs/imapclient)
* 搜索邮件

    ```
    client = IMAPClient(host="imap.qq.com")
    password = input("输入密码")
    client.login("ramwin@qq.com", password)
    message_ids = client.search(
      [u'SINCE', date(2021, 4, 8)],
    )
    >>> [393]
    ```

* 获取邮件

    ```
    message_id = 393
    content = client.fetch(message_id, ['FLAGS', 'RFC822'])[393][b'RFC822']
    ```

* 解析邮件

    ```
    import mailparser
    mail = mailparser.parse_from_bytes(content)
    print(mail.headers['Subject'])
    print(mail.body)
    ```

* 设置已读

    ```
    client.set_flags(messages, imapclient.SEEN)
    ```


## [faker](https://github.com/joke2k/faker)  *use fake to create a lot of name of text*  
    ```python
    from faker import Faker
    f = Faker('zh_cn')
    print(f.name(), f.address(), f.text())
    f.profile(['ssn', 'birthdate'])
    ```

    ```shell
    $ faker address
    $ faker name
    $ faker password
    ```
## [flake8] *检测python代码是不是满足pep8*
## [flask](./flask.md) *轻量级http服务器*
* [ics](https://pypi.org/project/ics/) *日历，行程 calendar*
* [ipdb](./other_useful_library/ipdb.md) *断点来检测查看源码和运行状态*
* [itchat](https://github.com/littlecodersh/ItChat)  *微信机器人*
* [iptools] *处理IP地址的包*
* [jinja模板渲染](./jinjia.md)
* kafka *用于kafka的消息分发*
    ```
    from kafka import KafkaConsumer
    consumer = KafkaConsumer('test',bootstrap_servers='192.168.1.191')
    for msg in consumer:
        print(msg)
    from kafka import SimpleProducer, SimpleClient
    kafka_client = SimpleClient('192.168.1.191')
    kafka_producer = SimpleProducer(kafka_client, async=False)
    kafka_producer.send_messages('test',b'test')
    ```
## [mysqliclient](https://mysqlclient.readthedocs.io/index.html)  
操作mysql数据库的包
* 安装
```
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
sudo pip3 install mysqlclient
```
* 运行
```
    from MySQLdb.connections import Connection
    db = Connection(db="test")
    c = db.cursor()

    res = c.execute("select * from pets");
    print(c.fetchall())
    >>> ((1, 'cat'), (2, 'cat'), (3, 'dogs'), (13, 'dog'), (14, 'dog'), (15, 'dog'), (21, 'dog'), (22, 'dog'))

    res = c.execute("insert into pets values (null, 'dog')");
    # 注意即使没有commit, 数据库id也会自增. 如果一次没有commit, 下次commit时,id就不是连续的了
    db.commit()
```

## [matplotlib](https://matplotlib.org/stable/tutorials/index)
画图工具

```python
imoprt matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])  # 默认x轴是0, 1, 2, 3
plt.plot([2, 3, 4, 5], [2, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()
```

## [mongoengine](./other_useful_library/mongoengine.md) *把mongodb当作sql用。那你为什么不直接用mysql啊*
* [moviewpy](https://github.com/Zulko/moviepy) *操作mp4的包*


    from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
    # 截取前5秒的mp4文件
    ffmpeg_extract_subclip("movie.mp4", 0, 5, targetname="test.mp4")

## [ordered-set](https://github.com/LuminosoInsight/ordered-set)
有顺序的set, 实现原理其实就是用一个class内部保存一个list和一个set.  
我尝试用dict来做(python现在dict的key是有顺序的),但是他的key不太方便做index顺序索引.  
但是他内部是先判断是否存在,后插入的, 会不会遇到多线程导致key重复的问题呢?  
会的, [参考代码](./test/test_sorted_set.py) 在sorted_set的add函数里加入一个time.sleep可以发现, 不加的话估计要很大的高并发才能出现
```
sudo pip3 install ordered-set

from ordered_set import OrderedSet
a = OrderedSet()
a.add(3)
a.update([5, 1, 4]) // OrderedSet([3, 5, 1, 4])
a.indexof(3)  // 0
```

## [openpyxl](./other_useful_library/openpyxl.md) *处理excel*

## [pandas](./other_useful_library/pandas.md)

## paramiko
[github](https://github.com/paramiko/paramiko) [文档](https://docs.paramiko.org/)
处理ssh的包，所以也能当sftp服务或者客户端。

* 示例

    ```python
    import paramiko

    client = paramiko.client.SSHClient()
    client.load_system_host_keys()
    client.connect(
        hostname="www.ramwin.com", port=22,
        username="*****", password="******")
    stdin, stdout, stderr = client.exec_command('pwd')
    print(stdout.read())
    ```

## [pdf2image](https://github.com/Belval/pdf2image): *把pdf转化成图片的库*
[测试代码](./other_useful_library/pdfconvert.py)

    from pdf2image import convert_from_path
    convert_from_path(pdf_path, output_folder=path, fmt='png')
    images = convert_from_path(pdf_path)


## [pdfminer](https://github.com/euske/pdfminer) *解析pdf的包，好用*
## [peewee](./other_useful_library/peewee.md) *简单而轻量级的sqlite3 orm，和django很像*
## [pillow](./pillow.md)
## [pip](https://pip.pypa.io/en/stable/user_guide/#config-file) *快速安装包*  
* pip *快速安装包*  
    * [官网](https://pip.pypa.io/en/stable/)
    * [配置文件](https://pip.pypa.io/en/stable/user_guide/#config-file)
    * 使用其他源
```
pip install --extra-index=https://pypi.tuna.tsinghua.edu.cn/simple --extra-index=https://pypi.python.org/ django
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple django==1.11  
pip install -i https://pypi.org/simple django==1.11
sudo pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple  # 设置清华的源
export LC_ALL="en_US.UTF-8"  # 出现乱码
export LC_CTYPE="en_US.UTF-8"
```

## [pycharm]
* 快捷键:
    * 界面工具查看
        * 命令行: `alt+F12`
    * 代码编辑
        * [折叠代码](https://www.jetbrains.com/help/pycharm/code-folding-2.html)
        * `Ctrl+B 或者 Ctal+click`: 查看一个函数的定义
        * `Ctrl+Q`: 查看一个函数的文档
        * `查看文件结构`: `alt+7` or `ctrl+F12`
        * `shift+F6`: *重构函数名称，全局变化他的名字*
    * 跳转
        * `ctrl+shift+backspace`: 查看上期编辑的地方
* ## [django支持](https://www.jetbrains.com/help/pycharm/running-tasks-of-manage-py-utility.html)

## [pycrypto]
    * 安装:
        * windows: 先去[下载visual c++ 9.0](http://aka.ms/vcpython27)，然后再 `pip install pycrypto`
## [pydub](https://github.com/jiaaro/pydub) *编辑mp3的包*
* 安装依赖: `apt install libav-tools ffmpeg`
* [示例](./other_useful_library/mp4tomp3.py)
* 基础:

    import math
    from pydub import AudioSegment
    song = AudioSegment.from_mp3('origin.mp3')
    song[10*1000: 40*1000].export('target.mp3')
    # 把一个视频切割成很多个小的mp3 ../other_useful_library/mp4tomp3.py

## [pyenv](./other_useful_library/pyenv.md)
python虚拟化，通过制定python路径，来在服务器安装多个python

## pyftpdlib ftp客户端和服务端

    # 直接启动一个ftplib
    python -m pyftpdlib  # 默认匿名登录, 端口号2121
    python -m pyftpdlib --port=1223 --username=admin --password=123  -d ~/Downloads


## [PyPDF2](https://pythonhosted.org/PyPDF2/) *对中文支持不友好*
* pyperclip *控制系统剪切板*
    pyperclip.copy('ew') # 把ew放入剪切板

## [pysrt](./other_useful_library/README.md#pysrt)  *控制srt字幕*

## [python-docx](https://python-docx.readthedocs.io/en/latest/index.html)

```python
f = open("模板.docx", "rb")
document = Document() or Document(f)
first_line = document.paragraphs[0]
first_line.text = "通知"
document.save("通知.docx")
```

## python-dotenv
* 用来读取本地.env的配置(当前目录.env > ~/.env)  
```
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()
CONFIG = {
    **os.environ(),
    dotenv_values,
}
```

* 设置环境变量  
```
dotenv set EMAIL foo@example.org
dotenv list
```

## [pytz](https://pythonhosted.org/pytz/)  *时区*
    ```
    from datetime import datetime
    from pytz import timezone
    import pytz
    utc = pytz.utc
    shanghai = timezone("Asia/Shanghai")
    fmt = "%Y-%m-%d %H:%M:%S %Z%z"
    loc_datetime = shanghai.localize(datetime(2002, 10, 27, 6, 0, 0))
    print(loc_datetime.strftime(fmt))
    utc_time = loc_datetime.astimezone(utc)
    ```
## [PyWinMouse](https://pypi.org/project/PyWinMouse/)  *windows下操作鼠标*
## [qiniu](./qiniu.md)  *七牛的接口*
## [redis](./redis.md) *use redis db*
## [requests](./other_useful_library/requests.md) *发送http请求*
## [rsa](./other_useful_library/rsa.md) *使用rsa加密*
## [scp](https://github.com/jbardin/scp.py)
用scp传输文件
```
with SSHClient() as ssh:
    ssh.connect("ramwin.com", compress=True)  # https://github.com/jbardin/scp.py/pull/19
    with SCPClient(ssh.get_transport()) as scp:
        scp.put(<本地文件>, <远程路径>)
        scp.get(<远程路径>, <本地文件>, recursive=True)
```

## [six](./other_useful_library/six.md) `python2和python3兼容的库`
## [scrapy](./scrapy/README.md)

## [sortedcontainers](https://github.com/grantjenks/python-sortedcontainers)

    pip install sortedcontainers
    from sortedcontainers import SortedList
    s1 = SortedList()
    s1.add(0)
    s1.update([2, 1, 3])

## [sortedsets](https://github.com/tailhook/sortedsets)
模仿redis的sorted set做的自动排序的set

    sudo pip3 install sortedsets
    >>> from sortedsets import SortedSet
    >>> ss = SortedSet()
    >>> for i in range(1, 1000):
    >>>     ss['player' + str(i)] = i*10 if i % 2 else i*i
    ss.by_score[470:511]
    >>> ss.index('player20'), ss.index('player21')
    400, 210


* ## ~~[srt](http://srt.readthedocs.io/en/latest/api.html)*因为缺少shift功能而改成用pysrt*~~
## [visidata](https://www.visidata.org/docs/rows/)
查看csv文件
* [快捷键](https://jsvine.github.io/visidata-cheat-sheet/en/)
  * | 搜索列来选择行
  * s 选择行
  * " 筛选过滤出的结果
  * _ 适应宽度

## [virtualenv](https://virtualenv.pypa.io/en/stable/)
```
virtualenv --system-site-packages -p /bin/python ENV
```
* ## [watchdog](https://pypi.org/project/watchdog/) *监控文件变化*
* ## websocket [websocket 客户端](https://github.com/websocket-client/websocket-client)
* ## [wechatpy](./other_useful_library/wechatpy.md) *和微信的接口*
* ## [wechat-django](https://github.com/Xavier-Lam/wechat-django) *微信的django app*
* ## [word2html](https://github.com/bradmontgomery/word2html)  *把word转化成html*
* ## [word2vec](http://nbviewer.jupyter.org/github/danielfrg/word2vec/blob/master/examples/word2vec.ipynb)
```
import word2vec
word2vec.word2phrase('./text8', './text8-phrases', verbose=True)
word2vec.word2vec('text8-phrases', 'text8.bin', size=100, verbose=True)
word2vec.word2clusters('text8', 'text8-clusters.txt', 100, verbose=True)
import word2vec
model = word2vec.load('text8.bin')
model.vocab
model.vectors.shape
model.vectors
model['狗'].shape
```

* ## [flake8] *检测python代码是不是满足pep8*
* ## [xlrd] *读取excel数据*
```python
import xlrd
wb = xlrd.open_workbook(filename)
wb.sheets()  // [sheet0, sheet1, sheet2]
ws = wb.sheets()[0]
ws.visibility  // 2: hidden 0: show
for i in range(ws.nrows):
    print(ws.row(i)[0])  // first column
```

## [yapf] *把python的代码格式化*

# 其他
* socket.gethostname()    # 获取当前主机的主机名
* uuid.getnote()    # 获取本机的MAC地址  
mac=uuid.UUID(int = node).hex[-12:]
* [ ] `readme_renderer`

## [设计模式](./设计模式.md)
[runoob教程](http://www.runoob.com/design-pattern/factory-pattern.html)

## 进程
通过fork可以创建一个子线程。子线程可以完整地运行并且每个子线程可以充分地利用一个cpu.当一个线程崩溃后，不会影响其他线程
## 线程
python的解释器在执行代码的时候，有个GIL锁，保证同一时间只有一个线程执行。所以不能充分利用CPU。但是这不代表不会出现几个线程打乱数据的问题，因为线程的切换是按照python字节码来处理的。`test/test_thread.py` 不会应为有多核CPU而变快。但是`test/test_fork.py`会因为多核而变快
用kill杀出一个子线程后，会导致进程崩溃

## 性能

1. time.time 来判断是否刷新缓存，1秒能执行753万次

    if time.time() > start :
        refresh()


2. random.random 来判断， 1秒能执行977万次


    if random.random() > 0.0000001:
        refresh()


[library-reference]: https://docs.python.org/3/library/index.html
[base64]: https://docs.python.org/3/library/base64.html
[subprocess]: https://docs.python.org/3/library/subprocess.html
[bz2]: https://docs.python.org/3/library/bz2.html#examples-of-usage
```
