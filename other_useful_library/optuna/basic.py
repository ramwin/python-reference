#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import optuna


def objective(trial):
    x = trial.suggest_float('x', -2, 2)
    y = trial.suggest_categorical("y", ["乘法", "指数", "加法", "平方"])
    if y == "指数":
        return 2 ** x
    if y == "平方":
        return x * x
    if y == "加法":
        return x + 2
    if y == "乘法":
        return x * 2


# study = optuna.create_study(
#     study_name="比比谁更大-10000次",
#     storage="sqlite:///db.sqlite3", direction="maximize",
# )
study = optuna.study.load_study(
    study_name="比比谁更大-10000次",
    storage="sqlite:///db.sqlite3",
)
study.optimize(objective, n_trials=10000)


print(study.best_params)
