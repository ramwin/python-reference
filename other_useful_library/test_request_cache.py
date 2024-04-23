#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import requests_cache


session = requests_cache.CachedSession(
        'demo_cache',
        backend="filesystem",
        use_cache_dir=False,
        allowable_methods=["GET"],
)


def main():
    res = session.get('http://localhost:18000')


main()
