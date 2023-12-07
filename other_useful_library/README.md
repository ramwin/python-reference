## bitstring
转化二进制数据
```
BitArray(HexBytes("0x7f")).int  // 127   01111111
BitArray(HexBytes("0x80")).int  // -128  10000000
```

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


## [filelock](https://github.com/benediktschmitt/py-filelock)


    from filelock import Timeout, FileLock
    lock = FileLock(path)
    try:
        lock.acquire(timeout=0)
    except Timeout:
        pass

## flockcontext
[github](https://github.com/AntoineCezar/flockcontext)
```
pip3 install flockcontext
from flockcontext import FlockOpen
with FlockOpen(Path, "w", timeout=3600) as lock:
    <do something>
    lock.fd.write("Locked\n")
```

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

## Humanfriendly
```
Humanfriendly.parse_size("10M")  // 10_000_000
Humanfriendly.parse_size("10M", binary=True)  // 1024 x 1024 x 10
```

## [hexbytes](https://hexbytes.readthedocs.io/en/stable/)
处理字符串和十六进制
```python
from hexbytes import HexBytes
HexBytes(b"123")  // HexBytes("0x313233")
HexBytes(b"123").hex()  // "0x0123"

HexBytes("123")  // HexBytes("0x0123")
HexBytes("123").hex()  // "0x313233"
```
* len  2个hex为1个长度
* slice `HexBytes("0xffff")[0:1] == HexBytes("0xff")`
* getitem `HexBytes("0xffff")[0] == 255`

## [imapclient](imapclient.md)
很好用的邮件客户端

* [ics](https://pypi.org/project/ics/) *日历，行程 calendar*
* [ipdb](./other_useful_library/ipdb.md) *断点来检测查看源码和运行状态*

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

## web3
* hexbytes.main.HexBytes
```
a == HexBytes(b"23")  b"2" == 50 == '0x32'
a = HexBytes("0x3233")
a.hex()  # "0x3233"
str(a)  # "b'23'"
```

* eth.subscribe
```
{
    'jsonrpc': '2.0',
    'method': 'eth_subscription',
    'params': {
        'subscription': '0x83d5de89ec40acb9929bbb809caa6f4c',
        'result': {
            'address': '0x6a091a3406e0073c3cd6340122143009adac0eda',  # pair address
            'topics': [
                '0xd78ad95fa46c994b6551d0da85fc275fe613ce37657fb8d5e3d130840159d822',  # topics, v2_swap
                '0x000000000000000000000000d9e1ce17f2641f24ae83637ab66a2cca9c378b9f',  # sender
                '0x0000000000000000000000002c678004af4c1e217d9ed8baabd4454406ceb63d',  # receiver
            ],
            'data': (
                '0x'
                '0000000000000000000000000000000000000000000000000000000000000000'  # amount0In
                '000000000000000000000000000000000000000000000000225ac0e25efff07a'  # amount1In
                '0000000000000000000000000000000000000000000000025f76668b7ad2b42f'  # amount0Out
                '0000000000000000000000000000000000000000000000000000000000000000'  # amount1Out
            ),
            'blockNumber': '0x11cca4f',
            'transactionHash': '0xe51d8ecfb4fffe4b26f87b4ff2894e8c4dcfed4dd2a42b8af93bc3f90e347d97',
            'transactionIndex': '0x72',
            'blockHash': '0x5a1f1a86651bc0fa04b8a219a6612e17ef6cc224bb7abe8f09c57324eddb1b5e',
            'logIndex': '0x108',
            'removed': False}
        },
    'time': 1701100620
}
```

* web3.eth.get_transaction
```
AttributeDict({
    'blockHash': HexBytes('0x7c15a5dc5ae...2ff3fc6'),
    'blockNumber': 18664014,
    'from': '0xDF9f0598E04DccdD941462De4fA6B915D5bb7784',
    'gas': 213168,
    'gasPrice': 43106689045,
    'maxFeePerGas': 74346949956,
    'maxPriorityFeePerGas': 5000000000,
    'hash': HexBytes('0xbff5390790e441959364cb8c7d1ac426de832d65a947f2aad069527a506c7318'),
    'input': HexBytes('0x8600c0fe...0000000000'),
    'nonce': 66,
    'to': '0x2C2C82e7CAf5F14e4995c366D9DB8CdFdf7677E3',
    'transactionIndex': 19,
    'value': 30000000000000000,
    'type': 2,
    'accessList': [],
    'chainId': 1,
    'v': 0,
    'r': HexBytes('0x7e561ae149d...c46ab87b61ec'),
    's': HexBytes('0x5a483194f03...710d52f97adf')}
```

### eth_typing
* eth_typing.evm.ChecksumAddress

