# tutorial
[官网](https://docs.python.org/3/tutorial/index.html)
* [Other Useful Library 其他有用的包](./other_useful_library/README.md)
* [official documents 官网文档](https://docs.python.org/3/)
* [python tips 小技巧](http://book.pythontips.com/en/latest/index.html)
* [awesome python](https://github.com/vinta/awesome-python)
* [github链接](https://github.com/ramwin/python-reference/)


## Data Structures 基础类型
其实这个是Library Reference的内容


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


# [Package 打包](https://packaging.python.org/en/latest/tutorials/packaging-projects/#creating-the-package-files)

* `setup.py`示例:
[文档](https://packaging.python.org/en/latest/tutorials/packaging-projects/#creating-the-package-files)

    ```python
    from setuptools import setup
    setup(
        # 必选
        name="包名",
        version="0.0.1",

        # 可选
        package_data = {
            '': ['*.png', '*.json'],  # 把包里面的png和json放入包
        },
        data_files=[('README.md', ['README.md'])],
        install_requires=[
            '<dependency_name> @ git+ssh://git@github.com/<user>/<repo_name>@<ref>',  # 依赖一个git仓库
        ]
    )
    ```

* 发布

```shell
python3 setup.py sdist bdist_wheel
twine upload dist/*
```

# 其他有用的包 Other Useful Library
## 7z

[官网](https://github.com/miurahr/py7zr)


    import py7zr
    archive = py7zr.SevenZipFile('sample.7z', mode='r')
    archive.extractall(path='/tmp')


## airflow
[github链接](https://github.com/ramwin/airflowtest/README.md)

## beautifulsoup4 *用来解析html文件*
[官网](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#id5)
    * 安装: `pip3 install beautifulsoup4`
    * [文档整理](./other_useful_library/beautifulsoup.md)

## [bitstring](https://github.com/scott-griffiths/bitstring)
把二进制转化成01
```python3
from bitstring import BitArray
BitArray(b"123").bin  # '001100010011001000110011'

```

## captcha  

[示例](./other_useful_library/captcha_test.py)
*生成验证码*
## celery
* *用来执行异步脚本*
这个软件在linux-reference里面  
    * [官网](http://docs.celeryproject.org/en/latest/index.html)
    * [github在线链接](https://github.com/ramwin/linux-reference#celery)

## [click](./other_useful_library/click.md) *用python写shell命令command*

## [datetime-month](https://github.com/yitistica/month)
安装: `pip install datetime-month`

```python
from month import XMonth
month = XMonth(2022, 11)
month.first_day()
```

## diff-match-patch
比较文字不同

## eth_typing
数字货币的类

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

## [filelock](./library_reference/README.md)

## [flake8] *检测python代码是不是满足pep8*
## [flask](./other_useful_library/flask.md) *轻量级http服务器*

## [GitPython](./other_useful_library/README.md#git)

## [hexbytes](./other_useful_library/README.md#hexbytes)

## [Humanfriendly](./other_useful_library/README.md)
转化尺寸

## [imapclient](other_useful_library/imapclient.md)
很好用的邮件客户端

* [ics](https://pypi.org/project/ics/) *日历，行程 calendar*
* [ipdb](./other_useful_library/ipdb.md) *断点来检测查看源码和运行状态*

## ipython
非常好用的交互式shell
* 在 `~/.ipython/profile_default/startup/` 下创建脚本可以默认import一些包

* [itchat](https://github.com/littlecodersh/ItChat)  *微信机器人*
* [iptools] *处理IP地址的包*

## [jmespath](https://github.com/jmespath/jmespath.py)
```
>>> jmespath.search("foo.bar", {"foo": {"bar": "baz"}})
'baz'
```

* [jinja模板渲染](./other_useful_library/jinjia.md)
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

```python
from MySQLdb.connections import Connection
db = Connection(db="test")
c = db.cursor()

res = c.execute("select * from pets");
print(c.fetchall())
>>> ((1, 'cat'), (2, 'cat'), (3, 'dogs'), (13, 'dog'), (14, 'dog'), (15, 'dog'), (21, 'dog'), (22, 'dog'))

res = c.execute("insert into pets values (null, 'dog')");
# 注意即使没有commit, 数据库id也会自增. 如果一次没有commit, 下次commit时,id就不是连续的了
db.commit()

# 使用连接池
https://github.com/discover-python-channel/youtube-content/blob/main/mysql_connection_pooling/python/import_fake_data.py

from mysql.connector import pooling
cnxpool = pooling.MySQLConnectionPool(pool_name="poolname", pool_size=20. autocommit=True, username...)
connection = cnxpool.get_connection()
cursor = connection.cursor()
cursor.execute(sql)
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

```python
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
# 截取前5秒的mp4文件
ffmpeg_extract_subclip("movie.mp4", 0, 5, targetname="test.mp4")
```

## numpy
* [linspace 获取整数](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
```
>>> numpy.linspace(0, 100, 3, dtype='int')
array([0, 50, 100])
```

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
    error = stderr.read().decode("utf8")
    if error:
        raise Exception(error)
    print(stdout.read())
    ```

## [pdf2image](https://github.com/Belval/pdf2image): *把pdf转化成图片的库*
[测试代码](./other_useful_library/pdfconvert.py)
```
from pdf2image import convert_from_path
convert_from_path(pdf_path, output_folder=path, fmt='png')
images = convert_from_path(pdf_path)
```

## [pdfminer](https://github.com/euske/pdfminer) *解析pdf的包，好用*
## [peewee](./other_useful_library/peewee.md) *简单而轻量级的sqlite3 orm，和django很像*

## [pendulum](library_reference/datetime时间.md)

## [PID](./other_useful_library/README.md#pid)
流程控制算法

## [pillow](./pillow.md)

## [pip](./other_useful_library/README.md#pip)
包管理程序

## [psutil](./other_useful_library/README.md#psutil)
获取系统信息

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

## pydash
模拟lodash的
```
# pip install pydash
import pydash
pydash.get(obj, "a.b.1", 1)  # 默认返回1, 但是key存在为None会返回None
```

## [pylint](other_useful_library/pylint.md)

## [pydub](https://github.com/jiaaro/pydub) *编辑mp3的包*
* 安装依赖: `apt install libav-tools ffmpeg`
* [示例](./other_useful_library/mp4tomp3.py)
* 基础:

```
import math
from pydub import AudioSegment
song = AudioSegment.from_mp3('origin.mp3')
song[10*1000: 40*1000].export('target.mp3')
```
* [把一个视频切割成很多个小的mp3](./other_useful_library/mp4tomp3.py)

## [pyenv](./other_useful_library/pyenv.md)
python虚拟化，通过制定python路径，来在服务器安装多个python

## pyftpdlib ftp客户端和服务端
[文档](https://pyftpdlib.readthedocs.io/en/latest/tutorial.html)
添加`-w`参数可以允许写入
```
# 直接启动一个ftplib
python -m pyftpdlib  # 默认匿名登录, 端口号2121
python -m pyftpdlib --port=1223 --username=admin --password=123  -d ~/Downloads
# 后台启动
python script/启动ftp.py
```



## [PyPDF2](https://pythonhosted.org/PyPDF2/) *对中文支持不友好*

## pyperclip *控制系统剪切板*
```python
pyperclip.copy('ew') # 把ew放入剪切板
```

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
    dotenv_values(),
}
```

* 设置环境变量  
```
dotenv set EMAIL foo@example.org
dotenv list
```

## [pytz](./library_reference/datetime时间.md)  *时区*
## [PyWinMouse](https://pypi.org/project/PyWinMouse/)  *windows下操作鼠标*
## [qiniu](./qiniu.md)  *七牛的接口*
## [requests](./other_useful_library/requests.md) *发送http请求*
## [rsa](./other_useful_library/rsa.md) *使用rsa加密*
## [scp](https://github.com/jbardin/scp.py)
用scp传输文件
```
from paramiko import SSHClient
from scp import SCPClient
with SSHClient() as ssh:
    ssh.load_system_host_keys()
    ssh.connect("ramwin.com", compress=True)  # https://github.com/jbardin/scp.py/pull/19
    with SCPClient(ssh.get_transport()) as scp:
        scp.put(<本地文件>, <远程路径>)
        scp.get(<远程路径>, <本地文件>, recursive=True)
```

## [scrapy](./scrapy/README.md)

## [sortedcontainers](https://github.com/grantjenks/python-sortedcontainers)

    pip install sortedcontainers
    from sortedcontainers import SortedList
    s1 = SortedList()
    s1.add(0)
    s1.update([2, 1, 3])

## [sortedsets](https://github.com/tailhook/sortedsets)
模仿redis的sorted set做的自动排序的set

```
sudo pip3 install sortedsets
>>> from sortedsets import SortedSet
>>> ss = SortedSet()
>>> for i in range(1, 1000):
>>>     ss['player' + str(i)] = i*10 if i % 2 else i*i
ss.by_score[470:511]
>>> ss.index('player20'), ss.index('player21')
400, 210
```

## [python-syncthing](https://github.com/blakev/python-syncthing)
```
import time

from dotenv import dotenv_values, load_dotenv
from syncthing import Syncthing

load_dotenv()

folder = "目录id"
client = syncthing.Syncthing(dotenv_values()["APIKEY"])
client.db.scan(folder, sub="要同步的目录")
while client.db.completion(remote_device, folder) != 100:
    time.sleep(10)
```


* ## ~~[srt](http://srt.readthedocs.io/en/latest/api.html)*因为缺少shift功能而改成用pysrt*~~
## [visidata](other_useful_library/visidata.md)

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

