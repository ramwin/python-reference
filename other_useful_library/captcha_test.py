#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-11-18 18:20:41


from captcha.image import ImageCaptcha

image = ImageCaptcha(fonts=['/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-B.ttf', '/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-R.ttf'])

data = image.generate('1234')
image.write('1234', 'out.png')
