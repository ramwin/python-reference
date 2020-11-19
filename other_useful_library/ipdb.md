**Xiang Wang @ 2019-07-09 16:39:26**

## ipdb
[github](https://github.com/gotcha/ipdb)

### 用法
```
import ipdb
ipdb.set_trace(context=5)  # 显示5行
```

### API
#### EOF
停止运行
> Handles the receipt of EOF as a command.

#### a
查看当前函数的参数
> Print the argument list of the current function.

#### c
继续执行剩下的代码
> Continue execution, only stop when a breakpoint is encountered.

#### l (line)
显示某行的代码. 默认是当前`set_trace`的下一行代码. 继续l会显示接下来的代码

#### s(tep)
执行一行代码, 或者进入函数内部
> Execute the current line, stop at the first possible occasion (either in a function that is called or in the current function).

#### n(ext)
> Continue execution until the next line in the current function is reached or it returns.

#### unt(il) [lineno]
继续执行直到运行到某一行的行数大于指定的lineno

#### r(eturn)
运行函数直到当前函数返回数据
> Continue execution until the current function returns.

#### p(print)
> Print the value of the expression.
