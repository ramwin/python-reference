#### Xiang Wang @ 2017-02-10 15:30:51

### 基础
* 参考资料
    * [官网教程](https://docs.python.org/3/)
    * [python tips](http://book.pythontips.com/en/latest/index.html)
* [字符串string](./string.md)
    * [unicode表](https://unicode-table.com/cn/#samaritan)
* [列表list](list.md)
    * [for else](http://book.pythontips.com/en/latest/for_-_else.html)
        ```
        for item in container:
            if search_something(item):
                process(item)
                break
        else:
            not_found_in_container()
        ```
* [集合set](set.md)
* [时间](time时间.md)
* enumerate
```
    enumerate(['a','b','c'])  // [(0, 'a'), (1, 'b'), (2, 'c')]  但是不是list， 而是一个enumerate对象
```
* [执行顺序](https://docs.python.org/3/reference/expressions.html#evaluation-order)
```
    ()  # 括号内
    **  # 指数
    +x, -x  # 负数
    in, not in, is, is not, <, <=, >, >=  # 比较
    not x  #
    and  #
    or  # and 和 or不是同样的哦。
```
* [Exception报错](./exception.md) [官网](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)
* [class](./class/README.md)
    * [property](./class/property.md) [示例](./class/property.py)


### 包参考
* [csv](./csv.md)
* [re正则表达式](./rematch正则表达式.md)
* [collections](./collections.md)
* [fractions](https://docs.python.org/2/library/fractions.html#fractions.Fraction)
```
    from fractions import Fraction
    f = Fraction(1,3)
    print("1/3 = %d/%d" % (f.numerator, f.denominator))
```
* [json](./json.md)

### 其他包
* [click](./click.md) *用python写shell命令*
* [flake8] *检测python代码是不是满足pep8*
* [flask](./flask.md) *轻量级http服务器*
* [jinja模板渲染](./jinjia.md)
* [mongoengine](./mongoengine.md) *把mongodb当作sql用。那你为什么不直接用mysql啊*
* [openpyxl](./openpyxl.md)
* [redis](./redis.md) *使用Redis缓存*
* [requests](./requests.md) *发送http请求*
* [rsa](./rsa.md) *使用rsa加密*
* [scrapy](./scrapy/README.md)
* [peewee](./peewee.md) *简单而轻量级的sqlite3 orm，和django很像*
* [pillow](./Pillow.md)
* pip *快速安装包*
    `pip install -i https://pypi.tuna.tsinghua.edu.cn/simple django==1.11`
* pip *快速安装包*
    `pip install -i https://pypi.tuna.tsinghua.edu.cn/simple django==1.11`
* [pydub](https://github.com/jiaaro/pydub) *编辑mp3的包*
    * 安装依赖: `apt install libav-tools ffmpeg`
    * 基础:
    ```python
    from pydub import AudioSegment
    song = AudioSegment.from_mp3('origin.mp3')
    song[10*1000: 40*1000].export('target.mp3')
    ```
* pyperclip *控制系统剪切板*
    pyperclip.copy('ew') # 把ew放入剪切板
* [qiniu](https://developer.qiniu.com/kodo/sdk/1242/python) *调用七牛的api上传文件*
* [urllib](./urllib.md) *处理url*
* [word2html](https://github.com/bradmontgomery/word2html)  *把word转化成html*
* [flake8] *检测python代码是不是满足pep8*
* [yapf] *把python的代码格式化*
