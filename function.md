#### Xiang Wang @ 2017-12-14 17:07:36


# 基础
* [参数的传递](#参数的传递)
```python
def main(name, age, height=2.2, *args, **kwargs):
    print("name: {}".format(name))
    print("age: {}".format(age))
```

# 参数的传递
* 调用的时候， 必须先传递位置变量，后传递名称变量。
    `main('name', key='value', 'age')  # 错`
* 如果位置变量已经有了值，后面肯定不能再加同名称变量了

# Annotation
[tutorial](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
注意这个annotation只是起到一个提示的作用，并不会对函数的执行，参数的校验起到真正的效果
```
def f(ham: str, eggs: str='eggs') -> str:
```
