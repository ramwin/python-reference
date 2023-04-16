## [git](https://gitpython.readthedocs.io/en/stable/tutorial.html)
处理git用
* 克隆代码

```python
from git import Repo
Repo.clone_from(url, to_path)
git.Repo.clone_from(url, to_path, recurse_submodule=True)
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
