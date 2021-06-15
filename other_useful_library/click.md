#### Xiang Wang @ 2016-10-13 01:19:39

# click，把python脚本变成命令

[官网教程][website]

# 基础
```
import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(click.style('!'*100 + 'Hello %s!' % name, bg='blue', fg='red', bold=True, blink=True, underline=True))

if __name__ == '__main__':
    hello()
```


# 参数
* 添加是否`dry_run`  
这样就可以`python3 run.py --dry-run // python3 run.py -n了`  
default为False, 传入了才是True, 请不要设置default为True, 这样传入了反而是False, 不方便阅读和理解


    @click.option("--dry-run", "-n", is_flag=True)
    def test(*args, **kwargs):
        assert isinstance(kwargs["dry_run"], bool)
        if kwargs["dry_run"]:
            return


* @click.option("--core", default=1)  # 根据default的类型，会自动转化
* @click.argument('name')  # 参数，最后的参数
* @click.option('--name')  # 使用 --name <value> 的参数
    if_flag=False  # 默认是否为布尔选项参数
* @click.confirm('-r')  # 确认
    text="删除文件"  # 确认的内容


# 选项
* required=False  # 是否需要，默认 False
* default="name"  # 默认的数值, 如有有prompt，则会显示在中括号里面
* prompt='Your name'  # 如果没有输入, 弹出提示让用户输入
* help="输入你的名字"  # 帮助内容里面的信息


[website]: https://click.palletsprojects.com/en/8.0.x/quickstart/
