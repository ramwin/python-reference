*Xiang Wang @ 2016-09-29 18:18:47*

# for 语句用法

## 基础
    for i in range(10):
        continue  # 继续执行
        break  # 终端所有的 for, (else也不执行)
        print(i)
    else:  # else可以不需要
        print("输出了前10个自然数")


## 自定义能循环的结构
    class myrange(object):
        """ 做一个从1开始计数的range """

        def __init__(self, n):
            self.max = n
            self.i = 0

        def __iter__(self):
            """ 这个函数只会初始化一遍 """

            while self.i < self.max:  # 一直输出知道输出为None
                self.i += 1
                yield self.i

            while True:  # 一直输出，除非遇到了特殊情况
                self.i += 1
                if self.i > self.max:
                    raise StopIteration
                else:
                    yield self.i

    class A(object):

        def f(self, x):
            for i in range(x):
                yield i
            raise StopIteration

        def __iter__(self):
            return self.f(10)
    b = A()
    for i in b.f(5):
        print(i)
    print(list(b.f(6)))
