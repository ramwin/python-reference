# Python Runtime Services 和编译器,环境有关的服务
[官网](https://docs.python.org/3/library/python.html)

## [Sys](https://docs.python.org/3/library/sys.html)

* [argv](https://docs.python.org/3/library/sys.html#sys.argv)
获取脚本的参数
```
print(ssy.argv)
["test.py", "12", "324"]
```


* stdin
```
print(sys.stdin)  # 用于python处理pipe数据
```

## traceback -- Print or retrieve a stack traceback
[官网](https://docs.python.org/3/library/traceback.html)
```
traceback.print_stack()  # 直接print出stack
log = traceback.format_exc()  # 记录报错的stack
stack = traceback.format_stack()  # 记录当前的stack
```

## dataclass
[官网](https://docs.python.org/3/library/dataclasses.html)
[参考](https://zhuanlan.zhihu.com/p/59657729)  
查看[typing](./library_reference/typing.md)可以了解更多方法
自动帮你实现 `__eq__`, `__repr__`, `__init__`

```
from dataclasses import dataclass, field

@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0
    mylist: list[int] = field(default_factory=list)

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
```

### `post_init`后处理
[官网](https://docs.python.org/3/library/dataclasses.html#post-init-processing)  
用来在初始化实例后, 根据实例的属性, 自动生成其他属性  
```python
@dataclass
class Student:
    first_name: str
    last_name: str
    display_name: str = None

    def __post_init__(self):
        if self.display_name is None:
            self.display_name = self.first_name + " " + self.last_name
```

### asdict/astuple
[官网](https://docs.python.org/3/library/dataclasses.html#dataclasses.asdict)  
把dataclass对象转化成dict. 注意, 如果是List[Obj], asdict后可以正常变成list. 但是再通过
Obj(**data)后, 会导致原来的List[Obj]会变成List[dict]
```
@dataclass
class Point:
     x: int
     y: int

@dataclass
class C:
     mylist: list[Point]

p = Point(10, 20)
assert asdict(p) == {'x': 10, 'y': 20}

c = C([Point(0, 0), Point(10, 4)])
assert asdict(c) == {'mylist': [{'x': 0, 'y': 0}, {'x': 10, 'y': 4}]}
```

##  contextlib
* suppress
忽略某些报错
```
with contextlib.suppress(models.Model.DoesNotExist):
    item = models.Model.objects.get(id=id)
    item.children.clear()
```

## 待更新
* [ ] warnings
