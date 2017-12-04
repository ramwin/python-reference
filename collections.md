#### Xiang Wang @ 2017-04-28 11:19:42

# 基础
* [官网文档](https://docs.python.org/3/library/collections.html#module-collections)
* [OrderedDict](#OrderedDict)
* [defaultdict](#defaultdict)
* [deque](#deque)


<span id="OrderedDict"></span>
## OrderedDict
* [官网文档](https://docs.python.org/3/library/collections.html#ordereddict-objects)
    ```
    od = OrderedDict()  # 注意不能直接把一个dict传入进去, 因为这个dict是没有排序的
    od = OrderedDict([('key', 'value'), ('key2', 'value2')])
    od['1'] = 1
    a.keys()
    ```


<span id="defaultdict"></span>
## defaultdict
* [官方文档](https://docs.python.org/3/library/collections.html#collections.defaultdict)
* [参考代码]
    ```
    dd = defaultdict(int)
    dd['w']
    >>> 0
    dd['w'] = 1
    dd['w']
    >>> 1
    ```
* [方法]
    * setdefault
        ```
        dd = defaultdict(int)
        dd.setdefault('w', 2)  # dd['w'] = 2 if 'w' not in dd
        dd['w']
        >>> 2
        dd.setdefault('w', 4)
        >>> 2
        ```

<span id="deque"></span>
## deque
* [官方文档](https://docs.python.org/3/library/collections.html#collections.deque)
* pop和append左右的速度很快
    ```
    a = deque('ghi')
    a.append('j')
    a.appendleft('f')
    a.pop()
    a.popleft()
    ```
