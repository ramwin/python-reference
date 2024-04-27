# OS
[https://docs.python.org/3/library/os.html](https://docs.python.org/3/library/os.html)

* [walk](https://docs.python.org/3/library/os.html#os.walk)
第一个参数是目录， 后面是目录下的目录名和文件名
```
~/g/python-reference/test/组目录 $ tree
.
└── 父目录
    ├── 父文件1
    └── 目录
        ├── 叶子文件1
        └── 叶子文件2

('.', ['父目录'], [])
('./父目录', ['目录'], ['父文件1'])
('./父目录/目录', [], ['叶子文件2', '叶子文件1'])
```

## 基础
```python
os.getcwd() # 获取当前目录  
os.path.abspath('.')

os.path.isdir("<path>") # 是否是目录

os.chdir('Pictures') # 切换目录

os.listdir() # 遍历文件

import shutil
shutil.rmtree('<directory>') # 删除目录
```

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

## os.path
[官网](https://docs.python.org/3/library/os.path.html)
* os.path.abspath
* [ ] `os.path.dirname`
* `os.path.exists`
返回是否存在这个文件或者目录 
* [ ] `os.path.lexists`
* `os.path.isfile`:  
Return True if path is an existing regular file. This follows symbolic links, so both islink() and isfile() can be true for the same path.
