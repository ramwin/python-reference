### [tempfile](https://docs.python.org/3/library/tempfile.html#examples)
临时文件功能

```
import tempfile
fp = tempfile.TemporaryFile(mode='w+b', encoding=None)
fp.write(b'Hello world!')
```

#### NamedTemporaryFile
带名字的tempfile, 所以可以提供给其他程序使用
```
with tempfile.NamedTemporaryFile() as f:
    subprocess.run(cmds, stdout=f)
```

#### SpooledTemporaryFile
因为linux系统的文件io自带page cache. 所以这个class没用

#### tempfile.TemporaryDirectory
可以把文件夹自动清除
```
with temfile.TemporaryDirectory() as d:
    tmp_csv = Path(d.name).joinpath("tmp.csv")
```
