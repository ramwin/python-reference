**Xiang Wang @ 2019-02-27 10:56:52**


### [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)


    import unittest

    class MyTest(unittest.TestCase):

        def test_divide_zero(self):
            with self.assertRaises(ZeroDivisionError):
                1/0
                pass

    if __name__ == "__main__":
        unittest.main()

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
