**Xiang Wang @ 2017-06-01 11:14:56**

[官网](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

#### 基础
* append(x) 添加元素,等价于a[len(a):] = [x]
* extend(iterable) 延长, 等价语a[len(a):] = iterable
* insert(i, x)
* remove(x) 删除x, 如果x不存在, 就会报错, 注意这个x是==来判断的, 只要二者相等就能remove
* pop([i]) pop掉第i个元素, 或者pop掉最后一个元素, 如果list为空,或者i太多 raise IndexError


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
