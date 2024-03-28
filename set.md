# 基础
* [官网文档](https://docs.python.org/3/tutorial/datastructures.html#sets)
* [官方api](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)
* 基础操作
```
basket = {'apple', 'orange', 'apple'}  # {'apple', 'orange'}
basket = set()  # 创建空的set需要使用方法，不能使用{}
a = set('abracadabra')
b = set('alacazam')
a - b
a | b  # ab并集
a & b  # ab交集
a ^ b  # 只存在于a或者b的
```

* 操作
    ```
    a = set()
    a.update([1,2,3])  # update把一个数组里面的元素都插入进去
    a.add('123')
    a.remove('123')
    b = {2}
    b.issubset(a)
    ```

* pop
返回任意一个元素，如果为空会raise KeyError

# 自定义类的set
[示例](./test/test_set.py)
* 需要设置`__hash__`来用来查找定位
* 需要设置`__eq__`来用来对hash一致的元素去重
