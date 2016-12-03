from PyWinMouse import *
import time

"""
windows下把有道云笔记的单词设置成记住的代码
"""

def main(n=10):
    print("move your mouse to 点击显示释义")
    time.sleep(3)
    a = Mouse()
    center = a.get_mouse_pos()
    print("move your mouse to 记得")
    time.sleep(3)
    checked = a.get_mouse_pos()
    for i in range(n):
        time.sleep(0.01)
        a.move_mouse(*center)
        time.sleep(0.01)
        a.left_click()
        time.sleep(0.01)
        a.move_mouse(*checked)
        time.sleep(0.01)
        a.left_click()
def cheet():
    a = Mouse()
    start = time.time()
    for _ in range(123):
        a.left_click()
        a.left_click()
    end = time.time()
    print(end-start)

number = input("输入你要执行的次数: ")
number = int(number)
main(number)
