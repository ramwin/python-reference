#### Xiang Wang @ 2017-06-01 11:14:56

### 基础
```
    a = ['a', 'b', 'c']
    a.pop(0)=='a' # ['b', 'c']  如果index太大，会报错
    a.remove('b')==None  # ['c'], 如果不存在，会报错。既然你都知道remove什么了，就不返回给你remove了什么了
    
```


### 操作
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

### 进阶
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
