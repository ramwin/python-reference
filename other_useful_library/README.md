## [diff-match-patch](https://github.com/google/diff-match-patch)
用来比较文字的不同
* 用法
    ```
    >>> from diff_match_patch import diff_match_patch
    >>> dmp = diff_match_patch()
    >>> dmp.diff_main('123', '22')
    [(-1, '1'), (1, '2'), (0, '2'), (-1, '3')]
    >>> dmp.diff_prettyHtml(dmp.diff_main('123', '223'))
    '<del style="background:#ffe6e6;">1</del><ins style="background:#e6ffe6;">2</ins><span>23</span>'
    ```
* 效果  
<del style="background:#ffe6e6;">1</del><ins style="background:#e6ffe6;">2</ins><span>23</span>

## eth_typing
* eth_typing.evm.ChecksumAddress

## [git](https://gitpython.readthedocs.io/en/stable/tutorial.html)
处理git用
* 克隆代码

```python
from git import Repo
from pathlib import Path
Repo.clone_from(url, to_path)
git.Repo.clone_from(url, to_path, recurse_submodule=True)

# 指定密钥来克隆
repo = git.Repo.init(Path("target"))
with repo.config_writer() as writer:
    writer.set("core", "sshCommand", "ssh -i <自定义密钥>")
```

* 基础代码

```python
sudo pip3 install gitpython
from git import Repo
repo = Repo()
for tag in repo.tags:
    print(tag.name, tag.commit)

for commit in repo.iter_commits(max_count=10):
    print(commit.hexsha, commit.message, commit.author.name, )
```

* 运行git命令

```python
import git
repo.git.rebase
cmd = git.cmd.Git()
cmd.execute('git lfs ls-files -l')
try:
    repo.git.merge(<ref>)  # 合并分支
except git.GitCommandError:
    raise
```

### 执行命令
* show
查看某个文件的内容
```
repo.git.show(f"{commit}:README.md") => str
```

### commit
```
commit = next(repo.iter_commits("master", before=datetime.date(2022, 1, 1)))  # 获取元旦最后一个提交
commit.commitded_date
datetime.datetime(2020, 6, 19, 9, 46, 9, tzinfo=<git.objects.util.tzoffset object at 0x7f0ac0736320>)
commit.hexsha
```

### remote
```
origin = repo.create_remote("origin", "git@github.com:ramwin/python-reference.git")
origin.pull()
```

## flockcontext
[github](https://github.com/AntoineCezar/flockcontext)
```
pip3 install flockcontext
from flockcontext import FlockOpen
with FlockOpen(Path, "w", timeout=3600) as lock:
    <do something>
    lock.fd.write("Locked\n")
```

## PID
流程控制算法
```python
from simple_pid import PID
from exponential_counter import LinearCounter

def test_time2():
    print("我们提供一个自己的时间函数，每次加1")
    pid = PID(1, 0.1, 0.05, time_fn=LinearCounter())
    value = -200
    for _ in range(3):
        delta = pid(value)
        value = value + delta
        print("增加%f 变成 => %f", delta, value)

# 我们提供一个自己的时间函数，每次加1
# 增加%f 变成 => %f 220.0 20.0
# 增加%f 变成 => %f -13.0 7.0
# 增加%f 变成 => %f 10.950000000000001 17.950000000000003

```

## psutil
[获取系统信息](https://psutil.readthedocs.io/en/latest/)
```python
import psutil
psutil.net_if_addrs()
all_ips = [
    i.address
    for i in itertools.chain(*psutil.net_if_addrs().values())
]
['169.254.139.78', '4c:cc:6a:47:6a:6f', '169.254.51.28',
 '90:61:ae:bb:31:8f', '127.0.0.1', '::1',
 '00:00:00:00:00:00', '169.254.162.106', '00:ff:cc:e9:90:30',
 '192.168.0.102', '90:61:ae:bb:31:8b', '169.254.220.176',
 '90:61:ae:bb:31:8c', '169.254.22.106', '92:61:ae:bb:31:8b']

```

* 获取CPU信息
```python3
psutil.cpu_percent() => 3.5  # 所有cpu平均3.5%
```

* [获取内存信息](https://stackoverflow.com/questions/938733/total-memory-used-by-python-process)
```python3
import os, psutil
process = psutil.Process()
print(process.memory_info().rss)  # in bytes
```


## pysrt
[官网](https://github.com/byroot/pysrt)
* 基础
```
import pysrt
subs = pysrt.open('srt.srt', encoding='utf8')
first_sub = subs[0]
first_sub.text = "hello world"
first_sub.start.seconds = 20
first_sub.shift(seconds=2)
first_sub.start += {'seconds': -1}
subs.shift(minutes=1)
subs.shift(ratio=25/23.9)  # convert a 23.9 fps subtitle in 25fps
del subs[12]
part = subs.slice(starts_after={'minutes': 2, 'seconds': 30}, ends_before={'minutes': 3, 'seconds': 40})
part.shift(seconds=-2)
subs.save('other/path.srt', encoding='utf8')
```
