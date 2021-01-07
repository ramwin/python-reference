#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2021-01-07 10:23:44


from ordered_set import OrderedSet
from threading import Thread

print("测试多线程导致sorted_set数据重复的问题")


import time


# 自己用的class有这个问题
# class A(object):
# 
#     def __init__(self):
#         self.keys = []
# 
#     def run(self):
#         print("我开始run啦")
#         if 1 not in self.keys:
#             print("两次都发现不存在哟")
#             time.sleep(1)
#             self.keys.append(1)
#             print("我插入啦")
#         print(self.keys)
#         print("执行结束")
# 
# 
# def run():
#     a = A()
#     t1 = Thread(target=a.run)
#     t1.start()
#     t2 = Thread(target=a.run)
#     t2.start()
#     a.run()
# 
# 


def run():
    s = OrderedSet()
    threads = []
    for i in range(1000):
        threads.append(Thread(target=s.add, args=["test a very long key"]))
    for t in threads:
        t.start()
    print(s)


if __name__ == "__main__":
    run()
