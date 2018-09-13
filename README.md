*Xiang Wang @ 2017-02-10 15:30:51*

# 目录
* [Language Reference](#language-reference)
* [Library Reference](#library-reference-内置库参考)
* [Other Useful Library](#other-useful-library)
* [official documents 官网文档](https://docs.python.org/3/)
* [python tips 小技巧](http://book.pythontips.com/en/latest/index.html)

# Language Reference
* ## [string](./string.md)
    * [unicode table](https://unicode-table.com/cn/#samaritan)
    * ### [format](./string.md#format)

* ## [列表list](list.md)
    * [基础]
        ```
        >>> a = ['a', 'b', 'c']
        >>> a.insert(1, 'd')
        ['a', 'd', 'b', 'c']
        ```
    * [for else](http://book.pythontips.com/en/latest/for_-_else.html)
        ```
        for item in container:
            if search_something(item):
                process(item)
                break
        else:
            not_found_in_container()
        ```
    * sorted
        ```
        sorted(l, key=lambda x: x['value'])  # 根据value进行排序
        ```
    * [自定义可迭代](./for.md)
* ## 字典dict
```python3
    a_dict = {'foo': 'bar', 'my': 'a-only'}
    b_dict = {'foo': 'b', 'you': 'b-only'}
    a_dict.update(b_dict)
    >>> a_dict
    {'foo': 'b', 'my': 'a-only', 'you': 'b-only'}
```
* ## [集合set](set.md)
* ## [函数](function.md)
* ## [执行顺序](https://docs.python.org/3/reference/expressions.html#evaluation-order)
```
    ()  # 括号内
    **  # 指数
    +x, -x  # 负数
    in, not in, is, is not, <, <=, >, >=, !=  # 比较
    not x  #
    and  #
    or  # and 和 or不是同样的哦。
```
* ## [class](./class/README.md)
    * [官网文档 TODO](https://docs.python.org/3.6/tutorial/classes.html)
    * ### 属性
        * `__module__` : class的模块
        * `__name__` : class的name
    * ### [property](./class/property.md) [示例](./class/property.py)
* ## enumerate
```
    enumerate(['a','b','c'])  // [(0, 'a'), (1, 'b'), (2, 'c')]  但是不是list， 而是一个enumerate对象
```
* ## [Exception报错](./exception.md) [官网](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)
* ## [magic method魔法方法](./magic_methods/README.md)


# [Library Reference 内置库参考](https://docs.python.org/3/library/index.html)
1. [ ] Introduction
2. [ ] Built-in Functions
3. [ ] Built-in Constants
4. [ ] Built-in Types
5. [ ] Built-in Exceptions
6. ## [Text Processing Services](https://docs.python.org/3/library/text.html)
    2. ### [re -- Regular expression operations](./re.md)

7. [ ] Binary Data Services

8. ## [Data Types](https://docs.python.org/3/library/datatypes.html)
    1. ### [datetime](./datetime时间.md)
    3. ### [collections](./collections.md)

9. ## Numeric and Mathematical Modules
    5. [fractions](https://docs.python.org/2/library/fractions.html#fractions.Fraction)
    ```
        from fractions import Fraction
        f = Fraction(1,3)
        print("1/3 = %d/%d" % (f.numerator, f.denominator))
    ```
    6. random — Generate pseudo-random numbers
        * random.randrange(stop)
        * random.randrange(start, stop[, step])  
        return value from start(included) to stop(excluded)
        * random.randint(start, stop)  
        return value from start(included) to stop(included)
    7. statistics — Mathematical statistics functions 数学分析
        * [statistics.mean](https://docs.python.org/3/library/statistics.html#statistics.mean)
        * [statistics.stdev](https://docs.python.org/3/library/statistics.html#statistics.stdev)
        * statistics.StatisticsError

10. [ ] Functional Programming Modules

11. ## [File and Directory Access](https://docs.python.org/3/library/filesys.html)
    2. ### [os.path](https://docs.python.org/3/library/os.path.html)
        * os.path.abspath
        * `os.path.isfile`:  
            *Return True if path is an existing regular file. This follows symbolic links, so both islink() and isfile() can be true for the same path.*
    6. ### [tempfile](https://docs.python.org/3/library/tempfile.html#examples)
        ```
        import tempfile
        fp = tempfile.TemporaryFile(mode='w+b', encoding=None)
        fp.write(b'Hello world!')
        ```

12. [ ] Data Persistence
    * ### [pickle](https://docs.python.org/3/library/pickle.html) *把python的对象序列化成字符串*
13. [ ] Data Compression and Archiving
    * [zipfile](./zip.md) *处理zip压缩包*
14. ## [File Formats](https://docs.python.org/3/library/fileformats.html)
    1. ### [csv](./csv.md)
        * [source code](https://github.com/python/cpython/blob/3.6/Lib/csv.py)
    2. [ ] configparser
    3. [ ] netrc
    4. [ ] xdrlib
    5. [ ] plistlib
15. [ ] Cryptographic Services

16. ## [Generic Operating System Services](https://docs.python.org/3/library/allos.html)
    1. ### [os](https://docs.python.org/3/library/os.html)
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
    4. [ ] argparse
    5. [ ] getopt
    6. ### [logging日志处理](./log/README.md)
    9. [ ] to be continued

17. [ ] Concurrent Execution
18. [ ] contextvars — Context Variables
19. [ ] Interprocess Communication and Networking
20. ## Internet Data Handling
    2. ### JSON
        * [官方教程](https://docs.python.org/3/library/json.html)
        * 代码内使用
        ```
            import json
            data = {}
            text = json.dumps(data)
            data = json.loads(text)

            file_obj = open('source/test.json','r')
            data = json.load(file_obj)

            file_obj = open('source/test.json', w')
            json.dump(obj, file_obj, ensure_ascii=False)
        ```
        * 命令行使用
        ```
            python -m json.tool <filename>
            import pprint
            pprint.pprint(data, depth=4, indent=4)
        ```
        * 报错
        json.decoder.JSONDecodeError(python3), ValueError(python2)
    6. ### base64
    ```
    b = base64.encodebytes('我'.encode('utf8')) # 只有二进制才能encode,结果还是bytes
    b = base64.encodestring('我'.encode('utf8')) # 查了源码，果然这个是为了兼容python2的语法。以后避免使用这个方法
    b = base64.encodestring('我')   # python2里面的str就是二进制,结果是str(仍然是二进制)
    ```
    * [ ] to be continued
21. [ ] Structed Markup Processing Tools
22. [ ] Internet Protocols and Support
27. Development Tools
    4. ### [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
        * [assets methods](https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug)  
            * assert**Equal**, assertNotEqual, 
            * assert**True**, assertFalse, 
            * assert**Is**, assertIsNot, 
            * assert**IsNone**, assertIsNotNone, 
            * assert**In(a, b)**, assertNotIn
            * assert**IsInstance**, assertNotIsInstance
100. [ ] to be continued


# Other Useful Library
* ## beautifulsoup4 *用来解析html文件*
    * [官网](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#id5)
    * 安装: `pip3 install beautifulsoup4`
    * [文档整理](./other_useful_library/beautifulsoup.md)
* ## [click](./click.md) *用python写shell命令*
* ## [faker](https://github.com/joke2k/faker)  *use fake to create a lot of name of text*  
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
* ## [flake8] *检测python代码是不是满足pep8*
* ## [flask](./flask.md) *轻量级http服务器*
* ## [ics](https://pypi.org/project/ics/) *日历，行程 calendar*
* ## [itchat](https://github.com/littlecodersh/ItChat)  *微信机器人*
* ## [iptools] *处理IP地址的包*
* ## [jinja模板渲染](./jinjia.md)
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
* ## [mongoengine](./mongoengine.md) *把mongodb当作sql用。那你为什么不直接用mysql啊*
* ## [openpyxl](./openpyxl.md) *处理excel*
* ## [pdfminer](https://github.com/euske/pdfminer) *解析pdf的包，好用*
* ## [peewee](./peewee.md) *简单而轻量级的sqlite3 orm，和django很像*
* ## [pillow](./Pillow.md)
* pip *快速安装包*
    `pip install -i https://pypi.tuna.tsinghua.edu.cn/simple django==1.11`
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
    * 基础:
    ```python
    from pydub import AudioSegment
    song = AudioSegment.from_mp3('origin.mp3')
    song[10*1000: 40*1000].export('target.mp3')
    ```
* ## [PyPDF2](https://pythonhosted.org/PyPDF2/) *对中文支持不友好*
* pyperclip *控制系统剪切板*
    pyperclip.copy('ew') # 把ew放入剪切板
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
* ## [qiniu](https://developer.qiniu.com/kodo/sdk/1242/python) *调用七牛的api上传文件*
* ## [redis](./redis.md) *use redis db*
* ## [requests](./requests.md) *发送http请求*
* ## [rsa](./rsa.md) *使用rsa加密*
* ## [scrapy](./scrapy/README.md)
* ## [srt](http://srt.readthedocs.io/en/latest/api.html)
    * 基础:
    ```python
    subs = list(srt.parse(text))
    for sub in subs:
        print(sub.content)  # 输出字幕的内容
    ```
* ## [urllib](./urllib.md) *处理url*
* ## [watchdog](https://pypi.org/project/watchdog/) *监控文件变化*
* ## [wechatpy](https://github.com/jxtech/wechatpy) *和微信的接口*
    * 基础
    ```
    from wechatpy.client import WeChatClient
    from wechatpy.session.redisstorage import RedisStorage
    from redis import Redis
    redis_client = Redis.from_url('redis://127.0.0.1:6379/0')
    session_interface = RedisStorage(redis_client, prefix="wechatpy")
    wechat_client = WeChatClient(
        app_id, secret, session=session_interface
    )
    ```
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
