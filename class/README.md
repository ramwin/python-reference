**Author**: *Xiang Wang* @   2016-06-02 10:08:41  
**e-mail**: [*ramwin@qq.com*](mailto:ramwin@qq.com)  

### 调用函数内部的方法

    class A(object):
        def __init__(self, i):
            self.i = i
            self._bar = 23  # 一个下划线，代表提示用户不要用这个内部的变量，但是实际上是可以用的。 如果的模块中有 _的函数，代表不被import *时import
            self.i_ = 34  # 变量名称已经被关键词占用，所以加一个_
            self.__bar = 23  # dir(a)的时候，是没有 __bar的，也无法调用了，只有内部才能使用。（其实python会把 __bar 变成其他名字 __Test__bar这种
            self.__as__ = 1 # 对于前面后面都有两个_的，这个就不再禁用了，但是很多内置函数会调用
            _ = 'tmp'  # _ 单独的_代表我对这个数据不关心

        def __eat(self):  # 如果是两个下划线，就是不能被使用的
            print("It is eating")

        @staticmethod   # 这个必须有
        def judge(i):
            return isinstance(i, int)

        def out(self):
            return self.judge(self.i)   # self可以换成 A

    a = A(3)
    a.judge()
    A.judge(a.i)    # 这样也可以，但是觉得违背了class封装的思想

### 继承
    class B(A):
        def __init__(self, i):
            super(B, self).__init__(i)  # 调用父类的方法
