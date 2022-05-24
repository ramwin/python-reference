[官方教程](https://docs.python.org/3/library/zipfile.html)


## 基础用法
```
from zipfile import ZipFile

# 把文件压缩到指定文件
with ZipFile(<filename.zip>, 'w') as myzip:
    myzip.write('filename', arcname='new_filename')  # 如果没有arcname，就会用filename来保存
    如果filename是绝对路径，会去掉最前面的/
```

## ZipFile
* `write(filename, arcname=None, compress_type=None, compresslevel=None)`
arcname默认是filename, 但是去掉了盘符和根`/`


## 压缩一个文件夹
```
root = Path('')
with ZipFile(filename, 'w') as myzip:
    for f in root.rglob("*"):
        myzip.write(f, f.relative_to(root))
```

## 处理zip网络文件
```
import tempfile
import zipfile
import pathlib
res = requests.get(url)
temp_file = tempfile.TemporaryFile()
temp_dir = tempfile.TemporaryDirectory()
for content in res.iter_content(4096):
    temp_file.write(content)
temp_file.seek(0)
zipfile.ZipFile(temp_file).extractall(temp_dir)
print(list(pathlib.Path(temp_dir.name).iterdir()))
```
