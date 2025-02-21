#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
找到redis最快使用的方式
a: list 的rpush, lpop. 每次分别插入item_length个, 每个字符长度string_size
"""


import time

import redis
from humanfriendly import parse_size
import optuna


def check(size, item_length, string_size, insert_direction, pop_direction): \
        # pylint: disable=unused-argument
    """测试使用这些参数插入redis速度库的速度是多少"""
    start = time.time()
    key = "test_speed"

    client = redis.StrictRedis(
        host="lte.test.huawei.com",
        port=6380,
        password="5c22fe36e7933f406cdac2a4b9ee104b",
    )
    client.delete(key)
    string = " " * string_size

    for _ in range(int(size / string_size / item_length)):
        if insert_direction == "left":
            client.lpush(key, *([string] * item_length))
        elif insert_direction == "right":
            client.rpush(key, *([string] * item_length))
        else:
            raise ValueError

    return time.time() - start


def objective(trial):
    """外部框架代码"""
    string_size = trial.suggest_int("字符长度", 1, 10000)
    item_length = trial.suggest_int("一次插入长度", 1, 1024)
    insert_direction = trial.suggest_categorical("pop方向", ["left", "right"])
    pop_direction = trial.suggest_categorical("insert方向", ["left", "right"])
    return check(parse_size("5M"), item_length, string_size,
                 insert_direction, pop_direction)


study = optuna.create_study(
    storage="sqlite:///db.sqlite3",
    study_name="找到redis最适合的参数-1M数据大小-10次", direction="minimize",
)
# study = optuna.load_study(
#     storage="sqlite:///db.sqlite3",
#     study_name="找到redis最适合的参数-10M数据大小-300次-远程服务器",
#     # direction="minimize",
# )
study.optimize(objective, n_trials=300)

print(study.best_params)
