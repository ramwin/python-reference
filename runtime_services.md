## [Python Runtime Services 和编译器,环境有关的服务](https://docs.python.org/3/library/python.html)

### [Sys](https://docs.python.org/3/library/sys.html)

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

### traceback -- Print or retrieve a stack traceback
[官网](https://docs.python.org/3/library/traceback.html)
```
traceback.print_stack()  # 直接print出stack
log = traceback.format_exc()  # 记录报错的stack
stack = traceback.format_stack()  # 记录当前的stack
```

### [dataclass](https://docs.python.org/3/library/dataclasses.html)
[参考](https://zhuanlan.zhihu.com/p/59657729)  
查看[typing](./library_reference/typing.md)可以了解更多方法
自动帮你实现 `__eq__`, `__repr__`, `__init__`

```
from dataclasses import dataclass

@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
```

###  contextlib
* suppress
忽略某些报错
```
with contextlib.suppress(models.Model.DoesNotExist):
    item = models.Model.objects.get(id=id)
    item.children.clear()
```

### 待更新
* [ ] warnings