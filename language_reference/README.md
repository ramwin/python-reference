# Language Reference
## 未分类
```{toctree}
../set.md
../polymorphism_多态.md
../qiniu.md
../class/README.md
../multi/README.md
../magic_methods/README.md
../language_reference/function.md
../script/把图片变成HTML/text.md
```

## Data Types
[官网](https://docs.python.org/3/library/datatypes.html)

```{toctree}
./exception.md
```

### [list](./list.md)
```{toctree}
./list.md
```

### [datetime](./library_reference/datetime时间.md)
### [ ] [calendar](https://docs.python.org/3/library/calendar.html)

### [heapq](./library_reference/heapq.md)

### [bisect](https://docs.python.org/3/library/bisect.html)
通过二分法来查找list或者插入数据
```
bisect.insort(list, item)  # 把x插入list并保持顺序
bisect.bisect(list, item)  # 找到可以插入item的位置(最右侧)
# 查看是否存在
def index(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError
```

### copy  

* copy.copy(x): return a shallow copy of x
* copy.deepcopy(x): return a deepcopy
copy.copy只会copy一层, 里面的可变对象不会copy  
copy.deepcopy会copy recursively  
在shallow copy里, 对于dict, 使用的是 dict.copy(), 对于list使用的是copied_list = original_list[:]  
如果要实现自己的copye, 可以重写 `__copy__()` 和 `__deepcopy__()`  

* [ ] pprint

### [enum](./library_reference/README.md#enum)

[官网](https://docs.python.org/3/reference/index.html)

## 6. Expressions
### [magic method魔法方法](./magic_methods/README.md)
* [slice](https://docs.python.org/3/reference/expressions.html#expression-lists)


    class A:

        def __getitem__(self, sli):
            sli.start, sli.stop, sli.step  # A()[start:stop:step]


### Evaluation order 执行顺序
[官网](https://docs.python.org/3/reference/expressions.html#evaluation-order)

    ()  # 括号内
    **  # 指数
    +x, -x  # 负数
    in, not in, is, is not, <, <=, >, >=, !=  # 比较
    not x  #
    and  #
    or  # and 和 or不是同样的哦。

## Simple statements 简单语句
11. [import机制](http://www.jianshu.com/p/b963782f59e9)
[import文档](https://docs.python.org/3/reference/simple_stmts.html#the-import-statement)  
如果使用了相对引用, 必须保证最外层不能抵达当前目录

12. [global](language_reference/global_test.py)
```{toctree}
./global全局变量.md
```

## Compound statements 复合语句
```{toctree}
./function.md
```

### [with语句 the with statement](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement)
[测试](./test/test_with.py)
成功执行时, exit的三个参数都为None, 否则为对应数据
```
class A():
    def __enter__(self):
        print('enter')
    def __exit__(self, exc_type, exc_value, traceback):
        print(f'exc_type: {exc_type}')
        print(f'exc_value: {exc_value}')
        print(f'traceback: {traceback}')
        print('exist')
with A():
    print('start')
    raise Exception('value')
```

### [for 语句](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement)
* 通过内置变量counter来记录执行的位置，所以remove会导致少执行，insert会导致重复执行

    ```
    for i in a:
        if i == 3: a.remove(i)  # 少执行
        if i == 3: a.insert(0, 3)  # 多执行
    ```



### [class](./class/README.md)
[官网文档 TODO](http://ramwin.com:8000/tutorial/classes.html)
* 属性
    * `__new__`: 创建class类的时候调用  

[示例](./class/class_new.py). 通过`__new__`的时候`，返回不同的class  

    ```python
    class GuessAnimal(object):
        def __name__(self, type, *args, **kwargs):
            if type == 'dog':
                return Dog(*args, **kwargs)
            return Cat(*args, **kwargs)
    d = Some("dog")
    d.say()
    c = Some("cat")
    ```

    * `__module__` : class的模块
    * `__name__` : class的name

* [property](./library_reference/built_in_functions内置函数.md#property)
