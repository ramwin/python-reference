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
