**Xiang Wang @ 2021-01-06 10:07:52**


### [pathlib](https://docs.python.org/3/library/pathlib.html)
```
from pathlib import Path
p = Path('.')
```

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
* glob(pattern): 返回匹配的文件或者目录名
```
glob("*.pdf")
glob("**/*.pdf")
```
* mkdir(exist_ok=False): 创建目录
* stem: 最后的目录(排除后缀)
```
>>> PurePosixPath('my/library.tar.gz').stem
'library.tar'
>>> PurePosixPath('my/library.tar').stem
'library'
>>> PurePosixPath('my/library').stem
'library'
```
* as_posix(): 返回绝对路径
* joinpath(str|path|paths): 合并一个或者多个路径
注意，如果一个path开头是 `/`, 那么前面的路径就失效了，直接按照这个path开始计算  


    dirpath = Path("缓存")
    cache_path = dirpath.join("运行缓存", "tmp.json")

* name: 返回文件名
* suffix: 返回最后一个后缀名
```
>>> Path("README.md").suffix
'.md'
```
* suffixes: 返回后缀名列表
* unlink: 删除文件或者链接
* write_text: 写入文字然后关闭

#### methods
* `is_dir()`: `返回是否是文件`
* `is_symlink()`: `返回是否是链接`
* stat()  
返回文件状态


    p.stat().st_size  # 文件字节大小
    p.stat().st_ctime st_mtime  # 创建，修改的时间戳
