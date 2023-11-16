#!/bin/bash
# Xiang Wang(ramwin@qq.com)


pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple 
pip install -U pip
pip install ipdb requests tldr redis click flake8 beautifulsoup4 pylint
pip install django django-redis djangorestframework pylint-django
