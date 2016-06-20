**Author**: *Xiang Wang* @   2016-06-02 10:08:41  
**e-mail**: [*ramwin@qq.com*](mailto:ramwin@qq.com)  

# 调用函数内部的方法

    class A(object):
        def __init__(self, i):
            self.i = i

        @staticmethod   # 这个必须有
        def judge(i):
            return isinstance(i, int)

        def out(self):
            return self.judge(self.i)   # self可以换成 A

    a = A(3)
    a.judge()
    A.judge(a.i)    # 这样也可以，但是觉得违背了class封装的思想
