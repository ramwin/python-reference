#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-02-27 18:58:27


import argparse

parser = argparse.ArgumentParser()

# 添加 Positional arguments
# parser.add_argument("echo", help="写入你希望输出的字符")
# parser.add_argument("square", help="给我一个数，还你他平方", type=int)
# parser.add_argument("--verbosity", help="详细信息")
parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")


args = parser.parse_args()
# print(args.echo)
# print(f"{args.square}的平方是: {args.square**2}")
# print(args.verbosity)
# if args.verbosity:
#     print("verbosity: on")
if args.verbose:
    print("verbose: on")
