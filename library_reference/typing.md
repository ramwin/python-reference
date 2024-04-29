# typing

[官网](https://docs.python.org/3/library/typing.html)  

[测试](./typing_test.py)  

[tutorial](https://docs.python.org/3/tutorial/controlflow.html#function-annotations)  

注意这个annotation只是起到一个提示的作用，并不会对函数的执行，参数的校验起到真正的效果
```python
def f(ham: str, eggs: str='eggs') -> str:
```
## callable

[官网](https://docs.python.org/3/library/typing.html#annotating-callable-objects)

[测试代码](../test/test_typing_callable.py)

```python
from collections.abc import Callable

def call_int(x: str) -> str:
    return x + '1'

f: Callable[[float], float]

f = call_int
```

## Literal
```
Mode: TypeAlias = Literal['r', 'rb', 'w', 'wb']
def open(file: str, mode: Mode):
    pass
```

## 基础
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


## 返回List
```python
def add(number: int) -> int:
    return number + 1
## 数字构成的数组
list[int]  # python3 >= 3.10
from typing import List
List[int]  # python3 <= 3.8
```

## 多选

```python
from typing import Literal
GenderType = Literal["male", "female"]
```


## Union

```python
from typing import Union
Union[User, None]
```

## NetType

```python
VersionName = NewType("VersionName", str)
version: VersionName = VersionName("1.1.1")
```

* 区分两种int
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


## TypedDict

```python3
class Point2D(TypedDict):
    x: int
    y: int
    label: str
```

* [NotRequired](https://docs.python.org/3/library/typing.html#typing.NotRequired)
3.11新特性，可选字段


## overload
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

## [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar)
classvar可以防止覆盖类型和类型错误。但是无法防止不赋值

```python
class A:
    count: ClassVar[int]
```
