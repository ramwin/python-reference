**Xiang Wang @ 2017-04-28 11:19:42**

### collections
* [官网文档](https://docs.python.org/3/library/collections.html#module-collections)
* [OrderedDict](#OrderedDict)
* [defaultdict](#defaultdict)
* [deque](#deque)


#### OrderedDict
* [官网文档](https://docs.python.org/3/library/collections.html#ordereddict-objects)
    ```
    od = OrderedDict()  # 注意不能直接把一个dict传入进去, 因为这个dict是没有排序的
    od = OrderedDict([('key', 'value'), ('key2', 'value2')])
    od['1'] = 1
    a.keys()
    ```


#### defaultdict
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

#### deque
* [官方文档](https://docs.python.org/3/library/collections.html#collections.deque)
* pop和append左右的速度很快
    ```
    a = deque('ghi')
    a.append('j')
    a.appendleft('f')
    a.pop()
    a.popleft()
    ```


### collections.abc
这个是 Abstract Base Classes 可以用来确保这个Class无法被直接使用，而必须指定了特定的方法才能使用,利用的是`abc.abstractmethod`就能实现这样的效果

* #### Container

```
class A(Container):
    pass

class B(A):
    def __contains__(self, item):
        return True

b = B()  # OK
a = A()  # TypeError:  Can't instantiate abstract class A with abstract methods __contains__
```
* #### Hashable
* #### Iterable
