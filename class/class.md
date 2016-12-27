**Author**: *Xiang Wang* @   2016-06-02 10:08:41  
**e-mail**: [*ramwin@qq.com*](mailto:ramwin@qq.com)  

# 调用函数内部的方法

    class A(object):
        def __init__(self, i):
            self.i = i

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

# 继承
    class B(A):
        def __init__(self, i):
            super(B, self).__init__(i)  # 调用父类的方法
