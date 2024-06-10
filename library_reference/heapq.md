# [heapq](https://docs.python.org/3/library/heapq.html)
*heap queque algorithm*
对于任意一个列表, `a[k] <= a[2*k + 1] and a[k] <= a[2*k + 2]`  
所以插入元素耗时 `log(n)`  

* heapify
* `merge(*iterables, key=None, reverse=False)`
把多个列表按序输出， 注意每个列表必须是排序好了的

* heappush
把元素推入列表
```
heapq.heappush(result, i)
```

* heappushpop(heap, item)
把元素item添加到heap, 然后pop出最小的

* heapreplace(heap, item)
先从heap里面拿出最小的，然后push进去item. *和heappushpop的操作顺序相反哦*
