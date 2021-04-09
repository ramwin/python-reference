import threading
import random
from threading import local, Thread
import time
import os


_thread_locals = local()
_thread_locals.cnt = 1


def print_local(*args, **kwargs):
    process_id = os.getpid()
    print(f"当前进程id: {process_id}")
    thread_id = threading.current_thread().native_id
    print(f"    当前线程id: {thread_id}")
    time.sleep(random.random() * 10)
    print("sleep结束")
    if not hasattr(_thread_locals, "cnt"):
        print(f"线程{thread_id}没有 cnt")
        _thread_locals.cnt = random.randint(100, 200)
    print(f"当前cnt: {_thread_locals.cnt}")
    _thread_locals.cnt += 1
    print(f"加1了cnt: {_thread_locals.cnt}")


def main():
    print_local()
    s1 = Thread(target=print_local)
    s1.start()
    s2 = Thread(target=print_local)
    s2.start()
    print_local()
    # s2 = Thread(target=print_local, args=[], kwargs=[])
    # s2.start()

if __name__ == '__main__':
    main()
