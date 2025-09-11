#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#matplotlib inline
#config InlineBackend.figure_format='svg'      # 设置为矢量图格式

# plt.rcParams["font.sans-serif"] = ["SimHei"]   # 兼容中文

plt.figure(figsize=(10,6))                     # 设定画布大小
x = np.random.rand(10000)
y = np.random.rand(10000)
plt.plot(x)
plt.plot(y)
plt.legend(["x", "y"])                  # 图例
plt.savefig("plt_test.svg")                    # 保存svg图
