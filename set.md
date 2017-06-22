#### Xiang Wang @ 2017-04-28 10:38:49

# 基础
* [官网文档](https://docs.python.org/3/tutorial/datastructures.html#sets)
* 示例
```
    basket = {'apple', 'orange', 'apple'}  # {'apple', 'orange'}
    basket = set()  # 创建空的set需要使用方法，不能使用{}
    a = set('abracadabra')
    b = set('alacazam')
    a - b
    a | b
    a & b
    a ^ b
```
* 操作
    a = set()
    a.update([1,2,3])  # update把一个数组里面的元素都插入进去
