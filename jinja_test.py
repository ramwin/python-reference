#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-02-10 15:32:42

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
