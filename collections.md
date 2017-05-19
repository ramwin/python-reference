#### Xiang Wang @ 2017-04-28 11:19:42

# 基础
* [官网文档](https://docs.python.org/3/library/collections.html#module-collections)
* [OrderedDict](#OrderedDict)
* [defaultdict](#defaultdict)


## <span id="OrderedDict">OrderedDict</span>
* [官网文档](https://docs.python.org/3/library/collections.html#ordereddict-objects)
```
    od = OrderedDict()  # 注意不能直接把一个dict传入进去, 因为这个dict是没有排序的
    od = OrderedDict([('key', 'value'), ('key2', 'value2')])
    od['1'] = 1
    a.keys()
```


## <span id="defaultdict">defaultdict</span>
* [官方文档](https://docs.python.org/3/library/collections.html#collections.defaultdict)
```
    dd = defaultdict(int)
    dd['w']
    >>> 0
    dd['w'] = 1
    dd['w']
    >>> 1
```
