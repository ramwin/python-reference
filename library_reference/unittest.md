**Xiang Wang @ 2019-02-27 10:56:52**


### [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
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

#### [TestCase](https://docs.python.org/3/library/unittest.html#test-cases)

* [setUp](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp)  
每次执行前都调用. 各个test的函数分别调用的

* [tearDown](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDown)  
每次执行单元测试时, 最后都调用这个, 即使raise Exception了

* [assets methods](https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug)  
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
