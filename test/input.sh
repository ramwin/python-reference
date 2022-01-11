#!/bin/bash
# Xiang Wang(ramwin@qq.com)

while [ 1 ]; do
    echo "等待输入..."
    read text;
    echo "您输入了: " $text;
    if [ ! $text ]; then
        exit 0
    fi
done
