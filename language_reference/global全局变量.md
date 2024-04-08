# Global全局变量

```python
a = 0
def add():
    global a  # 如果没有这个， a就只能读，不能写
    a += 1
    print(a)
```
