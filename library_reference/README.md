[所有内置库一览](https://docs.python.org/3/library/index.html)

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

## [Functional Programming Modules](https://docs.python.org/3/library/functional.html)

### [itertools](./itertools.md)

### functools: 对于函数和可调用对象的执行操作
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

### [os](https://docs.python.org/3/library/os.html)
```python
# 获取当前目录  
os.getcwd()
os.path.abspath('.')

# 是否是目录
os.path.isdir("<path>")

# 切换目录
os.chdir('Pictures')

# 遍历文件
os.listdir()

# 删除目录
import shutil
shutil.rmtree('<directory>')
```


#### [Process Parameters](https://docs.python.org/3/library/os.html#process-parameters)


#### [File Descriptor Operations](https://docs.python.org/3/library/os.html#file-descriptor-operations)

#### [Files and Directories](https://docs.python.org/3/library/os.html#files-and-directories)
* [ ] os.chroot(path)
* os.fchdir(fd)  
等于`os.chdir`
* os.getcwd()  
返回当前工作目录: `'/home/wangx/github/python-reference'`
* os.getcwdb()
返回当前工作目录的二进制: `b'/home/wangx/github/duishang_design/\xe7\xbd\x91\xe9\xa1\xb5'`
* os.listdir(path=".")
Return a list containing the names of the entries in the directory given by path. 
* os.scandir(path=".")
Better performance than os.listdir
```
filter(lambda x: x.is_dir(), os.scandir())  # show all the directory entry
```

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

## File and Directory Acces

### [pathlib](./pathlib.md)
操作目录,路径的功能

