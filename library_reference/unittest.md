# [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
```python
import unittest

class MyTest(unittest.TestCase):

    def test_divide_zero(self):
        with self.assertRaises(ZeroDivisionError):
            1/0
            pass

if __name__ == "__main__":
    unittest.main()
```

## [TestCase](https://docs.python.org/3/library/unittest.html#test-cases)

* [setUp](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp)  
每次执行前都调用. 各个test的函数分别调用的

* [tearDown](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDown)  
每次执行单元测试时, 最后都调用这个, 即使raise Exception了

### [assets methods](https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug)  

* assert**Equal**, assertNotEqual, 
* assert**True**, assertFalse, 
* assert**Is**, assertIsNot, 
* assert**IsNone**, assertIsNotNone, 
* assert**In(a, b)**, assertNotIn
* assert**IsInstance**, assertNotIsInstance
* assert*Raises*
```
with self.assertRaises(SomeException):
    do_something()  如果do_something 不报这个 SomeException, 就失败
```
* `assertRaisesRegex(exception, regex)`
注意, 这个的regex和re.match不一样, 不需要从头匹配
```
with self.assertRaisesRegex(Exception, "自定义") as e:
    pass
print(e.exception)
# 也可以让这个assertraise来调用函数callable
self.assertRaisesRegex(exception, regex, callable, *args, **kwds)
```

* assertAlmostEqual
把a和b进行对比, 得到的值取places的精度. 看是否为0. 也可以传入delta, 看绝对误差多少
```
self.assertAlmostEqual(3.1415, 3.14, places=2)
self.assertAlmostEqual(100, 100.9, delta=1)
```

* `addCleanup(function, /, *args, **kwargs)`
```python
class MyTest(unittest.TestCase):

    def after(self, *args, **kwargs):
        print(args)  # addCleanup的参数会放进来, 这样可以在单元测试内打开文件, 传入fd. 这里close了
        print("after")

    def test_raise(self):
        self.addCleanup(self.after, 1, 2)
        with self.assertRaises(ZeroDivisionError):
            1/2
        print("测试完毕")

    def test_divide_zero(self):
        self.addCleanup(self.after, 1, 2)
        with self.assertRaises(ZeroDivisionError):
            1/0
        print("测试完毕")
```

## Class and Module Fixtures
模块执行和Class的setUpClass都只会调用一遍.  
[测试](../test/test_unittest_fixture.py)

```
# test_function.py
def setUpModule():
    print("模块执行前调用")

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("class 之前调用")

    @classmethod
    def tearDownClass(cls):
        print("class 之前调用")

def tearDownModule():
    print("模块执行后调用")

```
