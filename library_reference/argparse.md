**Xiang Wang @ 2019-02-27 18:57:23**


### argparse tutorial
[官网](https://docs.python.org/3/howto/argparse.html#id1)

#### Concepts
* command: `ls`
* positional argument: `ls DESC`
* optional argument: `ls -l`
* help text: `ls --help`

#### The basics
```
import argparse
parser = argparse.ArgumentParser()
parser.parse_args()
```

#### Introducing Positional arguments
* 添加一个参数
```
parser.add_argument("echo", help="echo the string you use here")
```
* 添加一个数字参数
```
parser.add_argument("square", help="展示一个数字", type=int)
```

#### [ ] Introducing Optional arguments
#### [ ] Combining Positional and Optional arguments
#### [ ] Getting a little mode advanced
#### [ ] Conclusion

### argparse
[官网](https://docs.python.org/3/library/argparse.html)
[测试](../test/argparse_test.py)

#### Example
```
import argparse

parser = argparse.ArgumentParser(description="我是一个用来处理几个数字的脚本")
parser.add_argument("integers", metavar='N', type=int, nargs="+", help="an integer for the accumulator")
parser.add_argument("--sum", dest="accumulate", action="store_const", const=sum, default=max, help="找到最大的数字 (default: find the max)")


args = parser.parse_args()
print(args.accumulate(args.integers))
```

#### ArgumentParse objects
##### type


#### The `add_argument()` method

#### The `parse_args()` method

#### Other utilities

#### Upgrading optparse code
