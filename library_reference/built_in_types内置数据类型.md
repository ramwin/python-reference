**Xiang Wang @ 2018-11-21 19:43:00**

**内置数据类型**
[官网](https://docs.python.org/3/library/stdtypes.html#)

* [ ] and, or, not; int, float, complet; list, tuple, range ...

### Truth Value Testing

### Boolean Operations - and, or, not
x or y: 如果x为True, 就不再计算y  
x and y: 如果x为False, 就不再计算y

### Mapping Types -- dict
* 原理
[stackoverflow questions: how-does-python-implement-dictionaries](https://stackoverflow.com/questions/56097997/how-does-python-implement-dictionaries)
[参考资料](https://www.freecodecamp.org/news/exploring-python-internals-the-dictionary-a32c14e73efa/)
一开始定义一个array(默认长度为8), 通过key的hash，存入对应的array。如果遇到碰撞了，就采用第二次hash`(i = i * 5 +1，或者 i = another_hash(i))`来保存输入。大约达到70%左右时，就考虑扩展这个arry的长度，重新放入值


这是唯一的一种mapping object  
hashable的数据, 就可以当作key. 因为数字遵循了一样的计算规则, 所以如果两个数字值一样, 那么他们得到的索引结果就一样. `a[1]`和`a[1.0]` 完全同步. 但是因为python保存浮点数是近似值, 所以用浮点数当作key很不明智
```
>>> a = dict(one=1, two=2, three=3)  # 使用keyword arguments
>>> b = {'one': 1, 'two': 2, 'three': 3}  # 使用逗号分割
>>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))  # 输入一个map
>>> d = dict([('two', 2), ('one', 1), ('three', 3)])  # 输入一个list
>>> e = dict({'three': 3, 'one': 1, 'two': 2})  # 输入一个dict
>>> a == b == c == d == e
True
```
* 方法
    * len: *返回items的数量*
    * `d[key]`: 返回某个item, 如果不存在会报错 `KeyError`  
    如果一个dict的子类定义了`__missing__()`函数, 则当key不存在时, 会调用那个函数, 这个比defaultdict好用, 因为可以根据key生成不同的数据
    * `del d[key]`: 删除某个key
    * `key in d`: 判断是否包含一个key
    * `key not in d`
    * `iter(d)`: 循环dict的key, 等价于 `iter(d.keys())`
    * clear: 删除所有item
    * copy: 返回shadowcopy
    * classmethod fromkeys(seq[, value]): `返回keys为seq, 默认值为value或者None的dict`
    * get(key[, default]) *如果有key就返回他的value, 否则返回default, default默认是None, 所以这个永远不会raise KeyError*
    * pop(key[, default]) *同get, 只是最后还要删除key 如果没有这个key会raise KeyError*
    * popitem() *返回(key, value)或者报KeyError, 注意是LIFO,后进先出的规则*
    * setdefault(key[, default]) *如果key不存在就设置默认值default或者None*
    * update *更新dictionary的值, 覆盖已经存在的key*
    * values *返回dictionary的值*
* Dictionary view objects  
dict.keys(), dict.values(), dict.items() 返回的对象. 当dict变化时, 这些也会变化. 棒.
    * len 返回长度
    * iter  
    因为都是保证顺序了, 所以可以用`pairs = zip(d.values(), d.keys())`. 或者 `pairs = [(v, k) for (k, v) in d.items()]`  *第一个只能python3.7保证*  
    在迭代的时候, 如果更新了会触发RuntimeError
    * x in dictview
    返回True 如果x在里面. 当dictview是dict_items的时候, x要是(key, value)的tuple, 不可以是list
* 循环插入深层的value  
在dict的key1下的key2下的key3设置为ivalue  
```
dic = {'a':'b'}
def insertdata(dic, keys, value):
    if len(keys) == 1:
        dic[keys[0]] = value
        return 0
    if not keys[0] in dic:
        dic[keys[0]] = {}
    insertdata(dic[keys[0]], keys[1:], value)
insertdata(dic, ['key1','key2','key3'], 'ivalue')
```
* [ ] Context Manager Types; Other; Special Attributes
