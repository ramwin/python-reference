#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import logging
from multiprocessing import Pool

import pandas


logging.basicConfig(level=logging.INFO, format="%(process)d %(message)s")


def get_data(f):
    logging.info(f"打开文件{f}")
    df = pandas.read_csv(f)
    logging.info(f"dataframe的地址: {id(df)}")
    return df


def test1():
    logging.info("这个例子可以看出Pool执行后，可以返回pandas DataFrame object地址会变动，有一次内存拷贝")
    with Pool() as p:
        res = p.map(get_data, ["一班.csv", "二班.csv"])
    for i in res:
        logging.info(f"最后得到dataframe的地址{id(i)}")
    return res


if __name__ == "__main__":
    test1()
