### [tempfile](https://docs.python.org/3/library/tempfile.html#examples)
临时文件功能

```python
import tempfile
fp = tempfile.TemporaryFile(mode='w+b', encoding=None)
fp.write(b'Hello world!')
```

#### NamedTemporaryFile
带名字的tempfile, 所以可以提供给其他程序使用
```python
with tempfile.NamedTemporaryFile() as f:
    subprocess.run(cmds, stdout=f)
```

#### SpooledTemporaryFile
因为linux系统的文件io自带page cache. 所以这个class没用

#### tempfile.TemporaryDirectory -> str
可以把文件夹自动清除
```python
with temfile.TemporaryDirectory() as d:
    tmp_csv = Path(d.name).joinpath("tmp.csv")
```

#### mkdtemp(dir=None)
创建一个临时目录. 和TemporaryDirectory比，不会自动清除。需要手动清理
