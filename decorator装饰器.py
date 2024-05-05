class locker:
    def __init__(self):
        print("locker.__init__() should be not called.")

    # @staticmethod
    # def acquire():
    #     print("locker.acquire() called.(静态方法)")

    # @staticmethod
    # def release():
    #     print("locker.release() called.(不需要实例)")

@deco(locker)
def myfunc():
    print('myfunc() called.')
myfunc()
# myfunc(text='text exists')
# myfunc = deco(myfunc)
# myfunc()


from functools import update_wrapper
## 但是这样 docstring就变了
def log(f):
    print('log')
    print(f.__name__)
    def fin(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            return '出现错误, 但是我不告诉你错误是什么'
    return update_wrapper(fin, f)

@log
def main():
    """ main docstring """
    print(1)

# main()
# print(main.__doc__)
