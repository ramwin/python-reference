# pathlib

[官网](https://docs.python.org/3/library/pathlib.html)

## 属性
* parents
返回所有的上级目录 `p.parents[0] == p.parent` `p.parents[-1] == p.root` 但是后面目前有bug
```
>>> p = PureWindowsPath('c:/foo/bar/setup.py')
>>> p.parents[0]
PureWindowsPath('c:/foo/bar')
>>> p.parents[1]
PureWindowsPath('c:/foo')
>>> p.parents[2]
PureWindowsPath('c:/')
```
* parent
* name: 返回文件名
* stem: 最后的目录(排除后缀)
```
>>> PurePosixPath('my/library.tar.gz').stem
'library.tar'
>>> PurePosixPath('my/library.tar').stem
'library'
>>> PurePosixPath('my/library').stem
'library'
```

## methods
* as_posix(): 返回绝对路径
* exists: 判断是否存在
* glob(pattern): 返回匹配的文件或者目录名
```
glob("*.pdf")
glob("**/*.pdf")
```
* `is_dir()`: `返回是否是目录`
* `is_file()`: `返回是否是文件`
* `is_symlink()`: `返回是否是链接`
* iterdir(): 返回一个包含子文件的generator
```
import re
def get_number(name):
    '785e321f-7855-42a8-8365-2cd82488d581-2.png'
    return int(re.match("\S+-(\d+).png", name).groups()[0])
sorted(
    path.iterdir(),
    key=lambda i: 
)
```
* joinpath(str|path|paths): 合并一个或者多个路径
注意，如果一个path开头是 `/`, 那么前面的路径就失效了，直接按照这个path开始计算  
```
dirpath = Path("缓存")
cache_path = dirpath.join("运行缓存", "tmp.json")
```

### [`mkdir(mode=511, parents=False, exist_ok=False)`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir)
创建目录, 具体的权限参考 [manpages](https://manpages.debian.org/bullseye/manpages-zh/open.2.zh_CN.html)
```
import stat
Path("new").mkdir(mode=stat.S_IREAD | stat.S_IWRITE | stat.S_IEXEC)
```

* resolve: 把相对路径转化成绝对路径. 并且会把软链接也解析
* rglob: 和glob一样，但是默认在前面添加`**/`
* rmdir: 删除空目录
* suffix: 返回最后一个后缀名
```
>>> Path("README.md").suffix
'.md'
```
* `relative_to`: `返回相对于某个路径的相对路径`
* suffixes: 返回后缀名列表
* stat()  
返回文件状态
```
p.stat().st_size  # 文件字节大小
p.stat().st_ctime st_mtime  # 创建，修改的时间戳
```
* `unlink(True)`: 删除文件或者链接, 参数`missing_ok`代表如果不存在是否报错
* `write_text`: 写入文字然后关闭
