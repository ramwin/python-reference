### [Typing](https://docs.python.org/3/library/typing.html)

[测试](./typing_test.py)

[tutorial](https://docs.python.org/3/tutorial/controlflow.html#function-annotations)  
注意这个annotation只是起到一个提示的作用，并不会对函数的执行，参数的校验起到真正的效果
```python
def f(ham: str, eggs: str='eggs') -> str:
```

#### 基础
可以直接用圆括号
```python
def get_tuple() -> (int, int):
    pass
def get_list() -> [int]:
    pass
def get_dict() -> {int: int}:
    pass
def get_set() -> {int}:
    pass
```


#### 返回List
```python
def add(number: int) -> int:
    return number + 1
# 数字构成的数组
list[int]  # python3 >= 3.10
from typing import List
List[int]  # python3 <= 3.8
```

#### 多选

```python
from typing import Literal
GenderType = Literal["male", "female"]
```


#### Union

```python
from typing import Union
Union[User, None]
```

#### 区分两个int

```python
from typing import NewType
UserId = NewType("UserId", int)
AttackPoint = NewType("AttackPoint", int)

def attack(target: UserId, atk: AttackPoint):
    if not atk:
        atk = AttackPoint(1)
    user = User.objects.get(id=UserId)
    user.healph -= atk
    user.save()

```
