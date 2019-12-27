**Xiang Wang @ 2017-06-01 11:14:56**

[官网](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

#### 基础
* append(x) 添加元素,等价于a[len(a):] = [x]
* extend(iterable) 延长, 等价语a[len(a):] = iterable
* insert(i, x)
* remove(x) 删除x, 如果x不存在, 就会报错, 注意这个x是==来判断的, 只要二者相等就能remove
* pop([i]) pop掉第i个元素, 或者pop掉最后一个元素, 如果list为空,或者i太多 raise IndexError
* sort  
把list排序
```
list.sort(key=None, reverse=False)
```
* sorted  
生成一个新的排序好的list
```
new_list = sorted(l, key=lambda x: x['value'])  # 根据value进行排序
```


#### 操作
* 切片
    ```
    a = [1,2,3]
    a[start:end]
    ```
    * 如果 `start >= len(a)`, 返回空列表

* zip合并
    ```
    zip([1, 2, 3], ['a', 'b', 'c'])
    (
        (1, 'a'),
        (2, 'b'),
        (3, 'c')
    )
    ```

#### 进阶
* 自定义迭代器
    ```
    class A(object):
        def __init__(self, i):
            self.i = 1
            self.start = 0
        def __iter__(self):
            return self
        def __next__(self):
            if self.start < self.i:
                self.start += 1
                time.sleep(self.start)
                return self.start
            else:
                raise StopIteration()
    ```


#### 其他
* [for else](http://book.pythontips.com/en/latest/for_-_else.html)
```
for item in container:
    if search_something(item):
        process(item)
        break
else:
    not_found_in_container()
```
