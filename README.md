*Xiang Wang @ 2017-02-10 15:30:51*

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

# [Language Reference](https://docs.python.org/3/reference/index.html)
## Exceution model
* [Exception报错](./exception.md)
[官网](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)

## Expressions
* ### [magic method魔法方法](./magic_methods/README.md)
* Evaluation order 执行顺序
[官网](https://docs.python.org/3/reference/expressions.html#evaluation-order)
```
    ()  # 括号内
    **  # 指数
    +x, -x  # 负数
    in, not in, is, is not, <, <=, >, >=, !=  # 比较
    not x  #
    and  #
    or  # and 和 or不是同样的哦。
```

## Simple statements 简单语句
11. [import机制](http://www.jianshu.com/p/b963782f59e9) [import文档](https://docs.python.org/3/reference/simple_stmts.html#the-import-statement)
12. [global](language_reference/global_test.py)

## Compound statements 复合语句
* [函数](function.md)
[官网](https://docs.python.org/3/reference/compound_stmts.html#function-definitions)
    * [decorator装饰器](http://www.cnblogs.com/huxi/archive/2011/03/01/1967600.html)
    * [decorator.py](decorator装饰器.py)
* [class](./class/README.md)
[官网文档 TODO](https://docs.python.org/3.6/tutorial/classes.html)
    * 属性
        * `__module__` : class的模块
        * `__name__` : class的name
    * [property](./class/property.md) [示例](./class/property.py)


# [Library Reference 内置库参考][library-reference]
1. [x] Introduction
2. [Built-in Functions](./library_reference/built_in_functions内置函数.md)
    * all
    * any
    * divmod
    * enumerate
    ```
    enumerate(['a','b','c'])  // [(0, 'a'), (1, 'b'), (2, 'c')]  但是不是list， 而是一个enumerate对象
    ```
3. Built-in Constants
4. Built-in Types
    * [Set集合](./set.md)
    * ### [Mapping Types -- dict 字典参考](./library_reference/built_in_types内置数据类型.md)
5. [ ] Built-in Exceptions
6. [Text Processing Services](https://docs.python.org/3/library/text.html)
    2. ### [re -- Regular expression operations 正则表达式](./re.md)
    [test regrex 在线测试](https://regex101.com/#python)

7. [ ] Binary Data Services

8. ## [Data Types](https://docs.python.org/3/library/datatypes.html)
    1. [datetime](./datetime时间.md)
    2. [ ] [calendar](https://docs.python.org/3/library/calendar.html)
    3. [collections](./collections.md)
    4. [collections.abc](./collections.md#collections.abc)
    5. [ ] heapq: *heap queque algorithm*
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

9. Numeric and Mathematical Modules
    2. [math](https://docs.python.org/3/library/math.html)
    ```
    math.ceil(x) 大于等于x的最小的整数, 使用 __ceil__ 方法，可以让一个对象支持这个函数
    math.floor(x) 小于等于x的最大的整数, 使用 __floor__ 方法，可以让一个对象支持这个函数
    ```
    5. [fractions](https://docs.python.org/2/library/fractions.html#fractions.Fraction)
    ```
        from fractions import Fraction
        f = Fraction(1,3)
        print("1/3 = %d/%d" % (f.numerator, f.denominator))
    ```
    6. random — Generate pseudo-random numbers
        * random.choice(list)  # choose one value from list
        * random.randrange(stop)
        * random.randrange(start, stop[, step])  
        return value from start(included) to stop(excluded)
        * random.randint(start, stop)  
        return value from start(included) to stop(included)
        * random.sample(list, k)  # choose k's value from list
    7. statistics — Mathematical statistics functions 数学分析
        * [statistics.mean](https://docs.python.org/3/library/statistics.html#statistics.mean)
        * [statistics.stdev](https://docs.python.org/3/library/statistics.html#statistics.stdev)
        * statistics.StatisticsError

10. [ ] Functional Programming Modules

11. ## [File and Directory Access](https://docs.python.org/3/library/filesys.html)
    2. [os.path](library_reference/os.md)
    6. [tempfile](https://docs.python.org/3/library/tempfile.html#examples)
        ```
        import tempfile
        fp = tempfile.TemporaryFile(mode='w+b', encoding=None)
        fp.write(b'Hello world!')
        ```

12. [ ] Data Persistence
    * ### [pickle](https://docs.python.org/3/library/pickle.html) *把python的对象序列化成字符串*
13. [ ] Data Compression and Archiving
    * [zipfile](./zip.md) *处理zip压缩包*
14. File Formats
[官网](https://docs.python.org/3/library/fileformats.html)
    1. ### [csv](./csv.md)
        * [source code](https://github.com/python/cpython/blob/3.6/Lib/csv.py)
    2. ### [configparser](./config.md) 配置文件
    3. [ ] netrc
    4. [ ] xdrlib
    5. [ ] plistlib
15. [ ] Cryptographic Services

16. ## [Generic Operating System Services](https://docs.python.org/3/library/allos.html)
    1. [os](https://docs.python.org/3/library/os.html)
        * os.scandir
        Better performance than os.listdir
        ```
        filter(lambda x: x.is_dir(), os.scandir())  # show all the directory entry
        ```

        * os.listdir  
        Return a list containing the names of the entries in the directory given by path. 
        * [以前的参考](./os.md)
    2. [ ] io
    3. [ ] time
    4. [argparse](./library_reference/argparse.md)
    这个用来解析python的命令
    5. [ ] getopt
    6. ### [logging日志处理](./logging/README.md)
    9. [ ] to be continued

17. [ ] Concurrent Execution
18. [ ] contextvars — Context Variables
19. [ ] Interprocess Communication and Networking
20. ## Internet Data Handling
    2. ### [JSON](./library_reference/json.md)
    6. base64
    ```
    b = base64.encodebytes('我'.encode('utf8')) # 只有二进制才能encode,结果还是bytes
    b = base64.encodestring('我'.encode('utf8')) # 查了源码，果然这个是为了兼容python2的语法。以后避免使用这个方法
    b = base64.encodestring('我')   # python2里面的str就是二进制,结果是str(仍然是二进制)
    ```
    * [ ] to be continued
21. [ ] Structed Markup Processing Tools
22. ## Internet Protocols and Support
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
30. ## Python Runtime Services 和编译器,环境有关的服务
[官网](https://docs.python.org/3/library/python.html)
    10. ### traceback -- Print or retrieve a stack traceback
    [官网](https://docs.python.org/3/library/traceback.html)
    ```
    traceback.print_stack()  # 直接print出stack
    log = traceback.format_exc()  # 记录报错的stack
    stack = traceback.format_stack()  # 记录当前的stack
    ```
33. Python Language Services
    2. ast
    `ast.literal_eval`: "savely evalute an expression node or a string containing a Python literal or container display."
    3. [ ] to be continued
100. [ ] to be continued


# Other Useful Library
* beautifulsoup4 *用来解析html文件*
[官网](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#id5)
    * 安装: `pip3 install beautifulsoup4`
    * [文档整理](./other_useful_library/beautifulsoup.md)
* [captcha](./other_useful_library/captcha_test.py) *生成验证码*
* ## celery *用来执行异步脚本*
    * [官网](http://docs.celeryproject.org/en/latest/index.html)
    * [github在线链接](https://github.com/ramwin/linux-reference#celery)
    * [本地链接](../linux-reference/README.md#celery)
* [click](./other_useful_library/click.md) *用python写shell命令*
* [faker](https://github.com/joke2k/faker)  *use fake to create a lot of name of text*  
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
* [flake8] *检测python代码是不是满足pep8*
* [flask](./flask.md) *轻量级http服务器*
* [ics](https://pypi.org/project/ics/) *日历，行程 calendar*
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
* [mongoengine](./other_useful_library/mongoengine.md) *把mongodb当作sql用。那你为什么不直接用mysql啊*
* [moviewpy](https://github.com/Zulko/moviepy) *操作mp4的包*
```
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
# 截取前5秒的mp4文件
ffmpeg_extract_subclip("movie.mp4", 0, 5, targetname="test.mp4")
```
* [openpyxl](./openpyxl.md) *处理excel*
* [pdfminer](https://github.com/euske/pdfminer) *解析pdf的包，好用*
* [peewee](./peewee.md) *简单而轻量级的sqlite3 orm，和django很像*
* [pillow](./pillow.md)
* pip *快速安装包*  
`pip install -i https://pypi.tuna.tsinghua.edu.cn/simple django==1.11`  
`pip install -i https://pypi.org/simple django==1.11`
```
export LC_ALL="en_US.UTF-8"  # 出现乱码
export LC_CTYPE="en_US.UTF-8"
```
* ## [pycharm]
    * 快捷键:
        * 界面工具查看
            * 命令行: `alt+F12`
        * 代码编辑
            * ## [折叠代码](https://www.jetbrains.com/help/pycharm/code-folding-2.html)
            * `Ctrl+B 或者 Ctal+click`: 查看一个函数的定义
            * `Ctrl+Q`: 查看一个函数的文档
            * `查看文件结构`: `alt+7` or `ctrl+F12`
            * `shift+F6`: *重构函数名称，全局变化他的名字*
        * 跳转
            * `ctrl+shift+backspace`: 查看上期编辑的地方
    * ## [django支持](https://www.jetbrains.com/help/pycharm/running-tasks-of-manage-py-utility.html)
* ## [pycrypto]
    * 安装:
        * windows: 先去[下载visual c++ 9.0](http://aka.ms/vcpython27)，然后再 `pip install pycrypto`
* ## [pydub](https://github.com/jiaaro/pydub) *编辑mp3的包*
    * 安装依赖: `apt install libav-tools ffmpeg`
    * [示例](./other_useful_library/mp4tomp3.py)
    * 基础:
    ```python
    import math
    from pydub import AudioSegment
    song = AudioSegment.from_mp3('origin.mp3')
    song[10*1000: 40*1000].export('target.mp3')
    # 把一个视频切割成很多个小的mp3 ../other_useful_library/mp4tomp3.py
    ```
* ## [PyPDF2](https://pythonhosted.org/PyPDF2/) *对中文支持不友好*
* pyperclip *控制系统剪切板*
    pyperclip.copy('ew') # 把ew放入剪切板
* ## [pysrt](./other_useful_library/README.md#pysrt)  *控制srt字幕*
* ## [pytz](https://pythonhosted.org/pytz/)  *时区*
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
* ## [PyWinMouse](https://pypi.org/project/PyWinMouse/)  *windows下操作鼠标*
* ## [qiniu](./qiniu.md)  *七牛的接口*
* ## [redis](./redis.md) *use redis db*
* ## [requests](./other_useful_library/requests.md) *发送http请求*
* ## [rsa](./other_useful_library/rsa.md) *使用rsa加密*
* ## [six](./other_useful_library/six.md) `python2和python3兼容的库`
* ## [scrapy](./scrapy/README.md)
* ## ~~[srt](http://srt.readthedocs.io/en/latest/api.html)*因为缺少shift功能而改成用pysrt*~~
* ## [urllib](./urllib.md) *处理url*
* ## [virtualenv](https://virtualenv.pypa.io/en/stable/)
```
virtualenv --system-site-packages -p /bin/python ENV
```
* ## [watchdog](https://pypi.org/project/watchdog/) *监控文件变化*
* ## websocket [websocket 客户端](https://github.com/websocket-client/websocket-client)
* ## [wechatpy](./other_useful_library/wechatpy.md) *和微信的接口*
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

* ## [yapf] *把python的代码格式化*
## 其他不重要的包


# 其他
* socket.gethostname()    # 获取当前主机的主机名
* uuid.getnote()    # 获取本机的MAC地址  
mac=uuid.UUID(int = node).hex[-12:]

## [设计模式](./设计模式.md)
[runoob教程](http://www.runoob.com/design-pattern/factory-pattern.html)


[library-reference]: https://docs.python.org/3/library/index.html
