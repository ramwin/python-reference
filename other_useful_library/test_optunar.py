#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
找到redis最快的参数
"""

import time
import optuna
from redis import Redis


def test(direction, string_size, batch_size) -> float:
    total = 1024 * 1024 * 128
    client = Redis()
    client.delete("list")
    start = time.time()
    if direction == "RPUSH":
        for _ in range((total // string_size + 1) // batch_size + 1):
            data = ["a" * string_size] * batch_size
            client.rpush("list", *data)
    elif direction == "LPUSH":
        for _ in range((total // string_size + 1) // batch_size + 1):
            data = ["a" * string_size] * batch_size
            client.lpush("list", *data)
    else:
        raise ValueError
    end = time.time()
    print(f"每次插入 {batch_size} 条长度为 {string_size}的字符串耗时: {end-start}")
    return end - start


def objective(trial):
    direction = trial.suggest_categorical('direction', ["RPUSH", "LPUSH"])
    string_size = trial.suggest_int("string_size", 2, 102400)
    batch_size = trial.suggest_int("batch_size", 2, 102400)
    speed = test(direction, string_size, batch_size)
    return speed


study = optuna.create_study()
study.optimize(objective, n_trials=20)
