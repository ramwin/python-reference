#!/bin/bash
# Xiang Wang(ramwin@qq.com)
#
set -ex

# rm dist/*
hatch build
hatch publish
# python3 setup.py sdist bdist_wheel
# twine upload dist/*"
