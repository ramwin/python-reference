**Xiang Wang @ 2018-09-13 19:30:55**

## [Built-in Functions](https://docs.python.org/3/library/functions.html#built-in-funcs)
### abs
### all: return True is all elements are True
### any: return True is any elements is True
### breakpoint: new in version 3.7, like `pdb.set_trace()`
### callable: False: 肯定无法调用
### delattr(object, name): del x.foobar
### divmod(a, b): (a // b, a % b)
### [ ] [to be continued](https://docs.python.org/3/library/functions.html#divmod)
### [property](https://docs.python.org/3/library/functions.html#property)
可以用来创建一个property
property(fget=None, fset=None, fdel=None, doc=None)  # 里面的参数代表调用`c.x`, `c.x = value` `del c.x`是调用的函数

    ```
    class C:
        def __init__(self):
            self._x = None

        def getx(self):
            return self._x

        def setx(self, value):
            self._x = value

        def delx(self):
            del self._x

        x = property(getx, setx, delx, "I'm the 'x' property.")

    class Student(object):

        def __init__(self, name, age):
            self.name = name
            self._age = age

        @property
        def age(self):
            print("%s的年龄是%d" % (self.name, self._age))

        @age.setter
        def age(self, value):
            if value < 0:
                print("你的设置的年龄%d不正确" % value)
            else:
                self._age = value

    student = Student("小明", 20)
    student.age
    student.age = -1
    student.age
    student.age = 21
    student.age
    ```
