#### Xiang Wang @ 2017-02-10 15:30:06

## 基础
* [官网教程](http://jinja.pocoo.org/docs/2.9/intro/#basic-api-usage)
* [示例代码](./jinja_test.py)
```
    from jinja2 import Template

    template = Template((
        "<title>{{title}}</title>"
        "friends:"
        "{% for friend in friends %}"
            "{{friend.name}}"
        "{% endfor %}"
    ))
    result = template.render(title='标题', friends=[{'name':'男朋友'}, {'name':'女朋友'}])
    print(result)
```
