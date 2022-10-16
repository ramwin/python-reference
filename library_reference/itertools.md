### [itertools](https://docs.python.org/3/library/itertools.html)

#### chain

```python
chain('ABC', 'DEF') --> A B C D E F
chain(range(1, 6), range(4, 0, -1)) --> 1 2 3 4 5 4 3 2 1
```

#### [chain.from_iterable](https://docs.python.org/3/library/itertools.html#itertools.chain.from_iterable)

```python
# 和chain差不多， 但是只支持一个参数， 会对此展开后再用chain
def from_iterable(iterables):
    for it in iterables:
        for element in it:
            yield it
```

#### count(start, [step])  
从某个数字开始一直循环


```python
from itertools import count
loop = count(10)
next(loop) // 10
next(loop) // 11
next(loop) // 12
...
```

#### tee(iterable, n=2)
把一个迭代器变成多个独立的

#### `zip_longest
* zip
虽然zip是python的内置函数, 但是估计会经常在这里查看
```
for a, b in zip(iter1, iter2):  # 按照最短的来
    pass
```
* `zip_longest(*iterables, fillvalue=None)
按照最长的来. 其他的会填充fillvalue
