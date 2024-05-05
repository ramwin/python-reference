# Function
[官网](https://docs.python.org/3/reference/compound_stmts.html#function-definitions)

## docstring

```
def function(a: int, b: str, c = True) -> bool:
    """_summary_ 这里的格式支持restructed text

    Args:
        a (int): _description_
        b (str): _description_
        c (bool, optional): _description_. Defaults to True.

    Returns:
        bool: _description_
    """
```

## 基础
* [参数的定义](https://docs.python.org/3/tutorial/controlflow.html#special-parameters)
```python
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
```
* [参数的传递](#参数的传递)
```python
def main(name, age, height=2.2, *args, **kwargs):
    print("name: {}".format(name))
    print("age: {}".format(age))
```

## 参数的传递
* 调用的时候， 必须先传递位置变量，后传递名称变量。
    `main('name', key='value', 'age')  # 错`
* 如果位置变量已经有了值，后面肯定不能再加同名称变量了

## Annotation
详情见[typing](./library_reference/typing.md)模块  

## decorator 装饰器

[官网](http://www.cnblogs.com/huxi/archive/2011/03/01/1967600.html)

### 基础用法
```
# 基础用法
from functools import update_wrapper
def log(f):
    print('log')
    print(f.__name__)
    def fin(*args, **kwargs):
        return f(*args, **kwargs)
    return update_wrapper(fin, f)
    return fin

@log
def main():
    ''' main __docstring__ '''
    print(1)
```

### 让装饰器带参数
```
def deco(text):
    def _deco(func):
        def __deco(*args, **kwargs):
            print('before myfunc() called.')
            print(text)
            func(*args, **kwargs)
            print('after myfunc() called.')
        return update_wrapper(__deco, func)
    return update_wrapper(_deco, func)

@deco('text')
def myfunc(text= 'no text' ):
    print("myfunc() called")
    print(text)
```
