#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2018-10-11 22:02:55


from PIL import Image
img = Image.open('png.png', 'r')
img = img.resize((192, 108))
basic_html = """
<html>
    <style>
        div.row {
            display: flex;
        }
        div {
            min-height: 10px;
            min-width: 10px;
        }
    </style>
    <body>
"""


for row_number in range(img.size[1]):
    row_html = '<div class="row">'
    for column_number in range(img.size[0]):
        r, g, b, t = img.getpixel((column_number, row_number))
        div_html = '<div style="background-color: rgb({r}, {g}, {b}, {t})"></div>'.format(r=r, g=g, b=b, t=t)
        # div_html = '<div class="red"></div>'
        row_html += div_html
    row_html += "</div>\n"
    basic_html += row_html

basic_html += """
    </body>
</html>
"""

f = open('test.html', 'w')
f.write(basic_html)
f.close()
