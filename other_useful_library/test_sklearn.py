#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 王祥 <ramwin@qq.com>

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression   # pip install scikit-learn

# 假设已有 DataFrame df
df = pd.DataFrame({'年龄':[...], '身高':[...]})

# ----------------------------------------------------------------------
# 1. 训练模型
# ----------------------------------------------------------------------
X = df[['年龄']].values          # 二维数组 (n_samples, 1)
y = df['身高'].values            # 一维数组 (n_samples,)

model = LinearRegression()       # 如果关系是曲线，可换成 PolynomialFeatures + LinearRegression
model.fit(X, y)

# ----------------------------------------------------------------------
# 2. 预测函数
# ----------------------------------------------------------------------
def predict_height(age: float | int | np.ndarray, df, x_column: str, y_column: str) -> float | np.ndarray:
    """
    根据年龄预测身高。
    参数
    ----
    age : float, int 或 array-like
        任意年龄值或数组。
    返回
    ----
    float 或 np.ndarray
        对应的预测身高。
    """
    model = LinearRegression()
    model.fit(
            df[[x_column]].values,
            df[y_column].values,
    )
    age = np.asarray(age).reshape(-1, 1)   # 转成二维
    return model.predict(age).squeeze()    # 去掉多余维度

# ----------------------------------------------------------------------
# 3. 使用示例
# ----------------------------------------------------------------------
print(predict_height(10))          # 单个年龄
print(predict_height([5, 7, 12]))  # 多个年龄
