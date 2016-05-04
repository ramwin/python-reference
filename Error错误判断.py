#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-01-03 21:10:49

def main():
    try:
        1/0
    except ZeroDivisionError:
        print('不能除以0')
    except Exception as err:
        print(err)
if __name__=='__main__':
    main()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-01-03 14:31:25

def main2():
    '''python2 的用法'''
    try:
        1/0
    except Exception,e:
        print e.message
def main3():
    '''python3 的用法, 最新版本的2也支持。'''
    try:
        1/0
    except Exception as err:
        print(err)
if __name__ == '__main__':
    main3()
