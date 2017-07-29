#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-06-23 15:10:57


import redis
import time
import json

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
def get_cache(f):
    def f_in(company_name):
        r = redis.Redis(connection_pool=pool)
        if r.get(company_name):
            res = json.loads(r.get(company_name).decode('utf8'))
        else:
            res = f(company_name)
            r.set(company_name, json.dumps(res, indent=4), 5)
        return res
    return f_in


@get_cache
def slow_function(number):
    time.sleep(number)
    print(number)
    return number


if __name__ == '__main__':
    print(slow_function(2))
    print(slow_function(2))
