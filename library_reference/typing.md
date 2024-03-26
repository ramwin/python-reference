### [Typing](https://docs.python.org/3/library/typing.html)

[测试](./typing_test.py)

[tutorial](https://docs.python.org/3/tutorial/controlflow.html#function-annotations)  
注意这个annotation只是起到一个提示的作用，并不会对函数的执行，参数的校验起到真正的效果
```python
def f(ham: str, eggs: str='eggs') -> str:
```

#### Literal
```
Mode: TypeAlias = Literal['r', 'rb', 'w', 'wb']
def open(file: str, mode: Mode):
    pass
```

#### 基础
可以直接用圆括号
```python
from typing import Tuple, List, Dict, Set
def get_tuple() -> Tuple[int, int]:
    pass
def get_list() -> List[int]:
    pass
def get_dict() -> Dict[int: int]:
    pass
def get_set() -> Set[int]:
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


#### TypedDict

```python3
class Point2D(TypedDict):
    x: int
    y: int
    label: str
```


#### overload
函数重载, [示例](../test_typing_overload.py)
```python3
from typing import overload
@overload
def process(response: None) -> None:
    ...
@overload
def process(response: int) -> tuple[int, str]:
    ...
@overload
def process(response: bytes) -> str:
    ...
def process(response):
    ...  # actual implementation goes here
```
