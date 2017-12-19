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
