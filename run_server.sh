#!/bin/bash
# Xiang Wang(ramwin@qq.com)

if [ -d _build ]
then
    rm -r _build
fi

sphinx-autobuild \
    --port 18000 \
    -j auto \
    --verbose \
    . _build/html/ \
    --re-ignore "\.mypy_cache" \
    --re-ignore "\.git"    \
    --re-ignore "\.*\.swp" \
    --re-ignore "\.*\.log" \

