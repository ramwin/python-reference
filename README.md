*Xiang Wang @ 2017-02-10 15:30:51*

# Basic
* Reference
    * ## [official documents](https://docs.python.org/3/)
    * ## [python tips](http://book.pythontips.com/en/latest/index.html)
* ## [string](./string.md)
    * ## [unicode table](https://unicode-table.com/cn/#samaritan)
    * [format](https://pyformat.info/)
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
* ## [时间](time时间.md)
* ## [函数](function.md)
* ## [执行顺序](https://docs.python.org/3/reference/expressions.html#evaluation-order)
```
    ()  # 括号内
    **  # 指数
    +x, -x  # 负数
    in, not in, is, is not, <, <=, >, >=  # 比较
    not x  #
    and  #
    or  # and 和 or不是同样的哦。
```
* ## [class](./class/README.md)
    * [官网文档 TODO](https://docs.python.org/3.6/tutorial/classes.html)
    * ## 属性
        * `__module__` : class的模块
        * `__name__` : class的name
    * ## [property](./class/property.md) [示例](./class/property.py)
* ## enumerate
```
    enumerate(['a','b','c'])  // [(0, 'a'), (1, 'b'), (2, 'c')]  但是不是list， 而是一个enumerate对象
```
* ## [Exception报错](./exception.md) [官网](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)
* ## [magic method魔法方法](./magic_methods/README.md)


# [Library Reference](https://docs.python.org/3/library/index.html)
1. [ ] Introduction
2. [ ] Built-in Functions
3. [ ] Built-in Constants
4. [ ] Built-in Types
5. [ ] Built-in Exceptions
6. [ ] Text Processing Services
    2. ### [re -- Regular expression operations](./re.md)
7. [ ] Binary Data Services
8. ## [Data Types](https://docs.python.org/3/library/datatypes.html)
    3. ### [collections](./collections.md)
9. [ ] Numeric and Mathematical Modules
10. [ ] Functional Programming Modules
11. ## [File and Directory Access](https://docs.python.org/3/library/filesys.html)
    2. ### [os.path](https://docs.python.org/3/library/os.path.html)
        * os.path.abspath
        * `os.path.isfile`:  
            *Return True if path is an existing regular file. This follows symbolic links, so both islink() and isfile() can be true for the same path.*
12. [ ] Data Persistence
13. [ ] Data Compression and Archiving
14. ## [File Formats](https://docs.python.org/3/library/fileformats.html)
    1. ### [csv](./csv.md)
        * [source code](https://github.com/python/cpython/blob/3.6/Lib/csv.py)
    2. [ ] configparser
    3. [ ] netrc
    4. [ ] xdrlib
    5. [ ] plistlib
15. [ ] Cryptographic Services
16. [ ] Generic Operating System Services
17. [ ] Concurrent Execution
18. [ ] Interprocess Communication and Networking
19. [ ] Internet Data Handling
20. [ ] Structed Markup Processing Tools
21. [ ] Internet Protocols and Support
22. [ ] to be continued


* ## [fractions](https://docs.python.org/2/library/fractions.html#fractions.Fraction)
```
    from fractions import Fraction
    f = Fraction(1,3)
    print("1/3 = %d/%d" % (f.numerator, f.denominator))
```
* ## json
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
* ## [os](./os.md)
* ## [pickle](https://docs.python.org/3/library/pickle.html) *把python的对象序列化成字符串*
* ## [tempfile](https://docs.python.org/3/library/tempfile.html#examples)
    ```
    import tempfile
    fp = tempfile.TemporaryFile(mode='w+b', encoding=None)
    fp.write(b'Hello world!')
    ```

* ## [zipfile](./zip.md) *处理zip压缩包*

# Other Useful Library
* ## beautifulsoup4 *用来解析html文件*
    * [官网](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#id5)
    * 安装: `pip3 install beautifulsoup4`
    * [文档整理](./beautifulsoup.md)
* ## [click](./click.md) *用python写shell命令*
* ## [flake8] *检测python代码是不是满足pep8*
* ## [flask](./flask.md) *轻量级http服务器*
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
* ## [yapf] *把python的代码格式化*
