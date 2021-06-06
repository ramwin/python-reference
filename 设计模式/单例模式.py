# 直接初始化好


class A:

    def __init__(self):
        self.count = 0

    def __str__(self):
        print(self.count)


a = A()


# 使用new


class B(object):

    def __init__(self):
        print("重新init")

    def init(self):
        self.count = 0

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            print("重新生成B")
            cls._instance = object.__new__(cls)
            cls._instance.init()
        else:
            print("有了")
        return cls._instance
