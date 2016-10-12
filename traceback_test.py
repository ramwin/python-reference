#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-09-28 13:53:13

import traceback
import sys
import time

def log_error(f):
    def fin(*args, **kw):
        try:
            return f(*args, **kw)
        except Exception as e:
            print("遇到了错误")
            print('repr(e):')
            error_msg = repr(e)
            # error = traceback.format_exc()
            print(e)
            print('dir(e): ')
            print(dir(e))
            print('e.message: ')
            print(e.message)
            print('print e.args: ')
            print(e.args)
            etype, value, tb = sys.exc_info()
            # print(etype)  # <type 'exceptions.ZeroDivisionError'>
            print('print etype:')
            print(etype)
            # print(value)  # integer division or modulo by zero
            tb_in = tb.tb_next  # 获取上层的 traceback
            # print(tb_in)  # 一个 traceback
            # print(type(tb_in))
            # l = traceback.format_tb(tb_in)
            print(tb_in.tb_lineno)  # 行号
            filename, lineno, functionname, code = traceback.extract_tb(tb_in)[0]  # 上下文
            text = "{time} [ERROR] {error_msg} in file {filename} on line {lineno}".format(
                time=time.strftime('%Y-%m-%d %H:%M:%S'),
                error_msg=error_msg,
                filename=filename,
                lineno=lineno,
                )
            print(text)
            return "结束"
    return fin


@log_error
def main():
    return 1/0


if __name__ == '__main__':
    print(main())
