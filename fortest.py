#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-09-29 18:18:10

for i in range(10):
    if i > 5:
        continue
    print(i)
else:
    print('输出完毕')


class myrange(object):
    def __init__(self, n):
        self.max = n
        self.i = 0

    def __iter__(self):

        while self.i < self.max:  # 第一种写法
            self.i += 1
            yield self.i

        while True:  # 第二种写法
            self.i += 1
            if self.i > self.max:
                print("最大")
                raise StopIteration
            else:
                yield self.i


for i in myrange(n = 10):
    print(i)
print("结束")
